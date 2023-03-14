def study_schedule(permanence_period, target_time):
    counter = 0

    if not target_time:
        return None

    for time in permanence_period:
        index = 0

        if not isinstance(time[index], int) or not isinstance(
            time[index + 1], int
        ):
            return None

        if target_time in range(time[index], time[index + 1] + 1):
            counter += 1

    return counter
