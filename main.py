
from examples.examples import (
    print_example, 
    inputs_example, 
    formatted_strings, 
    string_methods_example, 
    math_operations_example, 
    comparisson_true_operators_example,
    comparisson_false_operators_example
)

from functions.greeting import (
    dynamic_greeting
)

def Principal():
    #print_example()
    #inputs_example()
    #formatted_strings(name='Patrick', surname='Pereira', city='SP')
    #string_methods_example()
    #math_operations_example()
    #comparisson_true_operators_example()
    #comparisson_false_operators_example()
    dynamic_greeting(name='Patrick')

Principal()