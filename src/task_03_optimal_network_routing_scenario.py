import hashlib


def simple_hash(hash: str):
    """Method used for generating and
    verifying the hash values of the data fragments"""
    return


def reconstruct_data(fragments: dict):
    """Method to verify the integrity of each fragment using its
    corresponding hash value prior to the reconstruction"""

    return


fragments = {
    1: {"data": "Hello", "hash": simple_hash("Hello")},
    2: {"data": "World", "hash": simple_hash("World")},
    3: {"data": "!", "hash": simple_hash("!")},
}

original_data = reconstruct_data(fragments)
print(fragments)
print(original_data)
