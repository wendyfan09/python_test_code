import copy
def remove_duplicates(numbers):
    if len(numbers) == 0:
        return numbers
    new_copy = copy.copy(numbers)
    new_copy.sort()
    result = []
    i = 1
    while i < len(new_copy):
        if new_copy[i - 1] != new_copy[i]:
            result.append(new_copy[i - 1])
            i += 1
        else:
            i += 1
    else:
        result.append(new_copy[len(new_copy) -1])
    return result

numbers = raw_input("please enter number list: ").split(",")
print remove_duplicates(numbers)