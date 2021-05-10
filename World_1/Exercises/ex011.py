larg = float(input('Qual a largura da sua parede: '))
alt = float(input('Qual a largura da sua parede: '))
area = larg * alt
print('Sua parede tem {} x {} e sua area eh de {} m2'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, voce vai precisar de {}l de tinta'.format(tinta))