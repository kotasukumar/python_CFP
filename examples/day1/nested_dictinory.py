import os

try:
    os.makedirs("/dirA/diro")
    print("created successfully", os.path)
except FileExistsError:
    print("File already exists")