def lucky(ticket):

    if not ticket.isdigit():
        return False

    n = len(ticket)
    if n % 2 != 0:
        return False

    half = n // 2
    first_half = ticket[:half]
    second_half = ticket[half:]

    sum1 = sum(int(ch) for ch in first_half)
    sum2 = sum(int(ch) for ch in second_half)
    return sum1 == sum2

index = 0
while True:
    ticket = input().strip()
    index += 1
    if lucky(ticket):
        print(index)
        break