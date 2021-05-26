def people(*args):
    # args is a tuple
    print(args)
    n1, n2, *rest = args
    print(n1, n2, rest)
    len(args)

def country(**kwargs):
    print(kwargs)
    return kwargs