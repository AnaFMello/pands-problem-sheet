with open("mytext.txt", "r") as file:
    text = file.read()
    count = 0
    for char in text:
        word = char
        if char == "e":
            count += 1

    print(count)