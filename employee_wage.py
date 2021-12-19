"""Calculatig monthly employee wage"""

class EmpWage():
    emp_rate_per_hr=20
    days_in_month=20
    hrs_in_month=100
    is_full_time=8
    is_part_time=4
    
    absent=0
    def wage(self):
        work_hrs=0
        work_days=0 
        salary=0
    #computation
        while work_days < self.days_in_month and work_hrs <= self.hrs_in_month :
            work_days+=1
            import random
            rand= random.randint(0, 3)
            if rand==0:
             work_hrs=self.is_full_time
            elif rand==1:
             work_hrs=self.is_part_time
            else:
             work_hrs=self.absent
            work_hrs +=emp_hrs
            if work_hrs>100:
                work_hrs-=emp_hrs
                break
            salary=self.emp_rate_per_hr*work_hrs
    print("Total Salary: " ,salary)
    print("Total Hours: ", work_hrs )

emp=EmpWage()
emp.wage()

