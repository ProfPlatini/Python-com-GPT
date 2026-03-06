import random


print("Jogo da adivinhação!")
number_max = input("Digite um número para ser o limite de alternativas: ")

if number_max.isdigit():
    print("Você escolheu um número, boa escolha!")
    number_max = int(number_max)
    # print(type(number_max))
else:
    print("Você não escolheu um número!")
    quit()

numero = random.randint(1,number_max)
choices=0
    
while True:
    number_choice = input("Digite um número que você julga estar correto: ")
    choices += 1
    if number_choice.isdigit():
        number_choice = int(number_choice)
        print("Testando....\n")


    if number_choice == numero:
        print("Parabéns! Você escolheu o número correto!\n")
        if choices == 1:
            print(f"Gênio ou sortudo? Você precisou de apenas {choices} tentativa para acertar o número!")
            break
        else:
            print(f"Você precisou de {choices} tentativas para acertar! Esperava mais, Eduardo....")
            break
       
    elif number_choice < numero:
        print("Tente um número mais alto!")
        continue
    else:
        print("Tente um número mais baixo!")


    
sfdvg