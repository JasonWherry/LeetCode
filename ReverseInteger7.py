def reverse(x) -> int:
    if not isinstance(x, (int)):
        valType = type(x)
        print('ERROR: Given input "{}" is of type {}, not of type <class \'int\'>'.format(x, valType))
        return 0
    # y = 1
    # print(type(y))

    temp = list(str(x)) # turn input into a list of type string for iteration
    
    # check for negative
    neg = False
    if temp[0] == '-':
        neg = True
    print(temp)
    
    # if negative sign is present, start at index 1 to keep it there
    if neg:
        start = 1
    else:    
        start = 0
    end = len(temp)-1
    
    while start < end:
        temp[start], temp[end] = temp[end], temp[start]
        start += 1
        end -= 1
    
    val = ''
    for i in temp:
        val += i
    intval = int(val)
    if intval > 2147483647 or intval < -2147483648:
        return 0
    else:
        return intval

# positive tests
assert reverse(-456) == -654
assert reverse(2147483647) == 0
assert reverse(0) == 0

# negative tests
assert reverse(-200000000001) == 0
assert reverse('x') == 0
assert reverse('101') == 0
assert reverse([1,2,3,4]) == 0