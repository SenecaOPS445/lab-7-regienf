#!/usr/bin/env python3
# Student ID: rfrancisco6
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objests and return the sum."""
    total = Time(0,0,0)
    total.hour = t1.hour + t2.hour
    total.minute = t1.minute + t2.minute
    total.second = t1.second + t2.second

    if total.second >= 60:      # Convert
        total.minute += total.second // 60  # COmpute minutes
        total.second = total.second % 60    # Update seconds

    if total.minute >= 60:
        total.hour += total.minute // 60    # Compute hours
        total.minute = total.minute % 60    # Update minutes
    return total

def change_time(t, seconds):
    t.second += seconds

    # Positive seconds
    while t.second >= 60:
            t.second -= 60
            t.minute +=1

    # Negative seconds
    while t.second < 0:
        t.second += 60
        t.minute -= 1

    # Positive minutes
    while t.minute >= 60:
            t.minute -= 60
            t.hour += 1

    # Negative minutes
    while t.minute < 0:
        t.minute += 60
        t.hour -= 1
            
    return None

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True
