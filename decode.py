code = "5:1."

ciphertext = open("book.txt", "r")
for line in ciphertext:
    if code in line: print line
ciphertext.close()