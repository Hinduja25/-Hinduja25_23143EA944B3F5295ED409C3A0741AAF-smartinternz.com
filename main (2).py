implement a class called bank account that represents a bank account.

class bankaccount:
  def __init__(self, account_number,account_holder_name,initial_balace=0.0):
    self.__account_number=account
      _number
    self.__account_holder_name=
      account_holder_name
    self.__account_balance=initial
       _balance
  def deposit(self,amount):
    if amount>0:
      self.__account_balace+=amount
      print("deposited {}.new balance: {}".format(amount,self.__account_balance))
    else:
      print("invalid withdrawal amount or insufficient balance:")
  def display_balance(self):
    print("amount balance for {}(account #{}): {}".format(
    self.__account _holder_name
    self__account_number,
    self.__account_balance))
    
    
