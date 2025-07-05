#!/usr/bin/python3
import sys
# Corrected import: Use __import__ as per problem statement
lazy_paginator_module = __import__('2-lazy_paginate')
lazy_pagination = lazy_paginator_module.lazy_pagination # Access the function from the module


try:
    for page in lazy_pagination(100):
        for user in page:
            print(user)

except BrokenPipeError:
    sys.stderr.close()

