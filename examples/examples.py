###############################################################################################################

# How to manipulate outputs printing strings and numbers

def print_example():
    print(1, 'this is the first line')
    print(2, 'this is the second line')
    print(3, 'this is the third line')


###############################################################################################################

# Inputs
# Example which user must interact and type values in the terminal,
# then, this data will be registered in the variable

def inputs_example():
    name = input('Qual seu nome: ')
    surname = input('Qual seu sobrenome: ')
    pref = input('Qual OS deseja utilizar: ')
    developing = input('Prefere desenvolver em ambiente fechado ou aberto: ')

    text = (f"Olá {name} {surname}, bem vindo(a) a SkyNet. "
            f"Vejo que seu local de preferencia escolhido é {developing}, "
            f"a nossa equipa ja esta configurando o seu {pref} "
            f"e em breve todo ambiente estara pronto.")

    print(text)


###############################################################################################################

# Formatted strings in Python
# used to reduce complexity while writing texts, see example below using a pure string vs formatted string, check that results are equals.

def formatted_strings(name: str, surname: str, city: str):

    pureText = 'O ' + name + ' ' + surname + ' mora em ' + '<' + city + '>'

    formattedText = f'O {name} {surname} mora em <{city}>'

    print(pureText)
    print(formattedText)


###############################################################################################################

# String methods in Python
# used to transform a string text into lowercase, uppercase, find a specific position, etc... I can just add . after var

def string_methods_example():

    methodText = 'I DEVELOP WEBSITES POWERED BY REACTJS'
    print(methodText.upper())
    print(methodText.lower())
    print(methodText.lower().replace('reactjs', 'nextjs'))
    print(methodText.split())
    print(methodText.find('WEBSITES'))


###############################################################################################################

# Math operations in Python

def math_operations_example():
    mathSum = 2 + 2
    mathMinus = 10 - 2
    mathDivided = 12 / 2
    mathTimes = 4 * 8

    print(mathSum)
    print(mathMinus)
    print(mathDivided)
    print(mathTimes)


###############################################################################################################

# Comparisson Operators in Python

def comparisson_true_operators_example():

    # outputs below must be True

    ops1 = 10 == 10
    ops2 = 'blue' != 'purple'
    ops3 = 10 > 6
    ops4 = 2 < 4
    ops5 = 2 >= 1
    ops6 = 1 <= 2

    true_ops_str = '\n'.join(str(op)
                             for op in [ops1, ops2, ops3, ops4, ops5, ops6])

    print(true_ops_str)


###############################################################################################################

def comparisson_false_operators_example():

    # outputs must be false

    ops7 = 12 == 10
    ops8 = 'yellow' != 'yellow'
    ops9 = 2 > 4
    ops10 = 4 < 2
    ops11 = 8 >= 10
    ops12 = 9 <= 3

    false_ops_str = '\n'.join(str(op)
                              for op in [ops7, ops8, ops9, ops10, ops11, ops12])

    print(false_ops_str)


###############################################################################################################


# Conditional Statements

def conditional_example(speed: int):

    if speed > 100:
        print('Velocidade acima do permitido')
        print('reduza a velocidade')
    elif speed < 40:
        print('Velocidade minima atingida')
        print('Aumente a velocidade')
    else:
        print('Velocidade apropriada para rodovia')


###############################################################################################################


# Logical Operators


def logical_operators_example(salary: int, clean_name: bool, has_property: bool):

    if salary > 5000 and clean_name == True and has_property == True:
        print('Financiamento aprovado')
    elif salary > 3000 and clean_name == True and has_property == True:
        print('Financiamento pendente, avaliacao salarial')
    else:
        print('Financiamento negado')


###############################################################################################################


# Multiple Comparison Operators

def multiple_logical_operators(value: int):

    if value >= 1 and value < 10:
        print('Produto dentro do range aceito')
    else:
        print('Produto fora do range e nao aceito')


###############################################################################################################


# For Loop (Numbers)


def for_loop_numbers():

    for num in range(1, 11):
        print(num)


###############################################################################################################


# For Loop (Strings)


def for_loop_strings(word: str):

    for string in word:
        print(f'{string} esta dentro da palavra {word}')
