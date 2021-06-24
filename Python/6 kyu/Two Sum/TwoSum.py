def two_sum(numbers, target):
    for i in range(0,len(numbers)):
        for n in range(i+1,len(numbers)):
            if(numbers[i]+numbers[n] == target):
                return i, n