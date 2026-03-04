import os
from datetime import datetime

base_path = os.getcwd()

raw_path = os.path.join(base_path , "data" , "raw")
processed_path = os.path.join(base_path , "data" , "processed" )
log_path = os.path.join(base_path , "logs")

for path in [raw_path ,processed_path ,log_path] :
    if not os.path.exists(path):
        os.makedirs(path)

print("Folder creation Sucessfully!")

file_path = os.path.join(raw_path , "ganesh.txt")

if not os.path.exists(file_path):
    with open(file_path , "w") as f :
        f.write("Hello Ganesh How are you?")

print("file created : ", os.path.exists(file_path))

if os.path.exists(file_path):
    with open(file_path,"r" ) as f:
        content = f.read()
        print("file content is: " , content)


print("Current working dir is :")
print(os.getcwd())

print("list of dir :")
print(os.listdir())


def setup_project():
    base_path = os.getcwd()

    folders = [
        os.path.join(base_path, "data", "raw"),
        os.path.join(base_path, "data", "processed"),
        os.path.join(base_path, "logs")
    ]

    for folder in folders:
        if not os.path.isdir(folder):
            os.makedirs(folder)

    print(f"[{datetime.now()}] Folder creation successful!")

    file_path = os.path.join(base_path, "data", "raw", "ganesh.txt")

    if not os.path.isfile(file_path):
        with open(file_path, "w") as f:
            f.write("Hello Ganesh How are you?")

    print("File created:", os.path.exists(file_path))

    with open(file_path, "r") as f:
        print("File content:", f.read())

if __name__ == "__main__":
    setup_project()