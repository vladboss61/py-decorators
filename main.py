from time import time

#Decorator function measure_time without parameters -> @measure_time
def measure_time(decoratee_func):
    def wrapper(*args, **kargs):

        currnet_start = time()
        result = decoratee_func(*args, **kargs)
        currnet_end = time()

        print(f"Function Name: {decoratee_func.__name__}")
        print(f"Elapsed Time: {round(currnet_end - currnet_start)}")
        print(f"Result: {result}")

        return result
    return wrapper

#Decorator function log with parameters -> @log("ERROR", "Eror message") for instance
def log(logType: str, msg: str): # logType and msg params passed through decorator function
    def decorator(func): # decoratee function
        def wrapper(*args, **kargs): # params for decoratee function

            print(f"Log Type: {logType}")
            print(f"Message: {msg}")
            print(f"Function name: {func.__name__}")

            result = func(*args, **kargs) # execution of decoratee function

            if result:
                print(f"Function invocation result: {result}")
            return result # return from decorator result of function
        
        return wrapper
    return decorator

# Usage

@measure_time
@log("INFO", "General info")
def run1(value: int) -> None:
    print(10 + value)

@measure_time
@log("ERROR", "Eror message")
def run2(value: int) -> int:
    res = 33 + value
    print(33 + value)
    return res

log("TEST", "Test info")(run1)(123)

run1(999)

res = run2(111)
print("Test result")
print(res)