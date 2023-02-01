# Countdown
def count_down(num):
    count_list = []
    for i in range(num, -1, -1):
        #print(i)
        count_list.append(i)
    return count_list
print(count_down(5))

# Print and Return
def print_return(p, r):
    print(p)
    return r
print_return(3, 2)
print(print_return(3,2))

# Values Greater than Second
def greater_than_second(arr):
    result = []
    if len(arr)<2: return False
    for i in range(len(arr)-1):
        if arr[i]>arr[1]:
            result.append(arr[i])
    print(len(result))
    return result
arr1 = [5,2,4,3,1]
arr2 = [1]
print(greater_than_second(arr2))

# First Plus Length
def first_plus_len(arr):
    return arr[0] + len(arr)
print(first_plus_len([2,4,1,3,0,10]))

# This Length, That Value
def len_val(s,v):
    arr = []
    for i in range(s):
        print(i)
        arr.append(v)
    return arr
print(len_val(3,1))