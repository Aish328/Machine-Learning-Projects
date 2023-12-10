from speak import male
from speech import rect


response = {'Hi  1  Welcome', 'How may i help','sorry could not solve '}

def operations_from_text(text):

    l = []
    for t in text.split(''):
        try :
            l.append(float(t))
        except ValueError:
            pass
    return l
#defining functions:

def lcm(a,b):
    if  a>b:
        L = a
    else:
        L = b
    while L <= a*b:
        if L%a == 0 and L % b == 0:
            return L
        L+=1

def hcf(a,b):
    H = a if a>b else b
    while H>=1 :
        if a%H == 0 and b%H == 0 :
            return H
        H -= 1

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b
def mod(a,b):
    return a%b

def start():
    male(response[0])
    print(response[0])

def help():
    male(response[1])
    print(response[1])

def sorry():
    male(response[2])
    print(response[0])

operations= {'ADD': add,
              'PLUS': add,
              'SUM': add,
              'ADDITION': add,
              'SUB': sub,
              'SUBTRACT': sub,
              'MINUS': sub,
              'DIFFERENCE': sub,
              'LCM': lcm,
              'HCF': hcf,
              'PRODUCT': mul,
              'MULTIPLY': mul,
              'MULTIPLICATION': mul,
              'DIVIDE': div,
              'DIVISION': div,
              'MOD': mod,
              'REMANDER': mod,
              'MODULAS': mod}

commands = {'START' : start , 'HELP' : help , 'SORRY' : sorry}

def calci():
    while True:
        print("enter your queries:")
        male("enter your queries:")
        text = rect()
        r = 0
        for word in text.split(''):
            if word.upper() in operations.keys():
                try:
                    l = operations_from_text(text)
                    q = str(operations[word.upper()].__name__)
                    if q == 'mul':
                        r =1 
                        for i in range(len(l)):
                            r = operations[word.upper()](r , l[i])
                    elif q == 'add':
                        for i in range(len(l)):
                            r = operations[word.upper()](r , l[i])
                    elif q == 'div' or 'lcm' or 'hcf' or 'sub':
                        r = float(l[0])
                        for i in range (1 , len(l)):
                            r = operations[word.upper()](r,l[i])
                    elif q == 'mod':
                        r = operations[word.upper()](l[0], l[1])

                    print(r)
                    male(r)
                    return(r)
                    break
                except:
                    print('something went wrong')
                    male('something went wrong')
                    r = 'something went wrong'
                    break
                finally:
                    break
            elif word.upper() in commands.keys():
                commands[word.upper()]()
                break
        else:
            sorry()
        return(r)





