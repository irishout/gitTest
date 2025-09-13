
def bin_search(lis, target, l, r):
    left = l
    right = r
    while left <= right:
        mid = (left + right)//2
        if lis[mid] == target:
            return mid
        else:
            if target > lis[mid]:
                left = mid
            else:
                right = mid


#blahblahblah