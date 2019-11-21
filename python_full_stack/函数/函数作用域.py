"""
day16 函数作用域
"""
def foo():
    name = "1hf"
    def bar():
        name = "wupeiqi"
        def tt():
            print(name)
        return tt
    return bar

bar = foo()
print(bar)
tt = foo()()
tt()
tt = foo()()()