class ATM:
    def __init__(self,balance = 1000):
        self.balance = balance       
    
    def deposit(self,amount):
        self.balance +=amount
        return ("Your current balance is ",str(self.balance)) 
    
    def balanceCheck(self):
        return ("Your balance is ",str(self.balance))
    
    def withdraw(self,amount):
        if self.balance >= amount :
            self.balance -=amount
            return ("Your current balance is ",str(self.balance))
        else :
            return ("Insufficient balance..")
    
    
    


atm = ATM()
      
print("Welcome to ATM....")
while True:
      print("1. Balance check\n2. Deposit\n3. Withdrawal\n4. Exit")
      a = int(input("Enter your choise : "))
      
      if(a==1):
          print(atm.balanceCheck())
      elif(a==2):
          amount = int(input("Enter your amout "))
          print(atm.deposit(amount))
      elif(a==3):
          amount = int(input("Enter your amout "))
          print(atm.withdraw(amount))
      elif(a==4):
          print("Thanks for coming..")
          break
      else:
          print("Invalid choise...")
     
      press = input("Want to continue y/n")
      if(press.lower() != 'y'):
          print("Thanks for coming..")
          break
  
      
      
      
              
              
        