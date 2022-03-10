# extract 5 letter words from words.txt and save as 5letter_dict.txt

with open('words.txt', 'r') as file:
    f = open('5letter_dict.txt', 'w')
    lines = file.readlines()
    for word in lines:
        word = word.strip().upper()
        if len(word) == 5:
            f.write(word+'\n')
    f.close()