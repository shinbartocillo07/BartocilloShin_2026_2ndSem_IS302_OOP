try:
    with open("data.txt", "r") as file:
        content_SGB = file.read()
        print(content_SGB)
except FileNotFoundError:
    print("File does not exist")
finally:
    print("Finished file read attempt.")
