

# How to manipulate outputs printing strings and numbers

print(1, 'this is the first line')
print(2, 'this is the second line')
print(3, 'this is the third line')

# Types in Python -- Example using variables to manipulate data

name = str()  # Patrick, Joao, Bruno
age = int()  # 10, 20, 30
kilos = float()  # 8.4, 7.2, 12.9
is_male = bool()  # true or false
fav_movies = list()  # ['Batman', 'Interstellar', 'Fight Club']


# Inputs

#Example which user must interact and type values in the terminal, 
#then, this data will be registered in the variable

name = input('Qual seu nome: ')
surname = input('Qual seu sobrenome: ')
pref = input('Qual OS deseja utilizar: ')
developing = input('Prefere desenvolver em ambiente fechado ou aberto: ')

print(
    'Olá', name, surname, ',' 'bem vindo(a) a SkyNet, vejo que seu local de preferencia escolhido é',
    developing, ',' 'a nossa equipa ja esta configurando o seu', pref, 'e em breve todo ambiente estara pronto.'
)


# Slices in Python
# you can slice then using the index position value in [], so if I use job[0], the output is 'D'.

job = 'Developer'
print(job[0:3])


# Formatted strings in Python
# used to reduce complexity while writing texts, see example below using a pure string vs formatted string, check that results are equals.

name = 'Patrick'
surname = 'Pereira'
city = 'Sao Paulo'

# pure way - high complexity
pureText = 'O ' + name + ' ' + surname + ' mora em ' + '<' + city + '>'

# formatted way - low complexity - only uses f before stringing it.
formattedText = f'O {name} {surname} mora em <{city}>'

print(pureText)
print (formattedText)


# String methods in Python
# used to transform a string text into lowercase, uppercase, find a specific position, etc... I can just add . after var

methodText = 'I DEVELOP WEBSITES POWERED BY REACTJS'
print(methodText.lower())
print(methodText.lower().replace('reactjs', 'nextjs'))
print(methodText.split())
print(methodText.find('WEBSITES'))


# Math operations in Python

mathSum = 2 + 2
mathMinus = 10 - 2
mathDivided = 12 / 2
mathTimes = 4 * 8

print(mathSum)
print(mathMinus)
print(mathDivided)
print(mathTimes)


# Comparisson Operators in Python

# == equal
# != not equal
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

# outputs below must be True

ops1 = 10 == 10
ops2 = 'blue' != 'purple'
ops3 = 10 > 6
ops4 = 2 < 4
ops5 = 2 >= 1
ops6 = 1 <= 2

# outputs must be false

ops7 = 12 == 10
ops8 = 'yellow' != 'yellow'
ops9 = 2 > 4
ops10 = 4 < 2
ops11 = 8 >= 10
ops12 = 9 <= 3

true_ops_str = '\n'.join(str(op) for op in [ops1, ops2, ops3, ops4, ops5, ops6])
false_ops_str = '\n'.join(str(op) for op in [ops7, ops8, ops9, ops10, ops11, ops12])

print(true_ops_str)
print()
print(false_ops_str)



# Function example using < or > to print properly results

from datetime import datetime

def dynamic_greeting(name: str) -> None:
    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    print(f"{greeting}, {name}!")


dynamic_greeting("Patrick")