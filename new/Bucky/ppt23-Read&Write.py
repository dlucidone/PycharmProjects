fw = open('sample.txt', 'w')
fw.write('this is sample text file\n')
fw.write('tutorial to read and write file')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()