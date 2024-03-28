def calc(expression: str) -> int | float:
    allowed = '+-/*'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Выражение должно содержать хотя бы 1 знак из: {allowed}')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                return {
                    '+': lambda x, y: x + y,
                    '-': lambda x, y: x - y,
                    '*': lambda x, y: x * y,
                    '/': lambda x, y: x / y,
                }[sign](left, right)
                # if sign =='+':
                #     return left + right
                # elif sign =='-':
                #     return left - right
                # elif sign =='*':
                #     return left * right
                # elif sign =='/':
                #     return left / right
            except (ValueError, TypeError):
                raise ValueError(f'Выражение должн осодержать 2 целых числа и 1 знак')



if __name__ == '__main__':
    print(calc('2-2'))
