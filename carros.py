medias_consumo = {
    'BMW': {'gasolina': 9.8, 'alcool': 8.9},
    'AUDI': {'gasolina': 12.8, 'alcool': 10.9},
    'FIAT': {'gasolina': 26.8, 'alcool': 24.9},
    'FERRARI': {'gasolina': 13.8, 'alcool': 12.9}
}

continuar = True

while continuar:
    carro = input('\nQual o tipo de carro? (BMW, AUDI, FIAT OU FERRARI): ').upper()
    combustivel = input('Qual o tipo de combustível? (gasolina ou álcool): ').lower()
    num_portas = int(input('Quantas portas o carro tem? '))
    num_pessoas = int(input('Quantas pessoas vão no carro? '))
    bagageiro = input('O carro tem bagageiro? (sim ou não): ').lower()

    media = medias_consumo[carro][combustivel]

    if num_portas > 4:
        media -= 0.5

    if num_pessoas > 2:
        media -= 1.2

    if bagageiro == "sim":
        media -= 0.2

    print("\nTipo de combustível:", combustivel)
    print("Modelo do carro:", carro)
    print("Bagageiro:", bagageiro)
    print("Passageiros:", num_pessoas)
    print("Portas: ", num_portas)

    print(f"\nValor total com Especificacoes: {media:.2f}")
    print(f"Valor sem especificacoes: {medias_consumo[carro][combustivel]}")

    resposta = input("\nDeseja testar outro carro? (sim ou não): ").lower()
    if resposta != "sim":
        continuar = False