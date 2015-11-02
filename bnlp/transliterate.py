#-*- coding: utf-8 -*-
from sys import exit

# returns previous, item, next
def neighborhood(iterable):
    iterator = iter(iterable)
    prev = None
    item = iterator.next()
    for next in iterator:
        yield (prev,item,next)
        prev = item
        item = next
    yield (prev,item,None)


char_variations = {}

#tha, ha, ba, sin, ra, qaf, lam, nun
consonants_ar = [u'\u062b', u'\u062d', u'\u0628', u'\u0633',u'\u0631', u'\u0642', u'\u0644', u'\u0646']

#alif, wa, ya
vowels_ar = [u'\u0627',u'\u0648',u'\u064a']

#consonants_en = ['b','c','d','f','g','h','

#blank space
char_variations[u' '] = [u'',' ']

#alif
char_variations[u'\u0627'] = [u'a',u'o']

#alif hamza
char_variations[u'\u0623'] = [u'a']

#alif hamza with hamza at bottom
char_variations[u'\u0625'] = [u'i']

#ba
char_variations[u'\u0628'] = ['b']

# ta
char_variations[u'\u062a'] = [u't']

# tha
char_variations[u'\u062b'] = [u'th']

#ja/ga
char_variations[u'\u062c'] = ['j','g','ja','ga']

# ha'
char_variations[u'\u062d'] = [u'h',u'ha',u'he']

# dal
char_variations[u'\u062f'] = [u'd']

# ghayn
char_variations[u'\u063a'] = [u'gh']

#ra
char_variations[u'\u0631'] = [u'r',u'ra']

# za
char_variations[u'\u0632'] = [u'z',u'zz']

#sin
char_variations[u'\u0633'] = [u's','sa']

#shin connected
char_variations[u'\u0634'] = [u'sh',u'shu',u'sha']

#sad
char_variations[u'\u0635'] = [u's',u'sa']

#deep ta
char_variations[u'\u0637'] = [u't',u'ta']

# ayn
char_variations[u'\u0639'] = [u'3',u'a',u'']

# fa
char_variations[u'\u0641'] = [u'f',u'fa']

#qaf
char_variations[u'\u0642'] = [u'q',u'qu']

#kaf
char_variations[u'\u0643'] = [u'k',u'ka']

##lam
char_variations[u'\u0644'] = [u'l',u'l-',u'l ',u's',u's-',u's ',u'sh',u'sh-','sh ',u't',u't-',u't ',u'th',u'th-',u'th ','la',u'li']

#mim solo
char_variations[u'\u0645'] = ['m','ma','mu']

#nun
char_variations[u'\u0646'] = [u'n', u'na']

#tar ma-buta
char_variations[u'\u0629'] = [u'a',u'at']

#light ha/he
char_variations[u'\u0647'] = ['','h','ha','he']

#wa
char_variations[u'\u0648'] = [u'u',u'o','w','wa']

# ya, said ee
char_variations[u'\u064a'] = [u'y',u'i',u'iyy',u'yyi','ee']

#hamza solo
char_variations[u'\u0621'] = [u""]

#hamza on ya
char_variations[u'\u0626'] = ['i',"'i"]

#left-to-right mark
char_variations[u'\u200e'] = ['']

char_pattern = {}
for char, variations in char_variations.iteritems():
    char_pattern[char] = '(' + '|'.join(sorted(variations, key=lambda x: -1*len(x))) + ')'

def get_variations_as_pattern(string):
    print '\nstarting get_variations_as_pattern with', string

    if isinstance(string, str):
        string = string.decode("utf-8")

    pattern_as_string = ''
    for index, char in enumerate(string):
#        print "for index", index, "and char", [char]

        if char in char_variations:
            pattern_as_string += '(' + '|'.join(char_variations[char]) + ')'
        else:
            pattern_as_string += char
    return pattern_as_string

v = get_variations_as_pattern


def get_variations(string):
    print '\nstarting get_variations with', [string]

    if isinstance(string, str):
        string = string.decode('utf-8')

    current_variations = ['']
    length = len(string)
    for index, (prev_char, current_char, next_char) in enumerate(neighborhood(string)):
        if len(current_variations) > 50000:
            #print "    current_variations are", current_variations 
            #exit()
            return None

        new_variations = []

        #if char == lam
        if current_char == u'\u0644':
        #        #basically ^al or spaceal
            if prev_char == u'\u0627': #a, so al
                if next_char == u'\u0633': #sin or s
                    additions = [u'l',u'l-',u'l ',u's',u's-',u's ']
                elif next_char == u'\u0634': #shin
                    additions = [u'l',u'l-',u'l ',u'sh',u'sh-',u'sh ']
                else:
                    additions = [u'l',u'l-',u'l ']
            else:
                additions = [u'l']

        # ya
        elif current_char == u'\u064a':
            if next_char == ' ': # at end of word
                additions = [u'i']
            else:
                additions = char_variations[current_char]

        #if char == wa
        elif current_char == u'\u0648':
            if prev_char in consonants_ar and next_char in consonants_ar:
                #if surrounded by consonants, probably gonna be used as a vowel
                additions = [u'u', u'o', u'oo']
            elif next_char in vowels_ar:
                additions = [u'w']
            else:
                additions = [u'u',u'o',u'oo','w','wa']

                   
        elif current_char in char_variations:
            additions = char_variations[current_char]

        else:
            additions = [current_char]


        for variation in current_variations:
            for addition in additions:
                new_variations.append(variation+addition)


        current_variations = new_variations
    
    print "returning", current_variations[:20]
    return current_variations
                


buck2uni = {"'":"ء", "|":"آ", "?":"أ", "&":"ؤ", "<":"إ", "}":"ئ", "A":"ا", "b":"ب", "p":"ة", "t":"ت", "v":"ث", "g":"ج", "H":"ح", "x":"خ", "d":"د", "*":"ذ", "r":"ر", "z":"ز", "s":"س", "$":"ش", "S":"ص", "D":"ض", "T":"ط", "Z":"ظ", "E":"ع", "G":"غ", "_":"ـ", "f":"ف", "q":"ق", "k":"ك", "l":"ل", "m":"م", "n":"ن", "h":"ه", "w":"و", "Y":"ى", "y":"ي", "F":"ً", "N":"ٌ", "K":"ٍ", "~":"ّ", "o":"ْ", "u":"ُ", "a":"َ", "i":"ِ"}    


def transString(string, reverse=0):
    '''Given a Unicode string, transliterate into Buckwalter. To go from
    Buckwalter back to Unicode, set reverse=1'''

    if not reverse:     
        for k,v in buck2uni.iteritems():
            string = string.replace(v.decode('utf-8'),k.decode('utf-8'))

    else:     
        for k,v in buck2uni.iteritems():
            string = string.replace(k.decode('utf-8'),v.decode('utf-8'))

    return string
