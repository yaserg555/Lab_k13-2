print("Ільницький")
def convert(binary_value, system):
    letters = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    a = [0, 0, 0, 0, 0, 0, 0, 0]
    end = len(binary_value)
    for i in range(end-1, -1, -1):
        a[i] = letters[binary_value[i]]
    default = 1;
    result = 0;
    for i in range(end-1, -1, -1):
        result += default * a[i]
        default *= system
    return result

print("Math operations")
print("/////////////")
print("8 / 3 =" + str(8 / 3) + " " + str(type(8 / 3)), "8 // 3 = " + str(8 // 3) + " " + str(type(8 // 3)),
"8 % 3 = " + str(8 % 3) + " " + str(type(8 % 3)), "8**3 = " + str(8**3) + " " + str(type(8**3)))
print()
print("8.6 / 3 = " + str(8.6 / 3) + " " + str(type(8.6 % 3)), "8.6 // 3 = " + str(8.6 // 3) + " " + str(type(8.6 % 3)),
"8.6 % 3 = " + str(8.6 % 3) + " " + str(type(8.6 % 3)), "8.6**3 = " + str(8.6**3) + " " + str(type(8.6 % 3)))
print()
print("-8 / 3 = " + str(-8 / 3) + " " + str(type(-8 % 3)), "-8 // 3 = " + str(-8 // 3) + " " + str(type(-8 % 3)),
"-8 % 3 = " + str(-8 % 3) + " " + str(type(-8 % 3)), "-8**3 = " + str(-8**3) + " " + str(type(-8 % 3)))
print("//////////////")

print(convert("1011", 2))
print(convert("11111111", 2))

print(convert("1101", 8))

print(convert("AF", 16))
