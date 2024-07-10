# Python3 code to demonstrate working of
# Converting binary to string
# Using BinarytoDecimal(binary)+chr()


# Defining BinarytoDecimal() function
def binary_to_decimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


# Driver's code
# initializing binary data
bin_data = '0100011101100101011001010110101101110011'

# print binary data
print("The binary value is:", bin_data)

# initializing a empty string for
# storing the string data
str_data = ' '

# slicing the input and converting it
# in decimal and then converting it in string
for i in range(0, len(bin_data), 7):
    # slicing the bin_data from index range [0, 6]
    # and storing it as integer in temp_data
    temp_data = int(bin_data[i:i + 7])

    # passing temp_data in BinarytoDecimal() function
    # to get decimal value of corresponding temp_data
    decimal_data = binary_to_decimal(temp_data)

    # Decoding the decimal value returned by
    # BinarytoDecimal() function, using chr()
    # function which return the string corresponding
    # character for given ASCII value, and store it
    # in str_data
    str_data = str_data + chr(decimal_data)

# printing the result
print("The Binary value after string conversion is:", str_data)


def binary_to_text(binary_string):
    # Convierte cada bloque de 8 caracteres (un byte) en un entero y luego en un carácter
    return ''.join(chr(int(binary_string[i * 8:i * 8 + 8], 2)) for i in range(len(binary_string) // 8))


print(f'Binary to string {binary_to_text('0100011101100101011001010110101101110011')}')
