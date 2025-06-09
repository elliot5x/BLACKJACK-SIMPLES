import random
from colorama import Fore, Style, Back, init
from sys import exit
from os import system, name

init(autoreset=True)

cartas = [1,2,3,4,5,6,7,8,9,10,10,10,10]

suas_cartas = []
npc_cartas = []

nome = Fore.GREEN + "MARQUES"
maquina = Fore.YELLOW + "MAQUINA"

def cls():
    system('cls') if name == 'nt' else system('clear')
cls()

def menu():
    while True:
        try:
            cls()
            print("==== BLACKJACK ====\n")
            print("[1] Jogar\n[2] Sair\n")
            digite = int(input(">> "))
            opcoes = {1: jogo,2: exit}
            if digite in opcoes:
                opcoes[digite]()
            else:
                print("ERRO: Numero errado.")
                input("\nENTER para continuar")
                
        except ValueError:
            print("ERRO: Proíbido letras.")
            input("\nENTER para continuar")

def npc():
    while True:
        try:
            cls()    
            print(f"Adicionando mais uma carta...\n")
            npc_cartas.append(random.choice(cartas))
            print(f"{maquina}:", f"{sum(npc_cartas)}")
            input("\nENTER para continuar")

            if sum(npc_cartas) > 21:
                cls()
                print(f"{maquina}", f"perdeu com: {sum(npc_cartas)}\n")
                input("\nENTER para continuar")
                npc_cartas.clear()
                suas_cartas.clear()
                menu()
            if sum(npc_cartas) == 21:
                cls()
                print(f"{maquina}", "venceu\n")
                print(f"Resultado: {sum(npc_cartas)}")
                input("\nENTER para continuar")
                npc_cartas.clear()
                suas_cartas.clear()
                menu()                
            else:
                jogo()

        except ValueError:
            print("ERRO: Apenas aperte ENTER.")
            input("\nENTER para continuar")

def jogo():
    while True:
        try:
            cls()
            print(f"Adicionando mais uma carta...\n")
            suas_cartas.append(random.choice(cartas))
            print(f"{nome}", f": {sum(suas_cartas)}")
            input("\nENTER para continuar")
            
            if sum(suas_cartas) == 21:
                cls()
                print(f"{nome}", "venceu\n")
                print(f"Resultado: {sum(suas_cartas)}")
                input("\nENTER para continuar")
                suas_cartas.clear()
                npc_cartas.clear()
                menu()    
            if sum(suas_cartas) > 21:
                cls()
                print(f"{nome}", f"perdeu com: {sum(suas_cartas)}\n")
                input("\nENTER para continuar")
                suas_cartas.clear()
                npc_cartas.clear()
                menu()
            else:
                npc()

        except ValueError:
            print("ERRO: Apenas aperte ENTER.")
            input("\nENTER para continuar")
menu()