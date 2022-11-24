while True:
    reply = input('Enter text:')
    if reply == 'stop':break
    elif not reply.isdigit():
        print('Check!input')
    else:print(int(reply) ** 2)
print('Bye')
