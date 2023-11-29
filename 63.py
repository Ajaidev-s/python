def factorial(n):
    assert(n>=0),"negative number"
    f=1
    for i in range (1,n+1):
        f*=i
    print("factorial =",f)
try:
    factorial(-5)
except AssertionError as ae:
    print(ae)
