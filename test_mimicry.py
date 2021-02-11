import Mimicry

fileName = "text_dumps/debate.txt"
groupLength = 5
numberOfSentences = 10

y=Mimicry.mimic(fileName, numberOfSentences, groupLength)
print(y)
