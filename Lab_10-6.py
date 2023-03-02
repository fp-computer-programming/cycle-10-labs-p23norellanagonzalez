#author NDO 02/16/23 
# Write a function called add_nums that will do the try/except loop 
add_num = (5)
user_inp = (2,33,17)

# except statements 
try:
    number = int(input('enter a number'))
    print(add_num + user_inp)
except ValueError:
    print('Invalid Input')