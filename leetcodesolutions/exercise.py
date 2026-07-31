#!/usr/bin/env python3
# exercise.py
# Author : Shipra

monthly_expenses = [2200, 2350, 2600, 2130, 2190]
print(monthly_expenses)

feb_extra_expenses = monthly_expenses[1] - monthly_expenses[0]
print(feb_extra_expenses)

quarter_total = sum(monthly_expenses[:3])
print(quarter_total)

print(2000 in monthly_expenses)

monthly_expenses.append(1980)
print(monthly_expenses)

monthly_expenses[3] -= 200
print(monthly_expenses)
