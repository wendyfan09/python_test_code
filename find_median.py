def median(numbers):
    result = 0
    numbers.sort()
    length = len(numbers)
    if length % 2 != 0:
        result = numbers[length / 2 ]
    else:
        result =(numbers[(length / 2) -1] + numbers[length /2]) /2.0
    return result
print median([1,2,3,2,4,2,3,4,1])