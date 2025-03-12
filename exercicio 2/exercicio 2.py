
def soma_digitos(numero):
    # Inicializa a soma dos dígitos
    soma = 0
    while numero != 0:
        soma += numero % 10  # Pega o último dígito
        numero //= 10  # Remove o último dígito
    return soma

def main():
    # Recebe a entrada do usuário
    entrada = input("Informe um número inteiro: ")
    
    # Verifica se a entrada é um número inteiro
    if entrada.isdigit() or (entrada[0] == '-' and entrada[1:].isdigit()):
        numero = int(entrada)  # Converte a entrada para inteiro
        print(f"A soma dos dígitos é: {soma_digitos(abs(numero))}")  # Usa abs() para lidar com números negativos
    else:
        print("Valor inválido. Informe um número inteiro.")

# Chama a função principal
if __name__ == "__main__":
    main()