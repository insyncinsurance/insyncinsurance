from src.insync.insync import *

"""

The following example shows how to instantiate a policy object and set its premium. It also shows
useful debugging tools.

"""

# Create a new instance of 'Policy' for Public Liability
# Note: the class name (PL) and policy name ('Public Liability') can be anything. This is particularly useful for multiple policies (i.e. Public Liability, Employers Liability, Contents, etc.)

PL = Policy('Public Liability')

PL.add(100) # Add £100 to the policy premium
PL.rate(0.9) # Reduce the policy premium by 10%. This also works for adding loading (e.g. PL.rate(1.5))
PL.discount(50) # Reduce the policy premium by £50

debugging.toggle() # Toggle debugging on. This is best placed at the top of your code.

debugging.send('This is an example statement.', 'I can add many parameters, arrays or variables.') # Sends a debug message to ICE Rating

debugging.breakdown() # Sends a debug message to ICE Rating with a breakdown of the all policy premiums

"""

The debugging tool is useful for debugging and understanding how the policy works.
You can keep in the send/breakdown methods in the live environment, providing you remove the debugging.toggle().
By default the debugging is off unless debugging.toggle() is called.

"""


