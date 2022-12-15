class bank_acc:
    
    def __init__(self, balance = 10000):
        self.balance = balance

    def check_balance(self):
        print("the amount in your account is: ",self.balance)
    
    def deposit(self, dep):
        self.dep = dep
        self.balance + self.dep
        print("the amount in your account is: ", self.balance)
        print("the amount in your acc after deposit: ", self.balance + self.dep)

    def withdrawl(self, wit):
        self.wit = wit
        if (self.wit > self.balance):
            print("insufficeint balance")
        else:
            print(" the amount in your account is: ",self.balance)
            print("the amount after withdrawl from your accunt: ", self.balance - self.wit)

    def transctions(self):
        j=1
        while(j<=3):
            pin = input("enter your pin: ")
            if(pin == "1439"):
                    print('''select your option
                    1.check balance
                    2.withdrawl
                    3.depoist''')
                    choice = int(input("enter your option: "))
                    if(choice == 1):
                        self.check_balance()
                        break
                    elif(choice == 2):
                        wit = int(input("enter your withdrawl amountL: "))
                        self.withdrawl(wit)
                        break
                    elif(choice == 3):
                        dep = int(input("ente ryour deposit amount: "))
                        self.deposit(dep)
                        break
                    else:
                        print("your entered wrong option")
            else:
                print("you enterd wrong pin")
            j=j+1

yash = bank_acc().transctions()