import math


def estimate_approach_queue_resolution_time(
        LaneQueue,  # список списков n*Q
        reductionByDynamicCoeffs,  # массив коэффициентов сокращения (массив VEHICLE_TYPES_COUNT)
        reductionByConditionCoeffs,  # список коэффициентов сокращения по условиям
        turningRadiuses,  # двумерный список радиусов поворота для каждой полосы-выхода
        rightOfWayIntervals,  # пара (начало, конец) интервалов приоритета
        cycleLength,  # длина цикла
        nActualOutCount,  # фактическое количество выходов
        InLanesCount  # количество входных полос
):
    # s0 - стандартный поток насыщения (из rightOfWayIntervals)
    s0 = rightOfWayIntervals[0]

    # tLoss - максимальное время потерь насыщенности (из rightOfWayIntervals)
    tLoss = rightOfWayIntervals[1]

    # lG - длительность интервала разрешённого движения
    lG = tLoss - s0

    # Общий нормализованный поток Q(*)
    totalNormalizedFlow = 0

    # Расчёт по полосам
    for i in range(InLanesCount):  # Пробегаем по входным полосам
        for j in range(nActualOutCount):  # Пробегаем по выходам
            rowContribution = 0  # Вклад текущей полосы и выхода
            Km = 1.0  # Коэффициент радиуса поворота

            # Получаем радиус поворота, если доступен
            if i < len(turningRadiuses) and j < len(turningRadiuses[i]):
                specificRadius = turningRadiuses[i][j]
                if specificRadius > 0:
                    Km = 1.0 + (1.525 / specificRadius)  # Km

            # Расчёт по типам транспортных средств
            for k in range(len(reductionByDynamicCoeffs)):  # Пробегаем по типам ТС
                rowContribution += LaneQueue[i][k] * reductionByDynamicCoeffs[k] * Km

            # Применение коэффициента условий Ki (если доступно)
            if i < len(reductionByConditionCoeffs):
                rowContribution *= reductionByConditionCoeffs[i]

            # Добавляем вклад текущей полосы
            totalNormalizedFlow += rowContribution

    # x - коэффициент загрузки полосы
    x = totalNormalizedFlow / (s0 * (lG - tLoss))

    # Округление до целого числа циклов
    fullCycles = math.ceil(x)

    # lTQ - итоговое время разъезда очереди
    lTQ = (totalNormalizedFlow / s0) + tLoss + (fullCycles * cycleLength)

    return lTQ


# Пример использования функции
LaneQueue = [[5, 3], [6, 4]]  # пример значений очередей (по полосам и типам транспорта)
reductionByDynamicCoeffs = [0.9, 0.8]  # коэффициенты сокращения по типам транспорта
reductionByConditionCoeffs = [0.95, 0.85]  # коэффициенты условий по полосам
turningRadiuses = [[12, 15], [14, 20]]  # радиусы поворотов для каждой полосы и выхода
rightOfWayIntervals = (3, 10)  # интервал приоритета (s0, tLoss)
nActualOutCount = 2  # количество выходов
InLanesCount = 2  # количество входных полос
cycleLength = 60  # длина цикла в секундах

result = estimate_approach_queue_resolution_time(
    LaneQueue,
    reductionByDynamicCoeffs,
    reductionByConditionCoeffs,
    turningRadiuses,
    rightOfWayIntervals,
    cycleLength,
    nActualOutCount,
    InLanesCount
)

print(f"Время разъезда очереди (lTQ): {result:.2f} секунд")
