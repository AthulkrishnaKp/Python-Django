# Variable length arguments *args - Non keyword argument.

def var_length(*args):      # Tuple
    print(type(args))
    for i in args:
        print(i)
var_length(10,20)
var_length(1,2,3)

# Variable length arguments **karg -  keyword argument.

def fun(**karg):              # Dictionary
    print(type(karg))
    for k,v in karg.items():
        print(k,":",v)

fun(Name='Athul',cls='Btech')