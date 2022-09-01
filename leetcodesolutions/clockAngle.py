#!/usr/bin/env python3
# clockAngle.py
# Author : Shipra

def clockAngle(hours, minutes):
    """
    Given hours and minutes of the clock and return timings
    """

    MinuteHandAnglePerMinute = 360 / 60
    HourHandAnglePerMinute = 360 / (12 * 60)

    TotalHourAngle = (hours * 60 + minutes) * HourHandAnglePerMinute
    TotalMinuteAngle = minutes * MinuteHandAnglePerMinute

    Angle = abs(TotalHourAngle - TotalMinuteAngle)
    MinAngle = min(Angle, 360-Angle)

    return MinAngle


result = clockAngle(12, 30)
print(result)
