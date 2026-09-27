def total_minutes(minutes):
    """
    Add up how many minutes you spent on activities in a day.
    """
    if not minutes:
        raise ValueError("Cannot total an empty list of minutes")

    total = 0
    for item in minutes:
        total = total + item

    return total


def free_minutes(used_minutes, day_minutes=1440):
    """
    Find how many minutes are still free in the day.
    A full day is 1440 minutes (24 hours * 60).
    """
    leftover = day_minutes - used_minutes
    if leftover < 0:
        raise ValueError("Used minutes cannot be more than the day")

    return leftover


def longest_activity(names, minutes):
    """
    Find the daily activity that took the most time.
    names and minutes must be lists of the same length.
    """
    if not names or not minutes:
        raise ValueError("Cannot find the longest activity from empty lists")
    if len(names) != len(minutes):
        raise ValueError("Each activity name needs a matching number of minutes")

    # Start by assuming the first activity is the longest
    longest_name = names[0]
    longest_time = minutes[0]

    # Go through every activity and keep the one with more minutes
    index = 1
    while index < len(minutes):
        if minutes[index] > longest_time:
            longest_time = minutes[index]
            longest_name = names[index]
        index = index + 1

    return longest_name


def needed_to_goal(current, goal):
    """
    Find how much is still needed to finish a daily goal
    (steps, water glasses, study minutes, and so on).
    """
    if goal < 0 or current < 0:
        raise ValueError("Goal and current amounts cannot be negative")

    leftover = goal - current
    if leftover < 0:
        leftover = 0

    return leftover
