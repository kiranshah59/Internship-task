def count_words(filename):
    try:
        file = open(filename, "r")
        text = file.read()
        words = text.split()
        print("Total words:", len(words))
        file.close()
    except:
        print("File not found")

name = input("Enter file name: ")
count_words(name)