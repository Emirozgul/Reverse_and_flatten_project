

def reverse(x):
    x.reverse()
    for i in x:
        if type(i) is list:
            i.reverse()
            for a in i:
                if type(a) is list:
                    a.reverse()
                    for b in a:
                        if type(b) is list:
                            b.reverse()
                            for c in b:
                                if type(c) is list:
                                    c.reverse
    return x



def flat(x):
    f=[]
    for i in x:
        if type(i) is list:
            for a in i:
                if type(a) is list:
                    for b in a:
                        if type(i) is list:
                            for c in b:
                                f.append(c)
                        else:
                            f.append(b)
                else:
                    f.append(a)
        else:
            f.append(i)
    return f
