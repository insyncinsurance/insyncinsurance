from src.insync.insync import *

"""

By default, ICE sends referrals/declines to ICE rating using the following format:

info('Refer', ['CODE', 'Message about referral'])
or
info('Decline', ['CODE', 'Message about decline'])

This can become problematic if you want have a more specific messages including variables/lists/dictionaries to send to ICE rating.
The insync module provides an easier and quicker way to send referrals/declines.

The format is:

refer(code, *message)
or
decline(code, *message)

Note: You can add as many parameters as you want to the message.

"""

refer('Claim', 'This is a referral message about a claim you had on', claim_date)

decline('Claim', 'This is a decline message about a claim you had on', claim_date)

# You can also create a custom referral function using the create_message function.

test = create_message('Test')

test('This is a test message.', 'It will display anything you want.') # This will send a referral message to ICE Rating using the code 'Test'.

