import json
class Customer:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self):
        return{
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
John = Customer(1, 'John', 'Smith')
Jane = Customer(2, 'Jane', 'Doe')

class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def to_json(self):
        return {
            "account_id": self.account_id,
            "balance": self.balance,
        }
john_account1 = (Account(1,1000))      
jane_account1 = (Account(2,2000))
   
class Bank:
    def __init__ (self):
        self.customers = []
        self.accounts = []
    def add_customer(self, customer):
        self.customers.append(customer)
    def add_account(self,account):
        self.accounts.append(account)
    def to_json(self):
            customers_json = [customer.to_json() for customer in self.customers]
            accounts_json = [account.to_json() for account in self.accounts]
            return{ 
                    "customers": customers_json,
                    "accounts" : accounts_json,

                }
the_bank= Bank()       
the_bank.add_customer(John)
the_bank.add_customer(Customer(1, 'John' , 'Smith'))
the_bank.add_account(john_account1)
the_bank.add_customer(Jane)
the_bank.add_customer(Customer(2, 'Jane' , 'Doe' ))
the_bank.add_account(jane_account1)


bank_info = json.dumps(the_bank.to_json(), indent=2)
print(bank_info)