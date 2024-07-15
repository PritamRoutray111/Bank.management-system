# simple banking system for saving account

class account():
    def __init__(self,name,balance):
      self.name=name
      self.balance=balance

    def deposit(self,amount):
      self.balance+=amount
      print("successfully Diposited",amount,"to",self.name,"account total balance is",self.balance)

    def withdrow(self,amount):
      self.balance-=amount
      print(amount,"withdrowed from",self.name,"account remaining balanc is",self.balance)
      
    def get_balance(self):
      return self.balance

print("hello sir welcome to PRSU BANK plese fill the following details to add the account and start saving")
c1=account(input("sir please enter your name::"),int(input("enter the amount to 1st diposit::")))

print("finally your account is created with name",c1.name ,"balance",c1.balance)
print("if you want to diposit money press 1")
print("if you want to withdrow money press 2")
print("if you want to cheak balance press 3")
print("if you want to exit press 4")
while True:
  n=int(input("enter your choice"))
  if n==1:
    c1.deposit(int(input("enter the amount you want to diposit")))

  elif n==2:
    c1.withdrow(int(input("enter the amount you want to withdrow")))

  elif n==3:
    print( "the remaing amount is" ,c1.get_balance())

  else:
    print("thank you for using our bank")
    
    
   # end 
# @copyright:copyright (c) 2024 by PRITAM ROUTRAY
