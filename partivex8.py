

def isprime(y):
    x = y // 2 # For some y > 1
    while x > 1:
        if y % x == 0: # Remainder
             print(y, 'has factor', x)
             break # Skip else
        x-=1
    else: # Normal exit
        if y <= 1:
            print(y,'is Not valid')
        else:
            print(y, 'is prime')



def primes(y):
    x = y // 2
    for i in range(y,1,-1):
        if y % x == 0: # Remainder
             print(y, 'has factor', x)
             break
    else: # Normal exit
        if y <= 1:
            print(y,'is Not valid')
        else:
            print(y, 'is prime')




(isprime(10),primes(10) )
(isprime(13),primes(13) )
(isprime(15),primes(13) )
(isprime(0),primes(0)   )
(isprime(1),primes(1)   )
(isprime(-7),primes(-7) )
(isprime(-4),primes(-4) )
