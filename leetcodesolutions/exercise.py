#!/usr/bin/env python3
# exercise.py
# Author : Shipra

MonthlyExpenses = [2200,2350,2600,2130,2190]
print(MonthlyExpenses)
FebExtraExpenses = MonthlyExpenses[1] - MonthlyExpenses[0]
print(FebExtraExpenses)
QuarterTotal = MonthlyExpenses[0] + MonthlyExpenses[1] +MonthlyExpenses[2]
print(QuarterTotal)
print(2000 in MonthlyExpenses)

MonthlyExpenses.append(1980)
print(MonthlyExpenses)
MonthlyExpenses[3]= MonthlyExpenses[3]-200
print(MonthlyExpenses)

