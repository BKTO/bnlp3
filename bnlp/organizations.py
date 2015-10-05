import os
from titlecase import titlecase

global stopwords
stopwords = None

def loadStopWordsIfNecessary():
    global stopwords
    if not stopwords:
        filepath = os.path.dirname(os.path.abspath(__file__))
        with open(filepath + "/data/stopwords/orgs.txt", "r") as f:
            stopwords = [line.strip() for line in f if line]

def isOrganization(text):
    global stopwords
    loadStopWordsIfNecessary() 


    text = text.lower()

    if text.count(" ") == 0:
        return False
    if text in stopwords:
        return False
    if text.startswith("congressman"):
        return False
    if text.endswith("for"):
        return False
    if text.startswith("commander"):
        return False

    for wordphrase in ("foundation Donor", "unites", "donors", "guards", "councilman", "pgp public key block"):
        if wordphrase in text:
            return False

    for word in ("army", "assembly", "battalion", "bloc", "brigade", "brotherhood", "bureau", "church", "clan", "coalition", "commission", "committee", "community", "companies", "congress", "corps", "council", "department", "division", "force", "foundation", "front", "government", "group", "guard", "haraka", "hezb", "hizb", "house", "institute", "jabhat", "jaish", "jaysh", "legion", "liwa", "ministry", "movement", "office", "org", "organization", "parliament", "party", "rally", "senate", "supporters", "squadron", "unit", "union", "university"):
        if word in text:
            return True

    return False

def isAmbiguousOrg(text):
    #print "starting isAmbiguousOrg with", text
    text = titlecase(text)
    return any(word == text or "The " + word == text for word in ["Army", "Assembly", "Battalion", "Bloc", "Brigade", "Brotherhood", "Bureau", "Church", "Coalition", "Commission", "Committee", "Community", "Council", "Department", "Force", "Foundation", "Front", "Government", "Group", "Haraka", "Hezb", "Hizb", "House", "Institute", "Ministry", "Movement", "Office", "Org", "Organization", "Parliament", "Party", "Rally", "Senate", "Congress", "Unit", "Union", "University"])
