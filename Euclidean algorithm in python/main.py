# Python program to demonstrate Basic Euclidean Algorithm
# Function to return gcd of a and b
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)
a = 10
b = 15
print("gcd(", a, ",", b, ") = ", gcd(a, b))
a = 35
b = 10
print("gcd(", a, ",", b, ") = ", gcd(a, b))
a = 31
b = 2
print("gcd(", a, ",", b, ") = ", gcd(a, b))
print('---'*100)
a = int(input("įveskite 1-ą naturalųjį skaičių: "))
b = int(input("įveskite 2-ą naturalųjį skaičių: "))
sa = a;
sb = b
while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print("Didžiausias bendras dalyklis-DBD(%d, %d) = %d" % (sa, sb, a))

#output
gcd( 10 , 15 ) =  5
gcd( 35 , 10 ) =  5
gcd( 31 , 2 ) =  1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
įveskite 1-ą naturalųjį skaičių: 10
įveskite 2-ą naturalųjį skaičių: 15
Didžiausias bendras dalyklis-DBD(10, 15) = 5

Process finished with exit code 0
