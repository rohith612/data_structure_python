# Compare x with the middle element.

# If x matches with the middle element, we return the mid index.

# Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.

# Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.

def binary_search(elements, low, high, key):
    #  at first low will be 0, high will be 8
    # 1 - 8>0 = true
    # 2 - 8>5 = true
    # 3 - 8>7 = true
    # 4 - 8>=8 = true
    # 5 - 8>9 = false => return not found!!!
    if high >= low:
        # 1 - 8+0/2 = mid = 4 => el => 10
        # 2 - 8+5/2 = mid = 6 => el => 60
        # 3 - 8+7/2 = mid = 7 => el => 78
        # 3 - 8+8/2 = mid = 8 => el => 100
        mid = (high + low) // 2

        # 1 - 101 = 10 => false
        # 2 - 101 = 60 => false
        # 3 - 101 = 78 => false
        # 4 - 101 = 100 => false
        if  key == elements[mid]:
            return True

        # 1 - 101 < 10 => false
        # 2 - 101 < 60 => false
        # 3 - 101 < 78 => false 
        # 4 - 101 < 100 => false
        elif key < elements[mid]: 
            return binary_search(elements, low, mid - 1, key)

        # 1 - 101 > 10 => true
        # 2 - 101 > 60 => true
        # 3 - 101 > 78 => true
        # 4 - 101 > 100 => true
        elif key > elements[mid]:
            # 1 - low = 5, high = 8
            # 2 - low = 7, high = 8
            # 3 - low = 8, high = 8
            # 4 - low = 9, high = 8 
            return binary_search(elements, mid + 1, high, key)

    else:
        return False



element_list = [4, 6, 8, 9, 10, 45, 60, 78, 100]
search_key = 101
list_start = 0
list_end = len(element_list) - 1

is_found = binary_search(element_list, list_start, list_end, search_key)

print(is_found)