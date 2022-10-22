def main(list):
    def Min(arg):
        minimum = min(arg)
        return minimum
    def Max(arg):
        maximum = max(arg)
        return maximum
    def Last(arg):
        myMax = Max(list)
        myMin = Min(list)
        def remove():
            list.remove(myMin)
            list.remove(myMax)
            int_list = int(''.join(map(str, list)))
            return int_list
        return remove()

    print(Max(list))
    print(Min(list))
    print(Last(list))

if __name__ == "__main__":
    main([1, 2, 3])
