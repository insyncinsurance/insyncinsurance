from src.insync.insync import *

"""

Scripting in ICE Rating can be difficult and is error prone. 
To make it easier, the insync module provides a number of functions to make it easier and quicker.

Below are some examples of how to use the insync module for scripting.

"""

GIO_trades = getList('GenericInsuredObject', 'WorkbenchFieldName') # Returns a list of all the part names in the GenericInsuredObject
# Note: This can be used for any part type (i.e. GenericInsuredObject, Claim, Policyholder, etc.)

"""

Instead of using multiple try statements for each workbench field, you can use the tryAll function.

Example:

"""

PolicyFields = ['WorkbenchField1', 'WorkbenchField2', 'WorkbenchField3']

tryAll(PolicyFields)

# This will try each workbench field in the list in turn. If any return an error, it will send an error message to ICE Rating.
# If debug mode is enabled, it will also display the error message. (ref: see example/setting_policy_premiums.py)


"""

To make it easier to use the insync module, the following functions are also provided:
- addAddon()
- addCover()
- addFee()

All corresponding arrays are also provided.

"""