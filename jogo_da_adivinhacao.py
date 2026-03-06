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
    
while True:
    number_choice = input("Digite um número que você julga estar correto: ")
    if number_choice.isdigit():
        number_choice = int(number_choice)
        print("Testando....\n")
    else:
        print("Número inválido, tente novamente!")
        continue
    if number_choice == numero:
        print("Parabéns! Você escolheu o número correto!")
        break
    else:
        print("Você errou! Tente novamente!")
        continue


    
