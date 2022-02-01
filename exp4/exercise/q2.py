class Employee:
    def __init__(self,post,no):
        self.post=post
        self.No_of_Employee=no
    def printing(self,post,No_of_Employee):
        print("Your Post is : ",self.post)
        print("The number of employees is : ",self.No_of_Employee)
class Manager(Employee):
    def __init__(self,post,no):
        super().__init__(post,no)
        super().printing(post,no)
a=Manager("CEO", 77)
