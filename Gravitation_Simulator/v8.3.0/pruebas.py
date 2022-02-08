









def conv(n):    
        while '/' in n:
            ind_a = n.index('/')
            loc = n[ind_a+1::]
            ind_b = len(loc)
            for m,e in enumerate(loc):
                if e in '+*-' and loc[m-1] != 'e':
                    ind_b = m
                    break
            n = n[0:ind_a] + '*' + str(1/float(loc[0:ind_b])) + n[ind_a+ind_b+1::]
        n = n.replace('-', '+-').replace('*+-', '*-').replace('e+-', 'e-').replace('e+','e').split('+')
        if n[0] == '':
            n = n[1::]
        for j,e in enumerate(n):
            loc2 = 1
            for el in e.split('*'):
                if '^' in el:
                    el = el.split('^')
                    loc2 *= float(el[0])**float(el[1])
                else:
                    el = el.split('e')
                    loc2 *= float(el[0]) if len(el) == 1 else float(el[0])*(10**float(el[1]))
            n[j] = loc2
        return sum(n)


def calc_min(var):
    sindex = 0
    findex = 0
    value = var
    if '(' in var:
        sindex = var.index('(')
        findex = var.index(')')
        if '(' in var[sindex+1: findex + 1]:
            value = calc_min(var[sindex + 1: findex + 1])
        else:
            value = var[sindex: findex + 1]
    else:
        return value
    return value

def calcp(v):
    nums = '1234567890'
    for n in nums:
        if n+'(' in v:
            v = v.replace(n+'(', f'{n}*(')
        if ')'+n in v:
            v = v.replace(')'+n, f')*{n}')
    while '(' in v:
        r = calc_min(v)
        print(r)
        print(v)
        v = v.replace(r, str(conv(r[1:len(r)-1])))
        print(v)
    return conv(v)
    

def calc(v):
    v = v.replace(' ', '').replace(')(', ')*(')
    v2 = v.split(',')
    eq = v2[0]
    l = 'abcdfghijklmnopqrstuvxyz'
    if len(eq) > 1:
        for var in v2[1::]:
            var = var.split('=')
            eq = eq.replace(var[0],str(calcp(var[1])))
    flag = True
    for c in eq:
        if c in l:
            flag = False
            break
    print(eq)
    if flag:
        return calcp(eq) 
    else:
        return None


print(calc('((2*G*M*rc)/(rl(rc+rl)))^0.5, G = 6.67e-11, M = 1.989e30, rc = 4.6e10, rl = 6.98e10'))