# -*- coding: utf-8 -*-
import os
from os.path import abspath, dirname, isfile
from re import findall, IGNORECASE, MULTILINE, sub, UNICODE
from re import compile as re_compile
from titlecase import titlecase

global stopwords
stopwords = None

global org_regex
org_regex = None

global orgRegex
orgRegex = None

global soup_regex
soup_regex = None

global keywords
keywords = None

filepath = dirname(abspath(__file__))

def loadOrgKeywordsIfNecessary():
    global keywords
    if not keywords:
        with open(filepath + "/data/keywords/orgs.txt") as f:
            keywords = [k for k in f.read().split('\n') if k]
            keywords = sorted(keywords, key=lambda x: -1*len(x))
            print "keywords are", keywords

# returns a version of the name with org keywords removed
# e.g., University of Alabama will return Alabama
def trimOrgName(name):
    global keywords
    loadOrgKeywordsIfNecessary()

    for keyword in keywords:
        name = name.replace(keyword,"").replace("  "," ").strip()
    name = sub(r"( wal-|al-|')$", "", name, IGNORECASE)
    name = sub(r"^(of|the) ", "", name, IGNORECASE)
    name = sub(r"^(of|the) ", "", name, IGNORECASE)
    name = name.replace("  "," ").strip()
    return name
 
def createOrgRegexIfNecessary():
    global keywords
    loadOrgKeywordsIfNecessary()

    global org_regex
    if not org_regex:

        keyword_pattern = u"(?:" + u"|".join(keywords) + ")"

        titled_pattern = u"(?:\d*(?:st|nd|th)[ ])?(?:al-|ash-|ath-)?[A-Z][a-z(a'|'a)]{2,}(?:(?: |-i-)(?:al-|ash-|ath-|bin |of |of the |wal-|wa-)?[A-Z][a-z('a|a')]{2,})*"
        org_regex = re_compile(u"((?:"+titled_pattern+" )*" + keyword_pattern + "(?: "+titled_pattern+")*)")

def xGetOrgsFromText(text):
    global keywords
    loadOrgKeywordsIfNecessary()

    global orgRegex
    if not orgRegex:
        citation = u"(?: ?\[\d{1,3}\] ?)*"
        keyword = u"(?:" + u"|".join(keywords) + ")"
        seperator = u"(?:, |,|\u200E|\u200E | \u200E| \u200E | or |;|; ){1,3}"

        # accept a as uppercase because sometimes used in acronymns such as Jash al-... Ja...
        u = u"[^\W\d_b-z:]"
        l = u"(?:[^\W\d_A-Z:]|')"
        acronym = u+'{2,}'
        titled = u"(?:\d+(?:st|nd|th)[ ])?(?:al-|ash-|ath-|bin |of |of the |wal-|wa-)?" + u + l + "{2,}(?:(?: |-i-)(?:al-|ash-|ath-|bin |of |of the |wal-|wa-)?"+u+l+"{2,})*"
        alias = u"(?:(?:"+u+l+"{3,}: ?|meaning\")?" + "("+titled+")" + "|" + '('+acronym+')' +  ")"
        name = u"((?:"+titled+" )*" + keyword + "(?: "+titled+")*)" + citation
        aliases = "(?: ?\(" + alias + "(?: ?" + seperator + alias + ")*" + ")*"
        org = name + "(?: or " + name + ")?" + aliases
        #orgRegex = re_compile(org, MULTILINE|UNICODE)

    if isinstance(text, str):
        text = text.decode("utf-8")

#    return findall(orgRegex, text)
    return findall(org, text, UNICODE)
xg = xGetOrgsFromText
    
def createSoupRegexIfNecessary():
    global keywords
    loadOrgKeywordsIfNecessary()

    global soup_regex
    if not soup_regex:

        keyword_pattern = u"(?:" + u"|".join(keywords) + ")"

        titled_pattern = u"(?:\d*(?:st|nd|th)[ ])?(?:al-|ash-|ath-)?[A-Z][a-z(a'|'a)]{2,}(?:(?: |-i-)(?:al-|ash-|ath-|bin |of |of the |wal-|wa-)?[A-Z][a-z('a|a')]{2,})*"
        soup_regex = re_compile(u"^((?:"+titled_pattern+" )*" + keyword_pattern + "(?: "+titled_pattern+")*)$")
 

def getOrgsFromSoup(soup):
    global soup_regex
    createSoupRegexIfNecessary()

    try:
        print 'starting getOrgsFromSoup'
#        for elem in soup(text=org_regex):
#            print "    ", elem
        return soup.find_all('a', text=soup_regex)

    except Exception as e:
        print e

def loadStopWordsIfNecessary():
    global stopwords
    if not stopwords:
        filepath = os.path.dirname(os.path.abspath(__file__))
        if isfile(filepath):
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
