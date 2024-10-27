def pedir_nome() -> list:
    nomes: list = []
    continuar: str = 's'
    while continuar.lower() == 's':
        try:
            nome: str = input('Qual seu nome? ')
            if any(char.isdigit() for char in nome):
                raise ValueError("O nome não pode conter números")
            elif len(nome.split()) == 0:
                print("O nome não pode estar em branco")
            else:
                nomes.append(nome)
                continuar = input("Deseja adicionar mais pessoas? (S ou N) ")
        except ValueError as error:
            print(error)
    return nomes

def pedir_salario() -> list:
    salarios: list = []
    continuar: str = 's'
    while continuar.lower() == 's':
        try:
            salario: float = float(input('Qual o seu salário? '))
            if salario < 0:
                print("Seu salário não pode ser negativo. Tente novamente.")
            else:
                salarios.append(salario)
                continuar = input("Deseja adicionar mais pessoas? (S ou N) ")
        except ValueError as error:
            print(error)
    return salarios

def pedir_bonus() -> list:
    bonuses: list = []
    continuar: str = 's'
    while continuar.lower() == 's':
        try:
            bonus: float = float(input('Qual a % do seu bônus? '))
            if bonus < 0:
                print("Seu bônus não pode ser negativo. Tente novamente.")
            else:
                bonuses.append(bonus)
                continuar = input("Deseja adicionar mais pessoas? (S ou N) ")
        except ValueError as error:
            print(error)
    return bonuses

def calcular_bonus(salario, bonus) -> list:
    bonus_final: list = []
    for i in range(len(salario)):
        bonus_final.append(1000 + (salario[i] * bonus[i])/100)
    return bonus_final


def main():
    nome: list = pedir_nome()
    salario: list = pedir_salario()
    bonus: list = pedir_bonus()
    bonus_final: list = calcular_bonus(salario, bonus)

    info_geral: list = []
    for i in range(len(nome)):
        dict_apoio: dict = {}

        dict_apoio["nome"] = nome[i]
        dict_apoio["salario"] = salario[i]
        dict_apoio["bonus"] = bonus[i]
        dict_apoio["bonus_final"] = bonus_final[i]

        info_geral.append(dict_apoio)

        print(info_geral)

main()