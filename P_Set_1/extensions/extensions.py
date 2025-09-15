# Dictionary mapping file extensions to MIME types
formats = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

# Get input from the user, remove spaces, and convert to lowercase
file_name = input("File name: ").strip().lower()

# Split the filename by '.' to separate the name and the extension
file_format = file_name.split(".")

# Take the last part as the extension if it exists, otherwise empty string
ext = file_format[-1] if len(file_format) > 1 else ""

# Print corresponding MIME type or default if unknown/no extension
print(formats.get(ext, "application/octet-stream"))

# Mohammad_Reza_Mokhtari_Kia
