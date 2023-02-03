num1 = 1122334455666

num1_str = str(num1)
print(len(num1_str))
print(num1_str[3])
print(num1_str[2:5:1])
#i dont know what num2 and num3 means
string_with_0 = str(0)+num1_str
print(string_with_0[0:4])
print(string_with_0[4:len(string_with_0)])
print(string_with_0[-7:-4])