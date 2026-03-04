def outer_function(text):
    def inner_function():
        print(f"The message is: {text}")
    inner_function()

outer_function("Hello, World!")
