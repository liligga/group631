from lessons.lesson_2 import Car

class Money:
    def __init__(self, amount):
        self.amount = amount

    # def __str__(self):
    #     return f"<Money amount={self.amount}>"

    # equal -> ==
    def __eq__(self, other):
        print("other:", other)
        if self.amount == other.amount:
            return True
        return False


    # lt -> less than <
    # gt -> greater than >
    # lte -> less than or equal <=
    # gte -> greater than or equal >=
    def __lt__(self, other):
        print("other:", other)
        if self.amount < other.amount:
            return True
        return False
        # return self.amount < other.amount

    def __gt__(self, other):
        print("other:", other)
        if self.amount > other.amount:
            return True
        return False

    def __add__(self, other):
        print("other:", other)
        new_amount = other.amount + self.amount
        new_money_object = Money(amount=new_amount)
        return new_money_object

if __name__ == "__main__":
    money_igor = Money(100)
    money_kurmanbek = Money(101)
    # money_kurmanbek = money_igor
    money_nursultan = Money(1000)

    print(money_igor)
    print(money_igor == money_kurmanbek)
    print(money_igor < money_kurmanbek)
    print(money_igor > money_kurmanbek)
    total_money = money_igor + money_kurmanbek + money_nursultan
    print(total_money)
    car1 = Car("silver", "Subaru Forester")
