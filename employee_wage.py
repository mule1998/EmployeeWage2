"""Calculatig employee wage for multiple companies"""

class EmpWage():
   
    is_full_time=8
    is_part_time=4
    absent=0
    
    def wage(self,company,hours,days,per_hr):
        work_hrs=0
        work_days=0 
        emp_wage=0
        emp_hrs=0
        #computation
        while work_days < days and work_hrs <= hours :
            work_days+=1
            import random
            rand= random.randint(0, 2)
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
            emp_wage=per_hr*work_hrs
        print("Total Salary: " ,emp_wage)
        print("Total Hours: ", work_hrs )


emp=EmpWage()
emp.wage("BMW", 100, 20, 20)

