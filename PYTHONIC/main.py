def len_example():
    string = "Hello, World!"
    length = len(string)
    print(length)  # Output: 13

def sorted_example():
    numbers = [4, 2, 7, 1, 9]
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)  # Output: [1, 2, 4, 7, 9]

def range_example():
    for i in range(1, 5):
        print(i)
    # Output:
    # 1
    # 2
    # 3
    # 4

def enumerate_example():
    fruits = ['apple', 'banana', 'cherry']
    for index, fruit in enumerate(fruits):
        print(index, fruit)
    # Output:
    # 0 apple
    # 1 banana
    # 2 cherry

def zip_example():
    names = ['John', 'Jane', 'Mike']
    ages = [25, 30, 35]
    for name, age in zip(names, ages):
        print(name, age)
    # Output:
    # John 25
    # Jane 30
    # Mike 35

def map_example():
    numbers = [1, 2, 3, 4]
    squared_numbers = list(map(lambda x: x**2, numbers))
    print(squared_numbers)  # Output: [1, 4, 9, 16]

def filter_example():
    numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)  # Output: [2, 4, 6]

def sum_example():
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    print(total)  # Output: 15

def any_example():
    values = [True, False, True]
    result = any(values)
    print(result)  # Output: True

def all_example():
    values = [True, False, True]
    result = all(values)
    print(result)  # Output: False

def max_example():
    numbers = [7, 3, 9, 5, 1]
    maximum = max(numbers)
    print(maximum)  # Output: 9

def min_example():
    numbers = [7, 3, 9, 5, 1]
    minimum = min(numbers)
    print(minimum)  # Output: 1

def reversed_example():
    numbers = [1, 2, 3, 4]
    reversed_numbers = list(reversed(numbers))
    print(reversed_numbers)  # Output: [4, 3, 2, 1]

def join_example():
    names = ['John', 'Jane', 'Mike']
    joined_names = ', '.join(names)
    print(joined_names)  # Output: John, Jane, Mike

def format_example():
    name = 'Alice'
    age = 25
    formatted_string = "My name is {} and I am {} years old.".format(name, age)
    print(formatted_string)  # Output: My name is Alice and I am 25 years old.

# Run the examples
len_example()
sorted_example()
range_example()
enumerate_example()
zip_example()
map_example()
filter_example()
sum_example()
any_example()
all_example()
max_example()
min_example()
reversed_example()
join_example()
format_example()
