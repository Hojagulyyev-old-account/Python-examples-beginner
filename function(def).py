def hello():
    return 'Hello world !'

def alparslan():
    a = 5
    return a >= 5

def kwadrat(a):
    S = a*a
    return a

def listler(*args):
    return args

def dictionary(**kwargs):
    return kwargs

def myprint(*args, **kwargs):
    print(args)
    print('==========================')
    print(kwargs)

a = {
    'owez':'python',
    'suleyman':'python',
    "Aman":{
        'Selim':23,
        'alparslan':False
    }
}
myprint(a, Owez=23, Pena=45)

def cake(a, b, c):
    print(a)
    print(b)
    print(c)
    return a+b-c

def belli(a,b,c=3):
    return a, b, c

def goodbye(name):
    return f'Hello {name} !'


def listler(*args):
    return args

def dictionary(**kwargs):
    return kwargs

def myprint(*args, **kwargs):
    print(args)
    print('==========================')
    print(kwargs)

a = {
    'owez':'python',
    'suleyman':'python',
    "Aman":{
        'Selim':23,
        'alparslan':False
    }
}
myprint(a, Owez=23, Pena=45)
