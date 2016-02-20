def in_asc_order(arr):
    sort_arr = sorted(arr, key=int)
    bad_sort = sorted(arr, key=int, reverse=True)
    if arr == sort_arr:
        return True
    elif arr == bad_sort:
        return False
    if arr != sort_arr and arr != bad_sort:
        return False

print(in_asc_order([3, 2, 6]))
