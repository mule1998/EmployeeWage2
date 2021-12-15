import random
"""Constants"""
is_full_time=1
emp_rate_per_hr=20
emp_hrs=0
emp_wage=0
#computation
rand=random.randint(0, 2)
if rand==is_full_time:
    emp_hrs=8
else:
    emp_hrs=0
emp_wage=emp_hrs*emp_rate_per_hr
print("Employee Wage : ",emp_wage)