def getAverageCharacterNumber(text):
    return numpy.mean([ord(random.choice(text)) for n in range(100)])

def isEnglish(text):
    return getAverageCharacterNumber(text) < 100
