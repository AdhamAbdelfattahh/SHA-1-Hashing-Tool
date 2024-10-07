import hashlib

def sha1_hash(message):
    """Generate a SHA-1 hash for the input message."""
    sha1 = hashlib.sha1()
    sha1.update(message.encode())
    return sha1.hexdigest()

def main():
    message = "Hello, World!"
    print(f"Original Message: {message}")

    # Generate SHA-1 hash
    hash_value = sha1_hash(message)
    print(f"SHA-1 Hash: {hash_value}")

if __name__ == "__main__":
    main()
