

class EmpWage():
    emp_rate_per_hr=20
    days_in_month=20
    hrs_in_month=100
    is_full_time=8
    is_part_time=4
    total_salary=0
    total_salary=0
    work_hrs=0
    work_days=0 
    salary=0
    def wage(self):
    #computation
        while work_days < days_in_month and work_hrs <= hrs_in_month :
            import random
            rand= random.randint(0, 3)
            if rand==0:
             salary=is_full_time*emp_rate_per_hr
             work_hrs=work_hrs+is_full_time
             total_salary=total_salary+salary
            elif rand==1:
              salary=is_part_time*emp_rate_per_hr
              work_hrs=work_hrs+is_part_time
              total_salary=total_salary+salary
            else:
                salary=0
                total_emp_hrs+=emp_hrs  

    print("Total Salary: " ,total_salary)
    print("Total days: " ,work_days)
    print("Total Hours: ", work_hrs )

emp=EmpWage()
emp.wage()

