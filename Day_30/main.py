try:
    # Code block where you anticipate an error
    # If an error occurs here, it will be caught in the except block
    # If no error occurs, it will proceed to the else block
    pass  # Your code here

except:  # Specify the particular exception you want to catch, or use a more general Exception
    # Code block to handle the exception
    pass  # Your code here

else:
    # Code block that executes if no exception occurs in the try block
    pass  # Your code here

finally:
    # Code block that always executes whether an exception occurs or not
    pass  # Your code here

"""
Types of Errors in Python:

SyntaxError: Occurs when the syntax used in the code is invalid.
IndentationError: Arises when incorrect indentation is used.
NameError: When a name or variable is not found in the local or global scope.
TypeError: Occurs when an operation or function is applied to an object of an inappropriate type.
ValueError: Arises when a function receives an argument of the correct type but an inappropriate value.
IndexError: Occurs when trying to access an index that is out of range in a sequence.
KeyError: Occurs when trying to access a key that doesn't exist in a dictionary.
FileNotFoundError: When a file or directory is requested but cannot be found.
IOError: Generally happens when an input/output operation fails.
AssertionError: When an assert statement fails.
ZeroDivisionError: Arises when division or modulo by zero is attempted.
AttributeError: Occurs when an attribute reference or assignment fails.
KeyboardInterrupt: Happens when the user interrupts the execution, typically using Ctrl+C.
"""

# Raise your own errors
guess_number = int(input("Guess a number? "))

if guess_number != 5:
    raise ValueError("This is not the number what I want wanted 😅")
