def process_lists(list1, list2):
    result = []
    
    for num in list1:
        if num not in result:
            result.append(num)
    
    for num in list2:
        if num not in result:
            result.append(num)
    
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]
    
    return result

print(process_lists([1, 2, 3], [3, 4]))
print(process_lists([], [5, 0, -1]))
print(process_lists([], []))