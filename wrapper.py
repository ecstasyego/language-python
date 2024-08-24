def function():
    def wrapper():
        def subwrapper():
            return 1 
        return subwrapper
    return wrapper

function()()()
