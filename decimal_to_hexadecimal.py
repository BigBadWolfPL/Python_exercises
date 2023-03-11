
def decimal_to_hex(number, remainder_list=None):
    if remainder_list == None:
        remainder_list = []

    while True:
        remainder = number % 16

        if remainder == 10:
            remainder_list.append("A")
        elif remainder == 11:
            remainder_list.append("B")
        elif remainder == 12:
            remainder_list.append("C")
        elif remainder == 13:
            remainder_list.append("D")
        elif remainder == 14:
            remainder_list.append("E")
        elif remainder == 15:
            remainder_list.append("F")
        else:
            remainder_list.append(str(remainder))

        quotient = int(number/16)
        number = quotient

        if quotient == 0:
            remainder_list.reverse()
            break
    return "".join(remainder_list)

print(decimal_to_hex(255))
print(decimal_to_hex(45891))
print(decimal_to_hex(63251))
print(decimal_to_hex(63425658))