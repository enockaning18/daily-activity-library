# Daily Activity Library

A simple Python library for everyday routines. It helps you add up time spent on activities, see how much of the day is still free, find the longest activity, and check how much is left to reach a daily goal.

The functions are written from scratch with loops. They do not use built-in `sum()` or `max()`.

## Requirements

- Python 3.6 or newer

Check your version:

```bash
python3 --version
```

## How to get the library on your machine

### Option 1: Clone with Git (recommended)

```bash
git clone https://github.com/USERNAME/daily-activity-library.git
cd daily-activity-library
```

### Option 2: Download from GitHub

1. Open the repository on GitHub
2. Click **Code** → **Download ZIP**
3. Unzip the folder
4. Open Terminal and go into the folder:

```bash
cd path/to/daily-activity-library
```

## How to use the functions

### Method 1: Import in Python

1. Open Terminal and go to the project folder:

```bash
cd path/to/daily-activity-library
```

2. Start Python:

```bash
python3
```

3. Import and use a function:

```python
from daily_activity import total_minutes, free_minutes, longest_activity, needed_to_goal

times = [480, 300, 120, 45]
names = ["sleep", "class", "study", "exercise"]

total_minutes(times)
# Output: 945

free_minutes(945)
# Output: 495

longest_activity(names, times)
# Output: "sleep"

needed_to_goal(6500, 10000)
# Output: 3500
```

### Method 2: Use in your own Python file

Create a file (for example `test.py`) in the same folder as `daily_activity.py`:

```python
from daily_activity import total_minutes, free_minutes, longest_activity, needed_to_goal

names = ["sleep", "class", "study", "exercise"]
times = [480, 300, 120, 45]

used = total_minutes(times)
free = free_minutes(used)
longest = longest_activity(names, times)
steps_left = needed_to_goal(6500, 10000)

print(f"Minutes used: {used}")
print(f"Minutes free: {free}")
print(f"Longest activity: {longest}")
print(f"Steps still needed: {steps_left}")
```

Run it:

```bash
python3 test.py
```

## Function reference

### `total_minutes(minutes)`

Adds every number in a list of minutes.

**Parameter:**
- `minutes` — a list of minutes spent on activities

**Returns:**
- The total number of minutes

**Example:**

```python
total_minutes([480, 300, 120, 45])   # returns 945
total_minutes([60, 30])              # returns 90
```

**Error:**
- Raises `ValueError` if the list is empty

```python
total_minutes([])  # ValueError: Cannot total an empty list of minutes
```

### `free_minutes(used_minutes, day_minutes=1440)`

Finds how many minutes are still free in the day. A full day is 1440 minutes (24 hours × 60).

**Parameters:**
- `used_minutes` — minutes already used
- `day_minutes` — length of the day (default is 1440)

**Returns:**
- Minutes still free

**Example:**

```python
free_minutes(945)        # returns 495
free_minutes(60, 120)    # returns 60
```

**Error:**
- Raises `ValueError` if used minutes are more than the day

```python
free_minutes(1500)  # ValueError: Used minutes cannot be more than the day
```

### `longest_activity(names, minutes)`

Walks two lists together and returns the name of the activity with the most minutes.

**Parameters:**
- `names` — a list of activity names
- `minutes` — a list of matching minutes

**Returns:**
- The name of the longest activity

**Example:**

```python
longest_activity(["sleep", "class", "study"], [480, 300, 120])
# returns "sleep"
```

**Error:**
- Raises `ValueError` if a list is empty or the two lists are different lengths

```python
longest_activity(["sleep"], [480, 300])
# ValueError: Each activity name needs a matching number of minutes
```

### `needed_to_goal(current, goal)`

Finds how much is still needed to finish a daily goal (steps, water glasses, study minutes, and so on). If the goal is already met, it returns `0`.

**Parameters:**
- `current` — how much you have done so far
- `goal` — the daily target

**Returns:**
- The amount still needed

**Example:**

```python
needed_to_goal(6500, 10000)   # returns 3500
needed_to_goal(10000, 10000)  # returns 0
needed_to_goal(12000, 10000)  # returns 0
```

**Error:**
- Raises `ValueError` if `current` or `goal` is negative

```python
needed_to_goal(-1, 10000)  # ValueError: Goal and current amounts cannot be negative
```

## How it works (brief)

1. `total_minutes` starts at 0 and adds each activity’s minutes one by one
2. `free_minutes` subtracts used minutes from a 24-hour day
3. `longest_activity` starts with the first activity, then keeps any later activity that took more time
4. `needed_to_goal` subtracts what you have done from the target, and never goes below 0

## Project structure

```
daily-activity-library/
├── daily_activity.py   # The daily activity library
└── README.md           # This documentation
```

## Author

Created for Python class assignment.
