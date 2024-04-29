# String Data Types

# literal assignment
first = " Seyi "
last = "Makanjuola"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

#constructor function
# yam = str("egg")
# print(type(yam))
# print(type(yam) == str)
# print(isinstance(yam, str))

#concatenation
fullname = first + "" + last 
print(fullname)
fullname += " is a boy"
print(fullname)

#casting a number to a string
decade = str(1990)
print(type(decade))
print(decade)

statement = 'I\'m in love rap music from the ' + decade +"s."
print(statement)

#Multiple lines. here three quotation marks will be used
multiline = """
Guess who's back baby?

your mum!!!

                    all good?
"""
print(multiline)

#string method 
print(first.lower())
print(first.upper())