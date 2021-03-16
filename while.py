print('Python While operation system...')

'''
while Don't stop !!!
'''

# c = 0
# i = 1
# while i < 10:
#     c = c + 1
#     print('While count is : ' + str(c))

#
# i = 0
# while i <= 10:
#     print('i => ' + str(i))
#     i += 1

password = str(input('Password: '))

print('Please enter your password to login !')
while True:
    password2 = str(input('Confirm password: '))
    if password != password2:
        print('Try again !')
    else:
        print('Welcome to our site !')
        break
