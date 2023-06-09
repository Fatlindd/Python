# dec -> bin 
def dec_to_binary(num):
    bits = []
    while num > 0:
        bits.append(num % 2)
        num = num // 2
    bits.reverse()

    binary = ''
    for bit in bits:
        binary += str(bit)
    return binary

number = int(input('▶ Your decimal number: '))
print('Your binary is: ', dec_to_binary(number))