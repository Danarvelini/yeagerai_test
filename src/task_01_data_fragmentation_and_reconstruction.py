import hashlib


def simple_hash(data: str):
    """Method used for generating and
    verifying the hash values of the data fragments"""

    hash_value = hashlib.sha256(data.encode()).hexdigest()
    return hash_value[:30]


def reconstruct_data(fragments: dict) -> str:
    """Method to verify the integrity of each fragment using its
    corresponding hash value prior to the reconstruction"""

    try:

        reconstructed_data = ""

        for i, fragment in sorted(fragments.items()):
            fragment_hash = fragment["hash"]

            try:
                recalculated_hash = simple_hash(data=fragment["data"])

            except Exception as e:
                raise Exception(f"Error: Failed to calculate hash for fragment {i}: {str(e)}")

            if fragment_hash != recalculated_hash:
                raise Exception("Data integrity verification failed.")

            # Append the fragment to the reconstructed data
            try:
                reconstructed_data += fragment["data"]
            except Exception as e:
                raise Exception(f"Error: Failed to append fragment {i} to reconstructed data: {str(e)}")

        return reconstructed_data

    except Exception as e:
        raise Exception(f"Error: An unexpected error occurred during data reconstruction: {str(e)}")


fragments = {
    1: {"data": "Hello", "hash": simple_hash(data="Hello")},
    2: {"data": "World", "hash": simple_hash(data="World")},
    3: {"data": "!", "hash": simple_hash(data="!")},
}

original_data = reconstruct_data(fragments)
print(f"Fragments data: {fragments}")
print(f"Original data: {original_data}")
