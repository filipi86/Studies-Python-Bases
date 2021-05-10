prod = float(input('Qual eh o preco do Produto? R$ '))
novo = prod - (prod * 5 / 100)
print('O produto que custava R$ {:.2f}, na promocao com desconto de 5%, vai custar R$ {:.2f}'.format(prod, novo))