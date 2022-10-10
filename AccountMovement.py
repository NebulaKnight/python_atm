from datetime import datetime

class AccountMovement:
    def __init__(self, balance, withdraw):
        self.__balance = balance
        self.__withdraw = withdraw
        self.__date = datetime.now()

    def printWithdraw(self):
        dateFormated = self.__date.strftime("%d-%m-%Y %H:%M:%S")
        message = "Saldo: {balance} \t|\t Retiro: {withdraw} \t|\t Fecha: {date}\n".format(balance = self.__balance, withdraw = self.__withdraw, date = dateFormated)
        print(message)
