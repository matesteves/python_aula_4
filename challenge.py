
def pedir_nome() -> str:
    nome_valido: bool = False
    while not nome_valido:
        try:
            nome: str = input("Digite seu nome: ")
            if len(nome) == 0:
                raise ValueError("O nome não pode estar vazio.")
            elif any(char.isdigit() for char in nome):
                raise ValueError("O nome não deve conter números.")
            else:
                print("Nome válido:", nome)
                nome_valido = True
        except ValueError as e:
            print(e)
    return nome

def pedir_salario() -> float:
    salario_valido: bool = False
    while not salario_valido:
        try:
            salario:float = float(input("Digite o valor do seu salário: "))
            if salario < 0:
                print("Por favor, digite um valor positivo para o salário.")
            else:
                print("Salário válido: ", salario)
                salario_valido = True
        except ValueError:
            print("Entrada inválida para o salário. Por favor, digite um número.")
    return salario


def pedir_bonus() -> float:
    bonus_valido: bool = False
    while not bonus_valido:
        try:
            bonus: float = float(input("Digite o valor do bônus recebido: "))
            if bonus < 0:
                print("Por favor, digite um valor positivo para o bônus.")
            else:
                print("Bônus válido: ", bonus)
                bonus_valido = True
        except ValueError:
            print("Entrada inválida para o bônus. Por favor, digite um número.")
    return bonus

def calcular_bonus(nome: str, salario: float, bonus: float) -> None:
    bonus_recebido: float = 1000 + salario * bonus

    return print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")

def main():
    nome = pedir_nome()
    salario = pedir_salario()
    bonus = pedir_bonus()
    calcular_bonus(nome, salario, bonus)

main()