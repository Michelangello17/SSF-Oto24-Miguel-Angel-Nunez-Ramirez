import math as mt 
#Tarea 1 Miguel Angel Nuñez ramirez

#Variantes dadas Bendersky's website ejemplo de ecuacion 6x^3+4x^2+7x-19 con x=3 

# #naive method
def poly_naive(A, x):
    p = 0
    for i, a in enumerate(A):
        p += (x ** i) * a
    return p
print(poly_naive((6,4,7,-19),3))

#Horner's rule
def poly_horner(A, x):
    p = A[-1]
    i = len(A) - 2
    while i >= 0:
        p = p * x + A[i]
        i -= 1
    return p
print(poly_horner((6,4,7,-19),3))

#Iterative method
def poly_iter(A, x):
    p = 0
    xn = 1
    for a in A:
        p += xn * a
        xn *= x
    return p
print(poly_iter((6,4,7,-19),3))

#Horner's rule mostrado en clase 
def horner(coeffs,x):
    acc=0
    for c in reversed(coeffs):
        acc=acc*x+c
    return acc 
print(horner((6,4,7,-19),3))
#En todos los casos nos da -432 

#Funcion coseno para x pequeña 
print(mt.cos(30))
def coseno (x,n):
    sum=0.0
    for g in range(n-1):
        sum=sum+((-1)**g)*((x**g)/(mt.factorial(2*g)))      
    return sum
print(coseno(5,10))
print(((coseno(5,10**8))-mt.cos(30))/mt.cos(30))

#   X   Iteraciones             Suma            Error_relativo
#   1       10^4         0.5403023058681398            0
#   1       10^8         0.5403023058681398            0
#   30      10^4         0.6952656718281731     3.4888985620451094
#   30      10^8         0.6952656718281731     3.4888985620451094
