from add import add
from multiply import multiply
from subtract import subtract
from divide import divide
from power import power
from root import root

symbols  = {
        '+':add,
        '-':subtract,
        '*': multiply,
        '/': divide,
        '**': power,
        '^': root
        }


class Calculator:

    @staticmethod
    def calculate(equation: str) -> float:
        '''Enter the equation you want separated by space.
        Ex: 3 + 4
        '''

        if not ' ' in equation:
            return "You must enter the equation you want separated by space (Ex: 1 + 3)" 

        x = float(int(equation.split(' ')[0]))
        y = float(int(equation.split(' ')[2]))
        calculation_symbol = equation.split(' ')[1]


        if calculation_symbol in symbols.keys():
            function = symbols[calculation_symbol]
            return function(x, y)
        else:
            return "Sorry we currentluy do not allow this feture!"
        
        

if __name__ == '__main__':
    c = Calculator()
    print(f"Use symbols: {[ [k, v.__name__] for k, v in symbols.items() ]}")
    while True:
        equation = input("Please enter an equation (Ex: 1 + 2): ")
        print(f'Result: {c.calculate(equation)}')



        
  