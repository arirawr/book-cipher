# Open the cipher text and find the appropriate line
ciphertext = open("book.txt", "r")
code = open("code.txt", "r")

for line in code:
  linecode = line.split()[0] + ":" + line.split()[1]
  wordcode = line.split()[2]

  for line in ciphertext:
      if linecode in line:
        print line.split()[int(wordcode)]
        
code.close()
ciphertext.close()