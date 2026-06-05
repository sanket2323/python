def prime_number(x) -> bool:
    prime_or_not = False

    if x == 0 or x == 1:
        prime_or_not = True
        return prime_or_not

    else:
        for i in range(2, x):
            if x % i == 0:
                prime_or_not = False
                break
            else:
                prime_or_not = True

    return prime_or_not


print(prime_number(19))
