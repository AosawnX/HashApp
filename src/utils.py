import os
import mimetypes

MAX_FILE_SIZE_MB = 50  

def validate_file(file_path):
    """Validate that a file exists and is within size limits."""
    if not os.path.exists(file_path):
        return False
    if os.path.getsize(file_path) > MAX_FILE_SIZE_MB * 1024 * 1024:
        return False
    return True

def get_file_type(file_path):
    """Determine the file type based on the MIME type."""
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type:
        if mime_type.startswith("image"):
            return "image"
        elif mime_type.startswith("video"):
            return "video"
    return "unknown"
