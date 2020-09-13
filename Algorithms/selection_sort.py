def selection_sort(lst):
    for i in range(len(lst)):
        min_pos = i
        for j in range(i, len(lst)):
            if lst[min_pos] > lst[j]:
                min_pos = j
        temp = lst[i]
        lst[i] = lst[min_pos]
        lst[min_pos] = temp
    print(lst)


selection_sort([9, 8, 7, 6, 5, 4, 3, 2, 1])
