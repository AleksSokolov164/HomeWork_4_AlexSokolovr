def my_function(**kwargs):
    for k,v in kwargs.items():
        print(k,'--->',v, sep=' ')


my_function(name='Z',age=20)

def megafunction(first, second='2',*args, **kwargs ):
    print(first)
    print(second)
    print(args)
    print(kwargs)

megafunction(1,'second',1,2,2,4,5,name=1,data=11 )