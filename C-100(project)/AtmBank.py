class Atm:
    def __init__(self, CardNo, pin):
        self.CardNo = CardNo
        self.pin = pin
        self.money = 50000

    def BalanceEnquiry(self, user):
        print("Your balance is " + str(self.money))
        question = input("Do you want do do any other action?(Yes/no)-: ")
        print(question)
        if question == "yes":
            print("Choose your action")
            print("1:Withdrawl")
            print("2:Add Money")
            action = int(input("Enter action number :- "))
            if action == 1:
                user.Withdrawl()
            elif action == 2:
                user.AddMoney()
            else:
                print("number not recognized exiting program")
                exit()
        else:
            print("Thank your for using Atm Bank ")
            exit()

    def Withdrawl(self,user):
        amount = int(input("Enter the amount you want to withdraw - : "))

        if amount > self.money:
            print("Sorry! You do not have" + str(amount) + " Dollars")
            print("You have " + str(self.money) + " Dollars")
        else:
            balance = int(self.money) - amount
            print("Withdrawing Money")
            print()
            print("Here are the " + str(amount) + " Dollars you withdrawed")
            print("$$$$$$")
            print("Your remaining balance is " + str(balance) + " Dollars")

        question = input("Do you want do do any other action?(Yes/no)-: ")
        

        if question == "yes":
            print("Choose your action")
            print("1:Balance Enquiry")
            print("2:Add Money")
            action = int(input("Enter action number :- "))

            if action == 1:
                user.BalanceEnquiry()
            elif action == 2:
                user.AddMoney()
            else:
                print("number not recognized exiting program")
                exit()

        else:
            print("Thank your for using Atm Bank ")
            exit()

    def AddMoney(self,user):
        digit = int(input("Enter the amount you want to tranfer to your bank-: "))
        digits = int("50000") + digit
        print("Adding money")
        print()
        print("Your bank account now has " + str(digits) + " dollars")
        question = input("Do you want do do any other action?(Yes/no)-: ")

        
        if question == "yes":
            print("Choose your action")
            print("1:Balance Enquiry")
            print("2:Withdrawl")
            action = int(input("Enter action number :- "))
            if action == 1:
                user.BalanceEnquiry()
            elif action == 2:
                user.Withdrawl()
            else:
                print("number not recognized exiting program")
                exit()
        else:
            print("Thank your for using Atm Bank ")
            exit()

def main():
    CardNo = input("Please enter your card number:- ")
    Pin = input("Please enter your pin:- ")
    pi = len(Pin)
    pn = list(Pin)
    total = 0
    for x in pn:
        total = total + int(x)
    tot = total
    print(tot)
    print(pi)
    if((pi == 4) and (tot == 16)):
        new_user = Atm(CardNo, Pin)
        print("Choose your action")
        print("1:Balance Enquiry")
        print("2:Withdrawl")
        print("3:Add Money")
        action = int(input("Enter action number :- "))
        if action == 1:
            print("as")
            new_user.BalanceEnquiry(new_user)
        elif action == 2:
            new_user.Withdrawl(new_user)
        elif action == 3:
            new_user.AddMoney(new_user)
        else:
            print("Enter a valid action number")
    else:
        print("Wrong Pin")


if __name__ == "__main__":
    main()
