def b_search(list, item):#二分查找 返回角标
    low = 0
    high = len(list) - 1
    while(low <= high):
        mid = (low+high)//2 #地板除取整
        guess = list[mid]
        if guess == item:
            return mid
        elif guess>mid:
            low = mid + 1
        else:
            high = mid - 1;
    return -1

if __name__ == '__main__':
    list_a = [1,5,9,10,55,67,89,100]
    print(b_search(list_a, 89))