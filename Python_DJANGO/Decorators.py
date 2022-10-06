
#decorators : adding new features to function without adding more details in function.

def swap_dec(fn):               # dec must have a fun()
    def wrapper(n1,n2):         # dec must have an inner fun()
        if n2>n1:
            n1,n2=n2,n1
        return fn(n1,n2)        # fn - div
    return wrapper              # calling wrapper funstion symbol must not be used ()

@swap_dec
def div(n1,n2):
    return n1/n2

@swap_dec
def sub(n1,n2):
    return n1-n2


print(div(2,10))
print(sub(2,10))

