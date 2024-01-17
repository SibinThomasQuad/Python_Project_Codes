Certainly! Below is a simple example using asyncio to run two functions concurrently and measuring the time it takes to complete both tasks:

```python
import asyncio
import time

async def task_one():
    print("Task One started")
    await asyncio.sleep(2)
    print("Task One completed")

async def task_two():
    print("Task Two started")
    await asyncio.sleep(1)
    print("Task Two completed")

async def main():
    start_time = time.time()

    # Run both tasks concurrently
    await asyncio.gather(task_one(), task_two())

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTotal time taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
```

In this example:

- `task_one` and `task_two` are two coroutines simulating tasks that take different amounts of time to complete using `asyncio.sleep`.
- The `main` coroutine uses `asyncio.gather` to run both tasks concurrently.
- The `time` module is used to measure the total time taken to complete both tasks.

When you run this script, you'll see output similar to the following:

```
Task One started
Task Two started
Task Two completed
Task One completed

Total time taken: 2.00 seconds
```

The output demonstrates that both tasks are executed concurrently, and the total time taken is close to the time taken by the longest-running task. This illustrates the advantage of asynchronous programming in handling tasks concurrently without blocking the execution.
