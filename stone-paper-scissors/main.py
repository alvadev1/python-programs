from random import choice


choices_dict = {
    'pedra': 'tesoura',
    'papel': 'pedra',
    'tesoura': 'papel'
}

if __name__ == '__main__':
    print("pedra, papel, tesoura!")

    while True:
        option = input("qual sua escola: ")
        pc = choice(list(choices_dict.keys()))
        print(f"voce: {option}, oponente: {pc}.")
        
        if option == pc:
            print(f"deu empate, vamos de novo.")
            continue

        elif pc == choices_dict[option]:
            print("voce foi o vencedor.")
            break

        elif option == choices_dict[pc]:
            print("oponente foi o vencedor")
            break
