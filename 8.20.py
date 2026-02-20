def number_to_russian(n):
    if n == 0:
        return "ноль"

    ones = ["", "один", "два", "три", "четыре", "пять",
            "шесть", "семь", "восемь", "девять"]
    ones_fem = ["", "одна", "две", "три", "четыре", "пять",
                "шесть", "семь", "восемь", "девять"]
    tens = ["", "десять", "двадцать", "тридцать", "сорок",
            "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать",
             "четырнадцать", "пятнадцать", "шестнадцать",
             "семнадцать", "восемнадцать", "девятнадцать"]
    hundreds = ["", "сто", "двести", "триста", "четыреста",
                "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    def convert_hundreds(num, gender='m'):
        if num == 0:
            return ""

        result = []
        h = num // 100
        t = (num % 100) // 10
        o = num % 10

        if h > 0:
            result.append(hundreds[h])
        if t == 1:
            result.append(teens[o])
        else:
            if t > 0:
                result.append(tens[t])
            if o > 0:
                if gender == 'f':
                    result.append(ones_fem[o])
                else:
                    result.append(ones[o])

        return " ".join(result)

    result = []

    millions = n // 1000000
    if millions > 0:
        result.append(convert_hundreds(millions, 'm') + " миллион" +
                      get_million_ending(millions))

    thousands = (n % 1000000) // 1000
    if thousands > 0:
        result.append(convert_hundreds(thousands, 'f') + " тысяча" +
                      get_thousand_ending(thousands))

    remainder = n % 1000
    if remainder > 0:
        result.append(convert_hundreds(remainder, 'm'))

    return " ".join(result).strip()


def get_thousand_ending(n):
    n %= 100
    if 11 <= n <= 19:
        return "ч"
    n %= 10
    if n == 1:
        return "а"
    elif 2 <= n <= 4:
        return "и"
    else:
        return "ч"


def get_million_ending(n):
    n %= 100
    if 11 <= n <= 19:
        return "ов"
    n %= 10
    if n == 1:
        return ""
    elif 2 <= n <= 4:
        return "а"
    else:
        return "ов"

n = int(input("Введите число до 900000000: "))
if 0 <= n <= 900000000:
    print(number_to_russian(n))
else:
    print("Число должно быть от 0 до 900000000")