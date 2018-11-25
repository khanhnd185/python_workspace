def spam(arg):
    arg.append('Hello')

eggs = [1,2,3]
spam(eggs)
print(eggs)


def foo(arg):
    arg += 1
    print(arg)

bar = 1
foo(bar)
print(bar)
