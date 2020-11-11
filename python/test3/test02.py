def quick(list, first, last):
    if first >= last:
        return
    hi = last
    lo = first
    mid_value = list[first]
    while hi > lo:
        while (hi > lo) and (list[hi] > mid_value):
            hi -= 1
        list[lo] = list[hi]
        while (hi > lo) and (list[lo] < mid_value):
            lo += 1
        list[hi] = list[lo]
    list[lo] = mid_value
    quick(list, first, lo)
    quick(list, lo + 1, last)

if __name__ == "__main__":
    list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick(list, 0, len(list) - 1)
    print(list)
