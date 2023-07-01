str_manip = input("Enter a sentance:")
print(str_manip)
print(len(str_manip))
str_last = str_manip[-1]
print(str_manip.replace(str_last ,"@"))
print(str_manip[::-1][:3])
str_first_3 = str_manip[0:3]
str_last_2 = str_manip[-2:]
spam = str_first_3 + str_last_2
print(spam)
print("\n".join(str_manip))