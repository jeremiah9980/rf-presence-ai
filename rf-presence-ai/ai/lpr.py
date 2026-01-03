def hash_plate(text):
    import hashlib
    return hashlib.sha256(text.encode()).hexdigest()
