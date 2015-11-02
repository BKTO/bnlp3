#-*- coding: utf-8 -*-
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
