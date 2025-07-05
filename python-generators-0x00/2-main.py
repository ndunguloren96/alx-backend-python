#!/usr/bin/python3
import sys
# Corrected import: Use __import__ as per problem statement
processing_module = __import__('1-batch_processing')
batch_processing = processing_module.batch_processing # Access the function from the module

##### print processed users in a batch of 50
try:
    # Iterate over the generator yielded by batch_processing
    for user in batch_processing(50):
        print(user)
except BrokenPipeError:
    sys.stderr.close()


