from Account import Account
class Client:
    def __init__(self, name, pin):
        self.__name = name
        self.__pin = pin
        self.__account = Account(0.0)
    
    def __init__(self, name, pin, amount):
        self.__name = name
        self.__pin = pin
        self.__account = Account(amount)

    def getName(self):
        return self.__name

    def getPin(self):
        return self.__pin

    def getAccount(self):
        return self.__account