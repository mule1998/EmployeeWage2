import employee_wage
class CName:
    '''
    Created class for raise query by comoany
    '''
    def __init__(self,*params):
        self.company=params[0]
        self.hours=params[1]
        self.days=params[2]
        self.per_hr=params[3]
        self.emp_list=[]

    def query(self,name):
        
       
        for i in range(len(self.emp_list)):
            print("Salary : "+str(self.emp_list[i]))
            break
company_name=input(str("Enter a Company's name: "))
cmp=CName()
cmp.query(company_name)