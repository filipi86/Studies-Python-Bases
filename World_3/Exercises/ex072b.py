sequence = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
            'sete', 'oito',
            'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input("digite um número:"))
    if num < 0 or num > 20:
        print("Tente novamente, N: [0/20]")
        continue
    if 0 <= num <= 20:
        print(f"Você digitou o número: {sequence[num]}")
        continuar = str(input("Você quer continuar?")).strip().lower()[0]
        if continuar in 'Ss':
            continue
        if continuar in 'Nn':
            print("O program foi encerrado!")
            break