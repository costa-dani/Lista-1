r = input("Voce eh homem ou mulher: ")

h = float(input("Qual eh sua altura em metro: "))

if r == 'h':

    pi = (72.7*h)-58
    print(f"Seu peso ideal eh {pi:.2f}kg")

elif r == 'm':
    pi = (62.1*h)-44.7
    print(f"Seu peso ideal eh {pi:.2f}kg")