slovar = {
    'owez':'django',
    'suleyman':'python',
    'akynyaz':'js',
    'mekan':'php',
    'selim':'html'
}

new = []

search = input('Write person\'s name: \n\t\t ')

for i in slovar.keys():
    new.append(i)

if search in new:
    print(slovar[search])
else:
    print('User not found !')
