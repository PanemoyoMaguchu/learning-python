CnvrtFrom=str(input("enter the currency you are converting from"))
CnvrtTo=str(input("enter the currency you are converting to"))

if CnvrtTo==CnvrtFrom:
  input=("You cannot do that.")
elif CnvrtFrom!=CnvrtTo:
     input =("Please enter Value")

ammountin=int(input("enter numerical ammount of deposit"))

if CnvrtTo=="rupees" and CnvrtFrom =="pounds":
    cashout=ammountin / 99.67
    input=("your cashout is :"and cashout)

elif CnvrtTo=="pounds" and CnvrtFrom=="rupees" :
    cashout=ammountin* 99.67

elif CnvrtTo=="usd" and CnvrtFrom=="pounds":
    cashout= ammountin /1.22
    input=("your cashout is :"and cashout)

print("Hello")





