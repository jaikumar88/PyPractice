# Exception handling in python is used try , except and finally to handle exceptions

try:
    x = 10/1
except ZeroDivisionError:
    print("cannot devide by zero")
finally:
    print("Funally called")
    
class CustomeException(Exception):
    """Custom exception class"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidAgeException(Exception):
    def __init__(self, message="Age is not valid"):
        self.message=message
        super().__init__(self.message)

def check_age(age):
    if age < 0:
        raise InvalidAgeException("Age cannot be negative")
    elif age < 18:
        raise InvalidAgeException("Age must be 18 or older")
    else:
        print(f"Age is {age}  valid")

def main():
    try:
        age = int(input("Enter your age:"))
        check_age(age)
    except InvalidAgeException as e:
        print(f"Error {e}")
    else:
        print("age is valid")
    finally:
        print("Execution completed")

if __name__ == "__main__":
    main()