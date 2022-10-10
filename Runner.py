from Atm import Atm
from Client import Client
atm = Atm()
client = Client(name = "Jorge Mauricio Ruiz Flores", pin = "1235", amount = 1000.0)
attempts = 0
while(attempts < 3):
    if(atm.login(client = client)):
        atm.run(client = client)
        break
    else:
        print("ERROR: PIN incorrecto")
        attempts += 1