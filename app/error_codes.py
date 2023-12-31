"""
This file contains all of the error signatures that can be raised
by functions defined in other files.
"""

# Request related
BAD_REQUEST = "ERR_BAD_REQUEST"

# JWT related
JWT_EXPIRED = "ERR_JWT_EXPIRED"
JWT_INVALID = "ERR_JWT_INVALID"
JWT_OTHER = "ERR_JWT_OTHER"

# Firebase related
FIRESTORE_ERROR = "ERR_FIRESTORE"

# Live mode related
TENSOR_INVALID = "ERR_TENSOR_INVALID"
