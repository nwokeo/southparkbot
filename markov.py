from smarkov import Markov
from glob import glob
import random
import markovify # https://github.com/jsvine/markovify

allwords = []

files = glob('SouthParkData/Season*.csv')
with open(files[random.randrange(len(files))]) as infile:
    for line in infile:
        words = line[line.find('"'):].replace('\n', '').replace('"', '').split(' ')
        if words != ['']:
            allwords.append(words)

with open(files[random.randrange(len(files))]) as infile:
    text = infile.read()

chain = Markov(allwords)
print(" ".join(chain.generate_text()))

text_model = markovify.Text(text)
for i in range(5):
    print(text_model.make_sentence())
