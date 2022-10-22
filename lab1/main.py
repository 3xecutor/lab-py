def func(list):
    def Min(arg1):
        minimum = min(arg1)
        return minimum
    def Max(arg2):
        maximum = max(arg2)
        return maximum
    def Last(arg3):
        myMax = Max(arg3)
        myMin = Min(arg3)
        arg3 = list
        def remove():
            arg3.remove(myMin)
            arg3.remove(myMax)
            for i in arg3:
                return i
        return remove()

    print(Max(list))
    print(Min(list))
    print(Last(list))

func([1,2,3])
