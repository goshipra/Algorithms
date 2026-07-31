#!/usr/bin/env python3
# clockAngle.py
# Author : Shipra


def clock_angle(hours, minutes):
    """Return the smaller angle (in degrees) between the clock hands."""
    minute_hand_angle_per_minute = 360 / 60
    hour_hand_angle_per_minute = 360 / (12 * 60)

    total_hour_angle = (hours * 60 + minutes) * hour_hand_angle_per_minute
    total_minute_angle = minutes * minute_hand_angle_per_minute

    angle = abs(total_hour_angle - total_minute_angle)
    return min(angle, 360 - angle)


if __name__ == "__main__":
    print(clock_angle(2, 45))
