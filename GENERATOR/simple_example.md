Certainly! Here's a simple example of a generator function in Python:

```python
def countdown_generator(n):
    while n > 0:
        yield n
        n -= 1

# Using the generator
countdown = countdown_generator(5)

for number in countdown:
    print(number)
```

In this example, `countdown_generator` is a generator function that yields countdown numbers from a given starting point (`n`) down to 1. The generator is used in a `for` loop to print each countdown number.

When you run this code, it will output:

```
5
4
3
2
1
```

The key points in the example are:

1. The `countdown_generator` function contains a `while` loop that runs until `n` becomes 0.
2. Inside the loop, the `yield` statement produces the current value of `n` and temporarily suspends the function's state.
3. When the generator is used in a `for` loop, each call to `next()` resumes the function from where it was suspended, producing the next value in the sequence.

Generators are memory-efficient and allow you to work with sequences of values without having to store the entire sequence in memory. They are especially useful for handling large datasets or generating sequences on-the-fly.
