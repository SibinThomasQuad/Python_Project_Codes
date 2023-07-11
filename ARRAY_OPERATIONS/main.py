def array_sum(arr):
    """Calculates the sum of all elements in the array."""
    return sum(arr)

def array_average(arr):
    """Calculates the average of all elements in the array."""
    return sum(arr) / len(arr)

def array_min(arr):
    """Finds the minimum value in the array."""
    return min(arr)

def array_max(arr):
    """Finds the maximum value in the array."""
    return max(arr)

def array_sort(arr):
    """Sorts the array in ascending order."""
    return sorted(arr)

def array_reverse(arr):
    """Reverses the order of elements in the array."""
    return arr[::-1]

def array_unique(arr):
    """Returns a new array with unique elements from the input array."""
    return list(set(arr))

# Example usage:
my_array = [1, 2, 3, 4, 5]
print("Sum:", array_sum(my_array))
print("Average:", array_average(my_array))
print("Minimum:", array_min(my_array))
print("Maximum:", array_max(my_array))
print("Sorted array:", array_sort(my_array))
print("Reversed array:", array_reverse(my_array))
print("Unique elements:", array_unique(my_array))
