age = 32
txt = f"my sisters age is {age} "
print(txt)
'''
syntax :
for f-files
x = ___
y =f"______{x}"
print(y)
//where f functions are placeholders and can also be modifiers when
included a colon (:)
syntax:
x = _____
y = f"_____{x:.__}"
print(y)


we can also perform operations using strings such as 
example1
'''
x = 50
y = f"the rate of the product is{x:3d} rupees"
print(y)
#example1
txt = f"my age is {9*2}"
print(txt)
x = 10
y =20
txt = f"the total sum will be {x+(x*y)}"
print(txt)
#we can also give if else statements in f-functions:
x = 20
y = 15
txt = f"the given no.{'x is greater'if x>y else x is smaller}"
print(txt)
#so now
'''
x = int(input("Enter a no."))
y = int(input("Enter a no."))
txt = f"The greatest no. of two is {'x' if x>y else y}"
print(txt)

we can also use the f-functions in the string methods like upper ,lower and etc.,

animal = input("Enter an animal name")
txt = f"Nandini is {animal.upper()}"
print(txt)

def multiplier(x,y):
    return x*y
x = int(input("Enter a no."))
y = int(input("Enter a no."))
txt = f"The multiplication of two numbers will be {multiplier(x,y)}"
print(txt)
'''
x = 2000
txt = f"The price of this paper is {x:,} ruppes"
print(txt)








