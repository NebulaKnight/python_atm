from AccountMovement import AccountMovement

class Account:
    def __init__(self, balance):
        self.__balance = balance
        self.__movements = []

    def getBalance(self):
        return self.__balance

    def withdraw(self, amount):
        operation = False
        if amount > 0:
            if self.__balance >= amount:
                movement = AccountMovement(self.__balance, float(amount))
                self.__movements.append(movement)
                self.__balance -= float(amount)
                operation = True
                print("Se ha retirado el monto de: {amount}\n".format(amount = float(amount)))
            else:
                print("ERROR: Saldo insuficiente\n")
        else:
            print("El monto proporcionado no es valido\n")
        return operation
    
    def showMovements(self):
        print("============Movimientos===========");
        if self.__movements:
            for movement in self.__movements:
                movement.printWithdraw();
        else:
            print("No se encontraron movimientos")