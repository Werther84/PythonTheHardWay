__author__ = 'Slezak Attila'
# -- coding: utf-8 --

def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print("SUBSTRACTING %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

# A puzzle for the extra credit, type it anyway.
print("Here is puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

other_what = add(age, subtract(height, multiply(weight, divide(iq, subtract(age, iq)))))
print("That becomes: ", other_what, "Can you do it by hand?")

print(divide(add(24, 34), subtract(100, 1023)))