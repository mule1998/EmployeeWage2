import random
"""Constants"""
is_full_time=2
is_part_time=1
emp_rate_per_hr=20
num_of_working_days=20
emp_hrs=0
emp_wage=0
total_emp_wage=0
#computation
for i in range(0,num_of_working_days):
    rand=random.randint(0, 3)
    if rand==is_full_time:
        emp_hrs=8
    elif rand==is_part_time:
        emp_hrs=4
    else:
        emp_hrs=0
    emp_wage=emp_hrs*emp_rate_per_hr
    total_emp_wage+=emp_wage
    print("Employee Wage of the day: ",emp_wage)
print("Total Emp Wage",total_emp_wage)