def hello_world_recursive(n):
    if n <= 0:
        return
    print("Hello World")
    hello_world_recursive(n - 1)

# Example usage:
hello_world_recursive(5)
