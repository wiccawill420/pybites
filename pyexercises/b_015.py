names = ['julian', 'bob', 'pybites']
countries = ['australia', 'spain', 'global']

for idx in range(0, len(names)):
    this_fill = ' ' * (11 - len(names[idx]))
    print(f"{idx + 1}. {names[idx]}{this_fill}{countries[idx]}")
