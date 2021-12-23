"""Calculatig employee wage for multiple companies
who's having their own working days and hours
"""
from com import CName

class EmpWage(CName):
   
    is_full_time=8
    is_part_time=4
    absent=0
    

    def wage(self):
        work_hrs=0
        work_days=0 
        self.emp_wage=0
        daily_wage=0
        emp_hrs=0
        self.emp_list1=[]
        #computation
        while work_days < self.days and work_hrs <= self.hours :
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
            self.emp_wage=self.per_hr*work_hrs
            self.daily_wage=self.per_hr*work_hrs
            
            self.emp_list1.append(daily_wage)


    def __str__(self):
        return "company name :"+self.company+" salary: "+str(self.emp_wage)+ " DailyWage "+str(self.daily_wage)
        self.emp_list.append(emp1)
        self.emp_list.append(emp2)
        for i in range(len(emp_list)):
            print(emp_list[i])
emp1=EmpWage("BMW", 100, 20, 20)
emp1.wage()
print(emp1)
emp2=EmpWage("Ferrari", 100, 22, 49)
emp2.wage()
print(emp2)





