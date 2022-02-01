# employee class code in Python
# class definition
class Employee:
    __name=""
    __department=""
    __salary=0
    # function to set data
    def setData(self,name,department,salary):
        self.__name = name
        self.__department = department
        self.__salary = salary
    # function to get/print data
    def showData(self):
        print("Name :", self.__name)
        print("Department :", self.__department)
        print("Salary :", self.__salary)
# main function definition
def main():
    #Employee Object
    emp=Employee()
    name=input("Enter your name : ")
    department=input("Enter your department : ")
    salary=input("Enter your your salary : ")
    emp.setData(name,department,salary)
    emp.showData()
if __name__=="__main__":
    main()
