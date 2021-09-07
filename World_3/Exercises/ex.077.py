words = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Desenvolvedor')
for w in words:
    print(f'\nIn the word {w.upper()} have ', end='')
    for letter in w:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')