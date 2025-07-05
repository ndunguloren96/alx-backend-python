#!/usr/bin/python3
from itertools import islice
# Corrected import: Use __import__ as per problem statement
stream_users_module = __import__('0-stream_users')
stream_users = stream_users_module.stream_users # Access the function from the module

# iterate over the generator function and print only the first 6 rows

for user in islice(stream_users(), 6):
    print(user)


