def get_number(prompt):
    while True:
        try:
            number = float(input(prompt)) 
            if number.is_integer():
                return int(number) 
        except ValueError:
            print("Это не число! Пожалуйста, введите число.") 
def get_operation():
    message = '''
Выберете математическую операцию:

+ : Сложение
- : Вычитание
/ : Деление
* : Умножение
Ваш выбор:
'''

    correct_operations = '+-/*' 
    operation = input(message)

    while operation not in correct_operations:
        print('Такая операция недоступна. Повторите попытку.')
        operation = input(message)
    return operation
def calculate(num1, num2, operation):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '/':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = "Деление на ноль запрещено"
    elif operation == '*':
        result = num1 * num2
    return result
def main():
    num1 = get_number("Введите первое число: ") 
    num2 = get_number("Введите второе число: ") 
    operation = get_operation() 
    result = calculate(num1, num2, operation) 
    print("Результат:", result) 


main()
while True:
    decision = (input('Продолжить? (да/нет) ')).lower()
    if decision == 'да':
        main()
    elif decision == 'нет':
        break

