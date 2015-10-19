#-*- coding: utf-8 -*-

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

#alif
char_variations[u'\u0627'] = [u'a']

#alif hamza
char_variations[u'\u0623'] = [u'a']

#alif hamza with hamza at bottom
char_variations[u'\u0625'] = [u'i']

# ha'
char_variations[u'\u062d'] = [u'h',u'ha']

#ra
char_variations[u'\u0631'] = [u'r',u'ra']

#sin
char_variations[u'\u0633'] = [u's']

#shin connected
char_variations[u'\u0634'] = [u'sh']

#sad
char_variations[u'\u0635'] = [u's']

#kaf
char_variations[u'\u0643'] = [u'k']

#mim solo
char_variations[u'\u0645'] = [u'm']

#nun
char_variations[u'\u0646'] = [u'n']

#tar ma-buta
char_variations[u'\u0629'] = [u'a',u'at']

# ya, said ee
char_variations[u'\u064a'] = [u'y',u'i',u'iyy']

def get_variations(string):

    if isinstance(string, str):
        string = string.decode('utf-8')

    current_variations = ['']
    length = len(string)
    for index, (prev_char, current_char, next_char) in enumerate(neighborhood(string)):

        print "for", index, [current_char]
        new_variations = []
        #print "    current_variations are", current_variations 

        #if char == lam
        if current_char == u'\u0644':
            print "    current_char is lam"
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
                   
        elif current_char in char_variations:
            additions = char_variations[current_char]

        else:
            additions = [current_char]


        for variation in current_variations:
            for addition in additions:
                new_variations.append(variation+addition)


        current_variations = new_variations
#        print "current_variations set to", current_variations

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
