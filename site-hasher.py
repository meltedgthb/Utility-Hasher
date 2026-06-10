import hashlib

def sha512_file(file_path: str, chunk_size: int = 8192) -> str:
    """
    Compute SHA-512 hash of a file without loading it entirely into memory.
    
    Args:
        file_path (str): Path to the file.
        chunk_size (int): Number of bytes to read at a time.
    
    Returns:
        str: Hexadecimal digest of the file's hash.
    """
    hash_obj = hashlib.sha512()
    
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(chunk_size):
                hash_obj.update(chunk)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied: {file_path}")
    
    return hash_obj.hexdigest()

if __name__ == "__main__":
    file_path = "Nautilus.mp3"
    try:
        print("HASH:", sha512_file(file_path))
    except Exception as e:
        print("Error:", e)
