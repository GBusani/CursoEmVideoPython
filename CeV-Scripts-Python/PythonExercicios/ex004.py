a = input('\033[1;37;41mDigite algo:\033[m ')

print('\033[7;30;47mO tipo primitivo desse valor é',type(a),'\033[m')
print('\033[7;30;47mSó tem espaços?',a.isspace(),'\033[m')
print('\033[7;30;47mÉ um número?',a.isnumeric(),'\033[m')
print('\033[7;30;47mÉ alfabético?',a.isalpha(),'\033[m')
print('\033[7;30;47mÉ alfanumérico?',a.isalnum(),'\033[m')
print('\033[7;30;47mEstá em maiúsculas?',a.isupper(),'\033[m')
print('\033[7;30;47mEstá em minúsculas?',a.islower(),'\033[m')
print('\033[7;30;47mEstá capitalizada?',a.istitle(),'\033[m')
