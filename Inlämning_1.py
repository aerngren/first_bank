
import os
import datetime
import json
konton = {}
tiden = datetime.datetime.now()
def ladda_konton():
    if os.path.exists("konton.txt"):
        with open("konton.txt", "r") as f:
            konton_data = json.load(f)
            konton.update(konton_data)

def spara_konton():
    with open("konton.txt", "w") as f:
        json.dump(konton, f, indent=1)

def main():
    ladda_konton()

    while True:
        print(20*"*")
        print("\nHej och välkommer till Adams bankomat, gör ett val")
        print("1 - Skapa ett konto")
        print("2 - Logga in på konto")
        print("3 - Avsluta""\n")
        val = input(">>> ")
        if val == "1":
            skapa_konto()
        elif val == "2":
            logga_in()
        elif val == "3":
            break
        else:
            print("Jag förstod inte ditt val")

    
def skapa_konto():    
    while True:
        print(20*"*")
        print("\n""**Skapa konto**")
        nytt_konto = input('Välj kontonummer, 4 siffror eller avsluta med "q"\n>>> ')
        if nytt_konto == "q":
            break
        elif not nytt_konto.isdigit():
             input('Kontonumret kan endast vara siffror, tryck "Enter" för att försöka igen')
        elif nytt_konto in konton:
            input('Det kontot existarar redan, tryck "Enter" för att försöka igen')
        elif len(nytt_konto) < 4:
            input("För få siffror")
        elif len(nytt_konto) > 4:
            input("För många siffror")
        elif len(nytt_konto) == 4:
            konton[nytt_konto] = {}
            konton[nytt_konto]["pengar"] = [0] 
            konton[nytt_konto]["tid"] = [tiden.strftime("%c")]
            spara_konton()
            break


def logga_in():
    counter = 3
    while counter >= 1:
        print(20*"*")
        print(f"\n***Logga in, du har {counter} försök kvar***")
        print('Skriv in ditt kontonummer eller avbryt med "q"')
        konto_nummer = input("\n>>> ")
        if konto_nummer == "q":
            break
        elif konto_nummer in konton:
            while True:
                print(20*"*")
                print("\nVad vill du göra?")
                print("1 - Ta ut pengar")
                print("2 - Sätt in pengar")
                print("3 - Visa saldo & transaktioner")
                print("4 - Logga ut\n")
                inloggad = input(">>> ")
                if inloggad == "1":
                    while True:
                        print(20*"*")
                        konto_ut = input("\nSkriv in hur mycket du vill ta ut eller avsluta med q\n>>> ").lower().strip()
                        totalen = sum(konton[konto_nummer]["pengar"])
                        if konto_ut == "q":
                            break
                        elif not konto_ut.isdigit():
                            input('Du får ändast använda hela siffror, tryck "Enter"')
                        else:
                            if int(konto_ut) <= 0:
                                input('Du kan inte ta ut 0kr, tryck "Enter"')
                            elif totalen < int(konto_ut):
                                    input(f'Du har inte nog med pengar, du har endast {totalen}kr på kontot, tryck "Enter"')
                            elif totalen >= int(konto_ut):
                                konton[konto_nummer]["pengar"] += [-int(konto_ut)]
                                konton[konto_nummer]["tid"] += [tiden.strftime("%c")]
                                spara_konton()
                                break
                                   
                elif inloggad == "2":
                    while True:
                        print(20*"*")
                        konto_in = input("\nSkriv in hur mycket du vill sätta in eller avsluta med q\n>>> ").lower()
                        if konto_in == "q":
                            break
                        elif not konto_in.isdigit():
                            input('Du får ändast använda hela siffror, tryck "Enter"')
                        elif int(konto_in) == 0:
                            input('Du kan inte sätta in 0kr, tryck "Enter"')
                        else:    
                            konton[konto_nummer]["pengar"] += [int(konto_in)]
                            konton[konto_nummer]["tid"] += [tiden.strftime("%c")]
                            spara_konton()
                            break
                        
                elif inloggad == "3":
                    saldo = sum(konton[konto_nummer]["pengar"])
                    uttag = list(zip(konton[konto_nummer]["pengar"], konton[konto_nummer]["tid"]))
                    print(20*"*")
                    print(f"\nDu har {saldo}kr hos oss och dina senaste transaktioner är:")
                    for i, (transaktion, tid) in enumerate(uttag, 1):
                        if transaktion > 0:
                            print(f"{i}: Insättning: +{transaktion}kr {tid}")
                        else:
                            print(f"{i}: Uttag: {transaktion}kr {tid}")
                    input('Tryck "Enter" när du läst klart')        
                elif inloggad == "4":
                    spara_konton()
                    return
                else:
                    print("Jag förstod inte ditt val, försök igen")
                

        else:
            input(f'\nDu skrev in fel kontonummer, tryck "Enter"')
            counter -= 1



main()