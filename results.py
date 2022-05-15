#answer for 1
def create_tuple(first, second):
    mytuple = (first, second)
    return mytuple

#answer for 3
def odd_nums(tuple):
    c = 0
    for nums in tuple:
        if nums % 2 != 0:
            c +=1
    return c

#answer for 4
def tuple():
    tuple2 = (1,2,3)
    for i in tuple2:
        print(i)

#answer for 6
def avg_nums(tuple):
    c = 0
    for num in tuple:
        c += num
    return c / len(tuple)

#answer for 7
def len_tuple(tuple):
    for num in tuple:
        if num == len(tuple):
          return True
    else:
       return False
