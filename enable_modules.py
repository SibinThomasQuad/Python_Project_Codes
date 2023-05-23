def feature_enabled(feature_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if feature_name in enabled_features:
                # Execute the decorated function if the feature is enabled
                return func(*args, **kwargs)
            else:
                # Print a message or perform alternative action if the feature is disabled
                print(f"Feature '{feature_name}' is disabled.")
        return wrapper
    return decorator

# Example list of enabled features
enabled_features = ['feature1', 'feature3']

# Example usage
@feature_enabled('feature1')
def feature1_function():
    print("Feature 1 function executed.")

@feature_enabled('feature2')
def feature2_function():
    print("Feature 2 function executed.")

@feature_enabled('feature3')
def feature3_function():
    print("Feature 3 function executed.")

# Execute the functions
feature1_function()
feature2_function()
feature3_function()
