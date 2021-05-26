teams = ('Conrinthians', 'Palmeiras', 'Santos', 'Gremio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atletico', 'Botafogo', 'Atletico-PR', 'Bahia',
         'Sao Paulo', 'Fluminense', 'Sport', 'Vitoria',
         'Coritiba', 'Avai', 'Ponte Petra', 'Atletico-GO')
print('+=' * 40)
print(f'Team list: {teams}')
#for t in teams:
#   print(t)
print('+=' * 40)
print(f'The 5 teams are {teams[0:5]}')
print('+=' * 40)
print(f'The last 4 teams are {teams[-4:]}')
print('+=' * 40)
print(f'Teams in Alphabetical order {sorted(teams)}')
print('+=' * 40)
print(f'The Chapecoense team is {teams.index("Chapecoense")+1} position!')
print('+=' * 40)
print('PROGRAM FINISHED')
