def calculate(expression):
    expression = expression.replace(' ', '')
    pos = [0]

    def parse_value():
        nonlocal pos
        i = pos[0]
        if expression[i] == '(':
            pos[0] += 1
            val = parse_expression()
            pos[0] += 1
            return val
        else:
            return parse_number()

    def parse_number():
        nonlocal pos
        i = pos[0]
        if expression[i] == '-':
            i += 1
            sign = -1
        else:
            sign = 1
        num = 0
        while i < len(expression) and expression[i].isdigit():
            num = num * 10 + int(expression[i])
            i += 1
        pos[0] = i
        return sign * num

    def parse_term():
        nonlocal pos
        val = parse_value()
        while pos[0] < len(expression) and expression[pos[0]] in '*/':
            op = expression[pos[0]]
            pos[0] += 1
            right = parse_value()
            if op == '*':
                val *= right
            else:
                val //= right
        return val

    def parse_expression():
        nonlocal pos
        val = parse_term()
        while pos[0] < len(expression) and expression[pos[0]] in '+-':
            op = expression[pos[0]]
            pos[0] += 1
            right = parse_term()
            if op == '+':
                val += right
            else:
                val -= right
        return val

    return parse_expression()

expr = input("Введите выражение: ")
print(calculate(expr))