favLanguages = {
    'sarah': 'python',
    'rekha': 'scala',
    'sreeja': 'c'
}

for name, language in favLanguages.items():
    print(f'{name.title()}\'s fav language is {language.title()}')

print('...')

for name in favLanguages.keys():
    print(name.title())

print('...')

for language in favLanguages.values():
    print(language.title())