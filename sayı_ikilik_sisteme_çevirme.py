decimal = int(raw_input("Number in decimal format: "))

def binary(n):
    output = ""
    while n > 0:
        output = "{}{}".format(n % 2, output)
        n = n // 2
    return output

# our method
print(binary(decimal))

# another way
print(bin(decimal)[2:])

# yet another way
print("{0:b}".format(decimal))
