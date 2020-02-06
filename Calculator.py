import Operators as op

print('Hello, welcome to the calculator.')

while True:
    fun = input('Would you like to add, subtract, multiply or divide?').strip().lower()
    if fun == 'break':
        break
    input1 = input('Please give me a number. If done type DONE').strip().lower()
    list = []
    istrue = True
    while istrue == True:
        input1 = input('Please give me a number. If done type DONE').strip().lower()
        if input1.isnumeric() == True:
            input1 = int(input1)
            list.append(input1)
        elif input1 == 'break':
            break
        elif input1.isnumeric() == False:
            if input1 == 'done':
                if fun == 'multiply':
                    calc = op.multiply(list)
                    print(calc)
                    istrue = False
                elif fun == 'divide':
                    calc = op.divide(list)
                    print(calc)
                    istrue = False
                elif fun == 'add':
                    calc = op.add(list)
                    print(calc)
                    istrue = False
                elif fun == 'subtract':
                    calc = op.subtract(list)
                    print(calc)
                    istrue = False
                else:
                    print('Please give a valid operation')
                    istrue = False
            else:
                print('Invalid input')

