# print('Üdv \na \nfedélzeten', end='')
"""print('\nSzia', 'Jenő',sep='-----')

print('''Ez
több
sorba
kerül
''')
"""

# nev = input('Hogy hívnak: ')
nev = 'valaki'
titulus = 'dr.'
print('Szia', nev)
print(f'Szia {nev}')
print('Helló {0} {1}'.format(titulus, nev))

print('jobbra'.rjust(50, '-'))
print('balra'.ljust(50,'-'))
print('közép'.center(50))
