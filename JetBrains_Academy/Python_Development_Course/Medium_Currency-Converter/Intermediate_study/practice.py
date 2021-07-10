print('-'*20, 'EX-01', '-'*20)
    # Often programmers face a problem that can be solved by analogy.
    # You are already familiar with the string data type. 
    # Now you need to study the relevant section of the documentation about strings to solve this problem. 
    # https://docs.python.org/3/tutorial/introduction.html#strings
    # In the documentation you will find the necessary similar examples.

    # Your task is to correct the code so that the output would be the following:
        # It isn`t in the section 'C:\some\name_of_file'
print(r"It isn`t in the section 'C:\some\name_of_file'")
    # If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:
        # >>>
        # >>> print('C:\some\name')  # here \n means newline!
        # <<<C:\some
        # <<<ame
        # >>> print(r'C:\some\name')  # note the r before the quote
        # <<< C:\some\name


print('-'*20, 'EX-02', '-'*20)
    # A young programmer Mark wants to calculate the following expression:
        # First, get the remainder of dividing a by b.
        # Raise b to the power of a.
        # Subtract the two resulting numbers.
        # Get the absolute value of the subtraction.

    # But it seems that he made several errors in the code. 
    # In the Numeric Types section of the documentation, you can find a table describing the operations Mark wanted to perform.

    # You don't need to call the some_calculate() function or read from the input. 
    # Just implement the function and print the result after corrections.
def some_calculate(a, b):
    print(abs((a % b) - pow(b,a)))
some_calculate(2,3)


print('-'*20, "EX-03", '-'*20)
    # Mathematics is often useful in programming. 
    # Let's solve one math problem using the math library.

    # Your task is to implement the calculate_cosine() function. 
    # The function parameter is an angle in degrees.
    #  The function should calculate the cosine of the given angle using the corresponding math.cos() function from the math library, then round the result to two decimal places using the round(..., 2) function, and print it.

    # But it's not so simple. 
    # Read the documentation for this function and pay attention to what unit of measure the angle must be in.

    # You can find the additional function you need on the same page in the Angular conversion section.

    # Do not forget to import the necessary library. 
    # Don't call the function, just implement it.
# import the required library
import math

def calculate_cosine(angle_in_degrees):
    # do not forget to round the result and print it
    angle_in_radian = math.radians(angle_in_degrees)
    cosine = math.cos(angle_in_radian)
    print(round(cosine, 2))    
calculate_cosine(0)
calculate_cosine(60)

print('-'*20, 'EX-04', '-'*20)
    # Use Python's built-in help system to display brief information about the asctime() function from the time module.

    # Your output should be like this:
        # Help on built-in function asctime in time:

        # time.asctime = asctime(...) # or just asctime(...)
        #     asctime([tuple]) -> string
        # ...
        # ...

    # Do not use print().
# use built-in help system here
import time
help(time.asctime)


print('-'*20, 'EX-05', '-'*20)
    # Third-party libraries are part of a Python programmer's life. 
    # Many of these are documented at pypi.org, the Python Package Index (PyPI)[https://pypi.org/]. 
    # It is a repository of software for the Python programming language. 
    # Get familiar with some new libraries and find a suitable use for each based on their documentation:
        # Pandas [https://pypi.org/project/pandas/]
        # Requests [https://pypi.org/project/requests/]
        # PrettyTable [https://pypi.org/project/prettytable/]
    # Match the items from left and right columns
        # Pandas
            # Powerful data structures and time series data.
        # Requests
            # Working with HTTP requests.
        # PrettyTable
            # Data presentation in tabular format.


print('-'*20, 'EX-06', '-'*20)
    # One of the important parts of the documentation is the usual description of the structure of a certain unit of code. 
    # Read the first two paragraphs after the code example in the Defining Functions section and choose the correct statements from the list.
    # https://docs.python.org/3/tutorial/controlflow.html#defining-functions
        # [F]The first statement of the function body must be documentation string.
        # [F]The statements that form the body of the function are enclosed in {}.
        # [T]The keyword def must be followed by the function name and the parenthesized list of parameters.
        # [T]Including a documentation string, or docstring, is considered good practice.


print('-'*20, 'EX-07', '-'*20)
    # As you already understood, Python has many third-party libraries for a variety of purposes. 
    # For example, natural language processing plays quite an important role among them. 
    # NLTK is one of the main libraries for NLP purposes.
        # https://www.nltk.org/

    # Check out the documentation of this library and its examples.
    # Not everything may be clear to you now, but that's okay. 
    # From the options below, choose the line of code that will help you split the following sentence into words:
        # sentence = """We cannot solve our problems 
        # with the same thinking 
        # we used when we created them."""

    # The result after the operation should be the following:
        # ['We', 'can', 'not', 'solve', 'our', 'problems', 'with', 'the', 'same', 'thinking', 'we', 'used', 'when', 'we', 'created', 'them', '.']

        # Tokenize and tag some text:
            # >>> import nltk
            # >>> sentence = """At eight o'clock on Thursday morning
            #                ... Arthur didn't feel very good."""
            # >>> tokens = nltk.word_tokenize(sentence)
            # >>> tokens
            # <<< ['At', 'eight', "o'clock", 'on', 'Thursday', 'morning',
            #      'Arthur', 'did', "n't", 'feel', 'very', 'good', '.']
            # >>> tagged = nltk.pos_tag(tokens)
            # >>> tagged[0:6]
            # <<< [('At', 'IN'), ('eight', 'CD'), ("o'clock", 'JJ'), ('on', 'IN'),
            #      ('Thursday', 'NNP'), ('morning', 'NN')]


print('-'*20, 'EX-08', '-'*20)
    # Let's take a look at the Python documentation. 
        # https://docs.python.org/3/
    # Go to the Library Reference section and read its description at the beginning. 
    # What can you learn about in this section?
        # [F]the installation of Python environment on different platforms
        # [F]the syntax and "core semantics" of the language
        # [F]the capabilities of third-party Python libraries
        # [T]the capabilities of the standard Python libraries


print('-'*20, 'EX-09', '-'*20)
    # The Library Reference section contains a lot of necessary information, but sometimes it is difficult to understand where everything is. 
        # https://docs.python.org/3/library/index.html
    # Today is the time to be an explorer. 
    # Go down the page and you will see the sections headings:
    #     Introduction [https://docs.python.org/3/library/intro.html]
    #     Built-in Functions [https://docs.python.org/3/library/functions.html]
    #     Built-in Constants [https://docs.python.org/3/library/constants.html]
    #     ...
    #     Built-in-Exceptions [https://docs.python.org/3/library/constants.html]
    #     Data Types [https://docs.python.org/3/library/datatypes.html]
    
    # Your task is to look at some of them and select the appropriate statements about them. 
    # This will help you to learn how to navigate the documentation structure.

    # Match the items from left and right columns
        # Built-in Functions
            # Here's the documentation for the functions that are built into the Python interpreter. You can find out what the function does and what value it returns.
        # Built-in Types
            # In this section, you can learn about the different types of data and the operations they support.
        # Data Types
            # This module describes various specialized data types such as date and time.
        # Built-in Exceptions
            # It contains descriptions of various errors that you may encounter while writing code.