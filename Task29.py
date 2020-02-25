def replace():
    word = input("")
    words = word.replace(".", "").replace(",", "").replace("?", "").replace("!", "").replace(";","").replace(":","")
    print(words)
replace()