import csv
import re

def wordprocess(word):
  copy = word
  word = re.sub(r"[^a-zA-Z ]+", "", word)
  word = re.sub(r"\s+", " ", word)
  word = word.lower()
  word = word.strip()
  return word



# Read the CSV file and write to the output file
with open("wiktionary-en.csv", "r", encoding="utf-8") as file, open("rare.txt", "w", encoding="utf-8") as output_file, open("stdfile.txt","r") as sfile:
    written_words = set(sfile.read().split())
    reader = csv.reader(file)
    for row in reader:
        word = row[0]
        word = wordprocess(word)
        if word:
          if word not in written_words : 
              if all(len(w) <= 10 for w in [w.strip() for w in word.split()]):
                output_file.write(word + "\n")
                written_words.add(word)

with open("slang.txt", "w", encoding="utf-8") as output_file, open("rare.txt", "r", encoding="utf-8") as rfile,  open("urbanDic.data", "r", encoding="utf-8") as file, open("stdfile.txt","r") as sfile:
    written_words = set(sfile.read().split()+rfile.read().split())
    for word in file:
        word = wordprocess(word)
        if word:
          if word not in written_words: 
              if all(len(w) <= 10 for w in [w.strip() for w in word.split()]) and len(word)<50:
                output_file.write(word + "\n")
                written_words.add(word)

