def sort(lst):
    lst.sort()
    sorted_list = []
    sublist = []
    y = 0
    while y < len(lst) - 1:
        if lst[y] + 1 != lst[y + 1]:
            if len(sublist) > 0:
                sorted_list.append(f'{sublist[0]}-{lst[y]}')
                sublist = []
            else:
                sorted_list.append(f'{lst[y]}')
        else:
            sublist.append(f'{lst[y]}')
        y += 1
    return ', '.join(sorted_list)

def seq(arr):
    arr = arr.copy()
    arr.sort()
    
    start = arr[0]
    end = arr[0]
    i = 1
    result = []
    for e in arr:
        if start == e:
            continue
        elif start + i == e:
            end = e
            i += 1
        else:
            result.append(f'{start}-{end}' if start != end else f'{start}')
            i = 1
            start = e
            end = e
    return ', '.join(result)

lst = [33, 24, 37, 28, 41, 39, 17, 18, 43, 36, 44, 15, 34, 38, 29, 42, 26, 20]
sorted_list = sort(lst)
print(sorted_list)