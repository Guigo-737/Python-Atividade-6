 def calcular_media_variacao(temp_max, temp_min):
    # Calcula a média entre a temperatura máxima e mínima
    media = (temp_max + temp_min) / 2
    # Calcula a variação entre as temperaturas
    variacao = temp_max - temp_min
    return media, variacao

def soma_digitos(numero):
    # Verifica se o número é inteiro
    if not isinstance(numero, int):
        return "Valor inválido. Informe um número inteiro."
    
    soma = 0
    while numero != 0:
        soma += numero % 10
        numero //= 10
    return soma

def main():
    try:
        # Recebe as temperaturas como input do usuário
        temp_max = float(input("Informe a temperatura máxima do dia: "))
        temp_min = float(input("Informe a temperatura mínima do dia: "))
        
        # Calcula a média e variação
        media, variacao = calcular_media_variacao(temp_max, temp_min)
        
        print(f"\nA média entre a temperatura máxima e mínima é: {media:.2f}")
        print(f"A variação entre as temperaturas é: {variacao:.2f}")
        
        # Recebe o número para somar os dígitos
        numero = input("\nInforme um número para somar seus dígitos: ")
        
        # Verifica se o número informado é inteiro
        if numero.isdigit():
            numero = int(numero)
            print(f"A soma dos dígitos é: {soma_digitos(numero)}")
        else:
            print("Valor inválido. Informe um número inteiro.")
    
    except ValueError:
        print("Valor inválido. Informe um número decimal para a temperatura.")

# Chama a função principal
if __name__ == "__main__":
    main()