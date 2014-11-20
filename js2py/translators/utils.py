import sys
import unicodedata
from collections import defaultdict

def is_lval(t):
    """Does not chceck whether t is not resticted or internal"""
    if not t:
        return False
    i = iter(t)
    if i.next() not in IDENTIFIER_START:
        return False
    return all(e in IDENTIFIER_PART for e in i)

def is_valid_lval(t):
    """Checks whether t is valid JS identifier name (no keyword like var, function, if etc)
    Also returns false on internal"""
    if not is_internal(t) and is_lval(t) and t not in RESERVED_NAMES:
        return True
    return False


def is_plval(t):
    return t.startswith('PyJsLval')

def is_marker(t):
    return t.startswith('PyJsMarker') or t.startswith('PyJsConstant')

def is_internal(t):
    return is_plval(t) or is_marker(t) or t=='var' # var is a scope var

def is_property_accessor(t):
    return '[' in t or '.' in t





#http://stackoverflow.com/questions/14245893/efficiently-list-all-characters-in-a-given-unicode-category
U_CATEGORIES = defaultdict(list)  # Thank you Martijn Pieters!
for c in map(unichr, range(sys.maxunicode + 1)):
    U_CATEGORIES[unicodedata.category(c)].append(c)

UNICODE_LETTER = set(U_CATEGORIES['Lu']+U_CATEGORIES['Ll']+
                     U_CATEGORIES['Lt']+U_CATEGORIES['Lm']+
                     U_CATEGORIES['Lo']+U_CATEGORIES['Nl'])
UNICODE_COMBINING_MARK = set(U_CATEGORIES['Mn']+U_CATEGORIES['Mc'])
UNICODE_DIGIT = set(U_CATEGORIES['Nd'])
UNICODE_CONNECTOR_PUNCTUATION = set(U_CATEGORIES['Pc'])
IDENTIFIER_START = UNICODE_LETTER.union({'$','_'}) # and some fucking unicode escape sequence
IDENTIFIER_PART = IDENTIFIER_START.union(UNICODE_COMBINING_MARK).union(UNICODE_DIGIT).union(UNICODE_CONNECTOR_PUNCTUATION)

RESERVED_NAMES = {'var', 'function', 'if', 'this', 'for', 'in'} #todo complete this list