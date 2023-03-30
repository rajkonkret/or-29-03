# funkcje zagnieżdzone
def fun_1():
    print("To jest fun1()")

    def fun_2():
        print("To jest fun2()")

    return fun_2  # bez znawiasow


xFun = fun_1()  # przypiasnie do XFun tego co zwraca fun1()
print(xFun)  # xFun teraz zawiera fun2()
print(type(xFun))
xFun()  # wywołanie funkcji fun2() bo mamy ją w xFun
