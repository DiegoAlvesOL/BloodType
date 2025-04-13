# Name: Diego Alves de Oliveira
# Student ID: 78952
# Email: 78952@student.dorset-college.ie
import time

# Lista contendo os tipos sanguíneos válidos utilizados para validação de entrada.
valid_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

# As listas abaixo representam, para cada tipo sanguíneo, os tipos que são compatíveis como doadores.
receiver_Aplus = ["A+", "A-", "O+", "O-"]
receiver_Aminus = ["A-", "O-"]
receiver_Bplus = ["B+", "B-", "O+", "O-"]
receiver_Bminus = ["B-", "O-"]
receiver_ABplus = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
receiver_ABminus = ["A-", "B-", "AB-", "O-"]
receiver_Oplus = ["O+", "O-"]
receiver_Ominus = ["O-"]

# As listas a seguir mostra os tipos sanguíneos e quais tipos podem receber transfusão dos mesmos.
donors_Aplus = ["A+", "AB+"]
donors_Aminus = ["A+", "A-", "AB+", "AB-"]
donors_Bplus = ["B+", "AB+"]
donors_Bminus = ["B+", "B-", "AB+", ]
donors_ABplus = ["AB+"]
donors_ABminus = ["AB+", "AB-"]
donors_Oplus = ["O+", "A+", "B+", "AB+"]
donors_Ominus = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

# Essa função valida se o usuário digitou um tipo sanguíneo correto,
# comparando-o com a lista de tipos sanguíneos permitidos.
def valid_blood_type(blood_user):
    if blood_user in valid_types:
        return True
    else:
        return False

#  Esta função recebe como parâmetro o tipo sanguíneo informado pelo usuário e verifica se o tipo de sangue que ele informou está na lista, seguindo as regras de compatibilidade da função.
#  Estou usando o "in" ao invés de "==" porque o "in" vai percorrer dentro da lista e caso encontre um valor compativel com que o usuário digitou valida a lista.
#  No caso do "==" iria comparar o valor que o usuário digitou e comparar com toda a lista, e isso daria erro, porque o usuário vai digitar apenas um tipo sanguíneo por vez.
def get_donation (blood_user):
    if blood_user == "A+":
        return receiver_Aplus
    elif blood_user == "A-":
        return receiver_Aminus
    elif blood_user == "B+":
        return receiver_Bplus
    elif blood_user == "B-":
        return receiver_Bminus
    elif blood_user == "AB+":
        return receiver_ABplus
    elif blood_user == "AB-":
        return receiver_ABminus
    elif blood_user == "O+":
        return receiver_Oplus
    elif blood_user == "O-":
        return receiver_Ominus

# Esta função recebe como parâmetro o tipo sanguíneo informado pelo usuário
# e retorna a lista de tipos sanguíneos que podem receber doação deste tipo.
def receives_donation (blood_user):
    if blood_user == "A+":
        return donors_Aplus
    elif blood_user == "A-":
        return donors_Aminus
    elif blood_user == "B+":
        return donors_Bplus
    elif blood_user == "B-":
        return donors_Bminus
    elif blood_user == "AB+":
        return donors_ABplus
    elif blood_user == "AB-":
        return donors_ABminus
    elif blood_user == "O+":
        return donors_Oplus
    elif blood_user == "O-":
        return donors_Ominus

# Mensagem de boas vindas.
print("+","-"*50 ,"+")
print("|  Welcome to the Blood Type Compatibility Checker!  |")
print("+","-"*50,"+")

# Estrutura principal de repetição do programa.
# Exibe o menu de opções e permanece em execução até que o usuário opte por sair.
while True:
    print("+","-"*50,"+")
    print("| Choose an option: "," "*31, "|")
    print("| 1. Check what type of blood you can recive."," "*6, "|")
    print("| 2. Check which blood type you can donate to."," "*5, "|")
    print("| 3. Exit the program."," "*29, "|")
    print("+","-"*50,"+")
    print(" ")

    # Captura a escolha do usuário e aplica .strip() para remover espaços extras no início ou fim da entrada.
    choice = input("Enter your choice 1,2 or 3: ").strip()
    if choice == "3":
        print("Thank you for using the Blood Type Compatibility Checker. Goodbye!")
        break

    # Caso o usuário digite 1 ele cairá nessa estrutura que irá solicitar ao mesmo que digite o seu tipo sanguíneo.
    # O input é tratado com .upper(), .strip() e .replace() para garantir que:
    # - todas as letras estejam em maiúsculo
    # - espaços no início, meio e fim sejam removidos
    elif choice == "1":
        blood_user = input("Please, enter with your blood type: ").upper().strip().replace(" ", "")
        if not valid_blood_type(blood_user):
            print("O tipo sanguíneo que você digitou está incorreto.")
        else:
            donors = get_donation(blood_user)
            print("Please wait a moment while we process your information")
            for i in range(5,-1,-1):
                print(i)
                time.sleep(0.5)
            print("-"*103)
            print(" Your blood type is {}, you can receive blood from: {}".format(blood_user, donors))
            print("-"*103)
            print(" ")

    # Caso o usuário escolha a opção 2, o mesmo processo de entrada e validação é realizado.
    elif choice == "2":
        blood_user = input("Please, enter with your blood type: ").upper().strip().replace(" ", "")
        if not valid_blood_type(blood_user):
            print("O tipo sanguíneo que você digitou está incorreto.")
        else:
            receiver = receives_donation(blood_user)
            for j in range(5,-1,-1):
                print(j)
                time.sleep(0.5)
            print("-"*102)
            print("Your blood type is {}, and you can donate blood to: {}".format(blood_user,receiver))
            print("-"*102)
            print(" ")

    # Caso o usuário digite uma opção inválida (diferente de 1, 2 ou 3), será exibida uma mensagem de erro.
    else:
        print("Opção invalida! Por favor escolha uma das opções informada no menu")
        print(" ")