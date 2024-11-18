import math


def estimate_approach_queue_resolution_time(
        LaneQueue,  # список списков n*Q
        reductionByDynamicCoeffs,  # массив коэффициентов сокращения (массив VEHICLE_TYPES_COUNT)
        reductionByConditionCoeffs,  # список коэффициентов сокращения по условиям
        turningRadiuses,  # список радиусов поворота
        additional_delay_times,  # список дополнительных задержек
        rightOfWayIntervals,  # пара (начало, конец) интервалов приоритета
        cycle,  # длина цикла
        nActualOutCount,  # фактическое количество выходов
        InLanesCount  # количество входных полос
):
    # s0 - стандартный поток насыщения
    s0 = 1900  # примерное значение (может быть изменено)

    # tLoss - максимальное время потерь насыщенности
    tLoss = 3

    # lG - длительность интервала разрешённого движения
    lG = rightOfWayIntervals[1] - rightOfWayIntervals[0]

    # Общий нормализованный поток Q(*)
    totalNormalizedFlow = 0

    # Расчёт по полосам
    for i, lane in enumerate(LaneQueue):
        rowContribution = 0  # Вклад текущей полосы

        # Расчёт по типам транспортных средств
        for j, queue in enumerate(lane):
            rowContribution += queue * reductionByDynamicCoeffs[j]  # Q * Ks

        # Применение коэффициента условий Ki (если доступно)
        if i < len(reductionByConditionCoeffs):
            rowContribution *= reductionByConditionCoeffs[i]

        # Расчёт коэффициента Km для радиусов поворота
        if i < len(turningRadiuses) and turningRadiuses[i] > 0:
            Km = 1.0 + (1.525 / turningRadiuses[i])
            rowContribution *= Km

        totalNormalizedFlow += rowContribution

    # x - коэффициент загрузки полосы
    x = totalNormalizedFlow / (s0 * (lG - tLoss))

    # Округление до целого числа циклов
    fullCycles = math.ceil(x)

    # lTQ - итоговое время разъезда очереди
    lTQ = (totalNormalizedFlow / s0) + tLoss + (fullCycles * cycle)

    return lTQ


# Пример использования функции
LaneQueue = [[5, 3], [6, 4]]  # пример значений очередей
reductionByDynamicCoeffs = [0.9, 0.8]  # для каждого типа транспорта
reductionByConditionCoeffs = [0.95, 0.85]  # для каждой полосы
turningRadiuses = [12, 15]  # радиусы поворотов для полос
additional_delay_times = [2, 3]  # дополнительные задержки
rightOfWayIntervals = (10, 20)  # интервал приоритета (начало, конец)
nActualOutCount = 2  # количество выходов
InLanesCount = 2  # количество входных полос
cycle = 60  # длина цикла в секундах

result = estimate_approach_queue_resolution_time(
    LaneQueue,
    reductionByDynamicCoeffs,
    reductionByConditionCoeffs,
    turningRadiuses,
    additional_delay_times,
    rightOfWayIntervals,
    cycle,
    nActualOutCount,
    InLanesCount
)

print(f"Время разъезда очереди (lTQ): {result:.2f} секунд")
