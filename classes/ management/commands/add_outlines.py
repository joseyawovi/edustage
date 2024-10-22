# Import your models (replace 'yourapp' with the name of your app)
from classes.models import Course, Outline, SubOutline

# Create a course instance
course = Course.objects.create(title="Python Programming BootCamp")

# Define the outlines and sub-outlines
outlines_data = [
    {
        "title": "Introduction to Python",
        "sub_outlines": [
            "What is Python?",
            "Installing Python and Setting up the Environment",
            "Writing and Running Your First Python Script",
            "Understanding Python’s Role in Software Development"
        ]
    },
    {
        "title": "Python Basics",
        "sub_outlines": [
            "Variables and Data Types (int, float, str, etc.)",
            "Input/Output Functions (print() and input())",
            "Basic Operators and Expressions",
            "Understanding Indentation and Code Structure in Python"
        ]
    },
    {
        "title": "Control Flow",
        "sub_outlines": [
            "Conditional Statements (if, else, elif)",
            "Loops in Python (for and while)",
            "Break, Continue, and Pass Statements",
            "Using range() in Loops"
        ]
    },
    {
        "title": "Functions in Python",
        "sub_outlines": [
            "Defining and Calling Functions",
            "Parameters and Arguments",
            "Return Values",
            "Scope of Variables (Local vs Global)",
            "Lambda Functions"
        ]
    },
    {
        "title": "Data Structures",
        "sub_outlines": [
            "Lists: Creating, Accessing, and Modifying Lists",
            "Tuples: When to Use Tuples Over Lists",
            "Sets: Unique Elements and Set Operations",
            "Dictionaries: Key-Value Pairs, Accessing, and Updating"
        ]
    },
    {
        "title": "Working with Files",
        "sub_outlines": [
            "Reading from a File",
            "Writing to a File",
            "File Handling with Context Managers (with open())",
            "Working with Different File Types (Text, CSV)"
        ]
    },
    {
        "title": "Error Handling and Exceptions",
        "sub_outlines": [
            "Understanding Exceptions in Python",
            "Try, Except, Else, and Finally Blocks",
            "Raising Custom Exceptions",
            "Common Exceptions (ZeroDivisionError, FileNotFoundError, etc.)"
        ]
    },
    {
        "title": "Object-Oriented Programming (OOP)",
        "sub_outlines": [
            "Introduction to Classes and Objects",
            "Attributes and Methods",
            "The self Keyword",
            "Inheritance and Polymorphism",
            "Encapsulation and Abstraction"
        ]
    },
    {
        "title": "Modules and Packages",
        "sub_outlines": [
            "Importing Modules",
            "Using Python’s Built-in Libraries",
            "Creating and Using Custom Modules",
            "Working with pip and Installing External Packages"
        ]
    },
    {
        "title": "Advanced Python Topics",
        "sub_outlines": [
            "List Comprehensions",
            "Generator Functions",
            "Decorators: Adding Functionality to Functions",
            "Context Managers"
        ]
    },
    {
        "title": "Bonus Outline: Python for Data Science (Optional)",
        "sub_outlines": [
            "Introduction to NumPy and Pandas",
            "Data Analysis with Pandas",
            "Plotting with Matplotlib",
            "Reading and Analyzing Data from CSV Files"
        ]
    }
]

# Iterate over outlines_data and create Outline and SubOutline objects
for outline_data in outlines_data:
    outline = Outline.objects.create(course=course, title=outline_data['title'])
    
    for sub_outline_title in outline_data['sub_outlines']:
        SubOutline.objects.create(outline=outline, title=sub_outline_title)

print("Outlines and Sub-Outlines created successfully!")
