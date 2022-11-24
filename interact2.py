while True:
    reply = input('Enter text:')
    if reply == 'stop': break
    try:
        print(eval(reply) ** 2)
    except:
        print('Bad!' * 8)
print('Bye')
print('='* 100)
print('ANOTHER PROGRAM ONLY  >20')
print('='* 100)



while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        num = int(reply)
        if num < 20:
            print('low')
        else:
            print(num ** 2)
print('Bye')
