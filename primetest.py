''' Check if a number is prime
    number must be below 10 '''

y=input('Enter Number:')
y=int(y)
x = y // 2 # For some y > 1
while x > 1:
    if y % x == 0: # Remainder
        print(y, 'has factor', x)
        break # Skip else
    x -= 1
else: # Normal exit
    print(y, 'is prime')
