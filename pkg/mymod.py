def countLines(f):
    fh=open(f)
    return len(fh.readlines())



def countChars(f):
    fh=open(f)
    return len(fh.read())


def test(f):
    return countLines(f),countChars(f)

if __name__ == '__main__':
    print(test('mymod.py'))
