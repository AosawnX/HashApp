import hashlib

def hash_text(input_text,algorithm="sha256"):
    hasher = hashlib.new(algorithm)
    hasher.update(input_text.encode("utf-8"))
    return hasher.hexdigest()


def hash_file(file_path,algorithm="sha256"):
    hasher = hashlib.new(algorithm)
    with open(file_path,"rb") as file:
        while chunk := file.read(8192):
            hasher.update(chunk)
            
    return hasher.hexdigest()
