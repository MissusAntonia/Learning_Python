import re


def parse1():
    for line in open('log.text'):
        print('parse1',line.split('[')[1].split(']')[0])


def parse2():
    for line in open('log.text'):
        print('parse2',line.split()[3].strip('[]'))


def parse3():
    for line in open('log.text'):
        print('parse3',''.join(line.split('['or']')[3:5]))

def parse4():
    for line in open('log.text'):
        print('parse4',''.join(line.split()[3:5]).strip('[]'))
def parse5():
    for line in open('log.text'):
        print('parse5',re.split('\[|\]',line)[1])


parse1()
parse2()
parse3()
parse4()
parse5()
