num1 =int(input("enter first number: "))
num2 =int(input("enter second number: "))

def Add(num1,num2):
    
    num1 =int(input("enter first number: "))
    num2 =int(input("enter second number: "))
    print("Adding")
    sum=num1 + num2
    print(num1,"+",num2,"=",sum)   
    



def Subtract():
    num1=int(input("enter number to subtract from: "))
    num2=int(input("enter number to subtract: "))
    result=num1-num2
    print(num1,"-",num2,"=",result)


def Multiply():
    num1=int(input("input first number"))
    num2=int(input("input second number"))
    result=num1 * num2
    print(num1,"x",num2,"=",result)

def divide():
    num1 =int(input("input first number"))
    num2 =int(input("input second number"))
    result=num1 / num2
    print(num1,"/",num2,"=",result)



Add(2,3)

def main():
    num1 = input("num1")
    num2 = input("num2")
    operator = input("1: multiply, 2: add")s