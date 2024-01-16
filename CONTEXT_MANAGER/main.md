Sure, let's create a simple example of a custom context manager. In this example, we'll create a context manager that measures the time it takes for a block of code to execute:

```python
import time

class TimerContextManager:
    def __enter__(self):
        self.start_time = time.time()
        return self  # The instance of TimerContextManager is returned and can be used within the "with" block

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f'Time elapsed: {elapsed_time} seconds')

# Using the TimerContextManager
with TimerContextManager() as timer:
    # Some code that you want to measure the execution time for
    for _ in range(1000000):
        pass  # Simulating some time-consuming operation

# The TimerContextManager automatically prints the elapsed time when exiting the "with" block
```

In this example:

- The `TimerContextManager` class has `__enter__` and `__exit__` methods.
- In the `__enter__` method, it records the start time.
- The instance of `TimerContextManager` is used within the "with" block (assigned to the variable `timer`).
- The `__exit__` method calculates the elapsed time and prints it when the "with" block is exited.

Using context managers in this way provides a clean and reusable mechanism for measuring the execution time of code blocks without having to manually manage the start and end times.
