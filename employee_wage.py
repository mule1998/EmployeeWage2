import random
"""Constants"""
is_full_time=2
is_part_time=1
emp_rate_per_hr=20
num_of_working_days=20
max_hrs_in_month=100
emp_hrs=0
emp_wage=0
total_emp_hrs=0
total_working_days=0
#computation
while total_emp_hrs<=max_hrs_in_month and total_working_days<num_of_working_days :

    rand=random.randint(0, 3)
    if rand==is_full_time:
        emp_hrs=8
    elif rand==is_part_time:
        emp_hrs=4
    else:
        emp_hrs=0
    total_emp_hrs+=emp_hrs
    print("Day :" ,total_working_days ,"Employee hrs :" ,emp_hrs)
total_emp_wage=total_emp_hrs*emp_rate_per_hr
print("Total employee wage: ",total_emp_wage)
