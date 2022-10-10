from Client import Client

class Atm:
    def __init__(self):
        self.__selectedOption = 0
    
    def login(self, client):
        validation = False
        pin = input("Favor de ingresar su pin:")
        if client.getPin() == pin:
            validation = True
        return validation
    
    def __showMainMenu(self, client):
        option = 0
        try:
            with open("./resources/menus/main.txt", "r") as f:
                menu = f.read().replace("@CLIENT@", client.getName())
            print(menu)
            option = int(input("Seleccionar:"))
        except ValueError:
            print("ERROR: Favor de seleccionar una opción valida")
        return option

    def __balanceOption(self, client):
        while True:
            print("Su saldo es: {balance}".format(balance = client.getAccount().getBalance()))
            option = input("Desea regresar al menú principal? S/N(Otro): ")
            if option.upper() == "S":
                break
    
    def __withdrawOption(self, client):
        while True:
            try:
                print("Su saldo actual es: {balance}".format(balance = client.getAccount().getBalance()))
                amount = float(input("Proporcionar el monto: "))
                client.getAccount().withdraw(amount = amount)
                option = input("Desea realizar otro retiro? S/N(Otro): ")
                if not option.upper() == "S":
                    break
            except ValueError:
                print("ERROR: El monto proporcionado no es valido")

    def __movementsOption(self, client):
        while True:
            client.getAccount().showMovements()
            option = input("Desea regresar al menú principal? S/N(Otro): ")
            if option.upper() == "S":
                break

    def run(self, client):
        while True:
            self.__selectedOption = self.__showMainMenu(client = client)
            if self.__selectedOption == 1:
                self.__balanceOption(client)
            elif self.__selectedOption == 2:
                self.__withdrawOption(client)
            elif self.__selectedOption == 3:
                self.__movementsOption(client)
            elif self.__selectedOption == 4:
                print("Muchas gracias, vuelva pronto")
                break
            else:
                print("ERROR: La opción elegida no existe") 
