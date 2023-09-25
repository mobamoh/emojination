import os

def persist_to_file(content):
    os.makedirs("outputs",exist_ok=True)
    filename = os.path.join("outputs","land.txt")
    with open(filename,"w") as f:
        f.write(content)