import redis

# Connect to Redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def add_data(key, value):
    """
    Add data to Redis with the specified key and value.
    """
    redis_client.set(key, value)

def get_data(key):
    """
    Get data from Redis for the specified key.
    """
    return redis_client.get(key)

def delete_data(key):
    """
    Delete data from Redis for the specified key.
    """
    return redis_client.delete(key)

def update_data(key, new_value):
    """
    Update data in Redis for the specified key with a new value.
    """
    if redis_client.exists(key):
        redis_client.set(key, new_value)
    else:
        raise ValueError("Key does not exist in Redis")

def increment_counter(key):
    """
    Increment a counter value stored in Redis for the specified key.
    """
    return redis_client.incr(key)

def decrement_counter(key):
    """
    Decrement a counter value stored in Redis for the specified key.
    """
    return redis_client.decr(key)

def append_to_list(key, *values):
    """
    Append one or multiple values to a list stored in Redis for the specified key.
    """
    return redis_client.rpush(key, *values)

def get_list_elements(key):
    """
    Get all elements from a list stored in Redis for the specified key.
    """
    return redis_client.lrange(key, 0, -1)

def list_all_keys():
    """
    List all keys stored in Redis.
    """
    return redis_client.keys()

# Example usage
if __name__ == "__main__":
    # Add data
    add_data("name", "John")
    
    # Get data
    print("Data for 'name':", get_data("name"))
    
    # Update data
    update_data("name", "Jane")
    print("Updated data for 'name':", get_data("name"))
    
    # Increment counter
    print("Counter value after increment:", increment_counter("counter"))
    
    # Decrement counter
    print("Counter value after decrement:", decrement_counter("counter"))
    
    # Append to list
    append_to_list("fruits", "apple", "banana", "orange")
    print("List elements:", get_list_elements("fruits"))
    
    # List all keys
    print("All keys in Redis:", list_all_keys())
