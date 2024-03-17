#!/usr/bin/python
import os, json, math

MAX_FILE_SIZE = 300 # units - KB
REL_TOL = 6e-04  # relative tolerance for floats
ABS_TOL = 15e-03  # absolute tolerance for floats

PASS = "PASS"

TEXT_FORMAT = "text"  # question type when expected answer is a str, int, float, or bool
TEXT_FORMAT_NAMEDTUPLE = "text namedtuple"  # question type when expected answer is a namedtuple
TEXT_FORMAT_UNORDERED_LIST = "text list_unordered"  # question type when the expected answer is a list where the order does *not* matter
TEXT_FORMAT_ORDERED_LIST = "text list_ordered"  # question type when the expected answer is a list where the order does matter
TEXT_FORMAT_ORDERED_LIST_NAMEDTUPLE = "text list_ordered namedtuple"  # question type when the expected answer is a list of namedtuples where the order does matter
TEXT_FORMAT_SPECIAL_ORDERED_LIST = "text list_special_ordered"  # question type when the expected answer is a list where order does matter, but with possible ties. Elements are ordered according to values in special_ordered_json (with ties allowed)
TEXT_FORMAT_DICT = "text dict"  # question type when the expected answer is a dictionary
TEXT_FORMAT_LIST_DICTS_ORDERED = "text list_dicts_ordered"  # question type when the expected answer is a list of dicts where the order does matter


expected_json =    {"1": (TEXT_FORMAT_DICT, {'tt0477348': 'No Country for Old Men',
                                             'tt1659337': 'The Perks of Being a Wallflower',
                                             'nm0154716': 'Stephen Chbosky',
                                             'nm0000169': 'Tommy Lee Jones',
                                             'nm0503567': 'Logan Lerman',
                                             'nm3009232': 'Ezra Miller',
                                             'nm0001054': 'Joel Coen',
                                             'nm0000437': 'Woody Harrelson',
                                             'nm0001053': 'Ethan Coen',
                                             'nm0000849': 'Javier Bardem',
                                             'nm0000982': 'Josh Brolin',
                                             'nm0748620': 'Paul Rudd',
                                             'nm0914612': 'Emma Watson'}),
                    "2": (TEXT_FORMAT, 'Logan Lerman'),
                    "3": (TEXT_FORMAT_UNORDERED_LIST, ['Stephen Chbosky',
                                                       'Tommy Lee Jones',
                                                       'Logan Lerman',
                                                       'Ezra Miller',
                                                       'Joel Coen',
                                                       'Woody Harrelson',
                                                       'Ethan Coen',
                                                       'Javier Bardem',
                                                       'Josh Brolin',
                                                       'Paul Rudd',
                                                       'Emma Watson']),
                    "4": (TEXT_FORMAT_UNORDERED_LIST,['nm0000169']),
                    "5": (TEXT_FORMAT_ORDERED_LIST, [{'title': 'tt0477348',
                                                            'year': 2007,
                                                            'duration': 122,
                                                            'genres': ['Crime', 'Drama', 'Thriller'],
                                                            'rating': 8.2,
                                                            'directors': ['nm0001053', 'nm0001054'],
                                                            'cast': ['nm0000169', 'nm0000849', 'nm0000982', 'nm0000437']},
                                                           {'title': 'tt1659337',
                                                            'year': 2012,
                                                            'duration': 103,
                                                            'genres': ['Drama'],
                                                            'rating': 7.9,
                                                            'directors': ['nm0154716'],
                                                            'cast': ['nm0503567', 'nm0914612', 'nm3009232', 'nm0748620']}]),
                    "6": (TEXT_FORMAT, 4),
                    "7": (TEXT_FORMAT, 'nm0000169'),
                    "8": (TEXT_FORMAT_ORDERED_LIST, [{'title': 'No Country for Old Men',
                                                      'year': 2007,
                                                      'duration': 122,
                                                      'genres': ['Crime', 'Drama', 'Thriller'],
                                                      'rating': 8.2,
                                                      'directors': ['Ethan Coen', 'Joel Coen'],
                                                      'cast': ['Tommy Lee Jones',
                                                       'Javier Bardem',
                                                       'Josh Brolin',
                                                       'Woody Harrelson']},
                                                     {'title': 'The Perks of Being a Wallflower',
                                                      'year': 2012,
                                                      'duration': 103,
                                                      'genres': ['Drama'],
                                                      'rating': 7.9,
                                                      'directors': ['Stephen Chbosky'],
                                                      'cast': ['Logan Lerman', 'Emma Watson', 'Ezra Miller', 'Paul Rudd']}]),
                    "9": (TEXT_FORMAT, 'The Perks of Being a Wallflower'),
                    "10": (TEXT_FORMAT_UNORDERED_LIST, ['Logan Lerman', 'Emma Watson', 'Ezra Miller', 'Paul Rudd']),
                    "11": (TEXT_FORMAT_UNORDERED_LIST, ['Stephen Chbosky']),
                    "12": (TEXT_FORMAT_ORDERED_LIST, [{'title': 'Dark Rider',
                                                          'year': 1991,
                                                          'duration': 94,
                                                          'genres': ['Action', 'Adventure', 'Crime'],
                                                          'rating': 5.6,
                                                          'directors': ['Bob Ivy'],
                                                          'cast': ['Joe Estevez', 'Doug Shanklin', 'Alicia Anne', 'Cloyde Howard']},
                                                         {'title': 'Izu no odoriko',
                                                          'year': 1967,
                                                          'duration': 85,
                                                          'genres': ['Drama'],
                                                          'rating': 8.4,
                                                          'directors': ['Hideo Onchi'],
                                                          'cast': ['Yôko Naitô',
                                                           'Toshio Kurosawa',
                                                           'Tatsuyoshi Ehara',
                                                           'Nobuko Otowa']},
                                                         {'title': 'Things Change',
                                                          'year': 1988,
                                                          'duration': 100,
                                                          'genres': ['Comedy', 'Crime', 'Drama'],
                                                          'rating': 7.0,
                                                          'directors': ['David Mamet'],
                                                          'cast': ['Don Ameche', 'Joe Mantegna', 'Robert Prosky', 'J.J. Johnston']},
                                                         {'title': 'Móvil pasional',
                                                          'year': 1994,
                                                          'duration': 98,
                                                          'genres': ['Thriller'],
                                                          'rating': 5.6,
                                                          'directors': ['Mauricio Walerstein'],
                                                          'cast': ['María Rojo', 'Orlando Urdaneta', 'Elvira Valdés', 'Hugo Márquez']},
                                                         {'title': 'Venky',
                                                          'year': 2004,
                                                          'duration': 162,
                                                          'genres': ['Action', 'Comedy', 'Mystery'],
                                                          'rating': 7.4,
                                                          'directors': ['Sreenu Vaitla', 'Gopimohan'],
                                                          'cast': ['Ravi Teja', 'Sneha', 'Ashutosh Rana', 'Srinivasa Reddy']},
                                                         {'title': 'Shooting Silvio',
                                                          'year': 2006,
                                                          'duration': 96,
                                                          'genres': ['Crime', 'Drama'],
                                                          'rating': 5.1,
                                                          'directors': ['Berardo Carboni'],
                                                          'cast': ['Federico Rosati',
                                                           'Sofia Vigliar',
                                                           'Alessandro Haber',
                                                           'Antonino Iuorio']},
                                                         {'title': 'Up the Mountain',
                                                          'year': 2019,
                                                          'duration': 105,
                                                          'genres': ['Adventure', 'Comedy', 'Drama'],
                                                          'rating': 5.8,
                                                          'directors': ['Sébastien Betbeder'],
                                                          'cast': ['William Lebghil',
                                                           'Izïa Higelin',
                                                           'Bastien Bouillon',
                                                           'Jérémie Elkaïm']},
                                                         {'title': 'The Last Adventurers',
                                                          'year': 1937,
                                                          'duration': 75,
                                                          'genres': ['Drama', 'Romance'],
                                                          'rating': 7.1,
                                                          'directors': ['Roy Kellino'],
                                                          'cast': ['Niall MacGinnis',
                                                           'Roy Emerton',
                                                           'Linden Travers',
                                                           'Peter Gawthorne']},
                                                         {'title': 'Handmade Cinema',
                                                          'year': 2012,
                                                          'duration': 52,
                                                          'genres': ['Documentary'],
                                                          'rating': 8.0,
                                                          'directors': ['Guido Torlonia'],
                                                          'cast': ['Chiara Mastroianni']},
                                                         {'title': 'The Crime',
                                                          'year': 2022,
                                                          'duration': 127,
                                                          'genres': ['Action', 'Crime', 'Thriller'],
                                                          'rating': 6.1,
                                                          'directors': ['Sharif Arafah', 'Mohamed Nasser Hamza'],
                                                          'cast': ['Ahmed Ezz',
                                                           'Menna Shalabi',
                                                           'Maged El-Kidwani',
                                                           'Haggag Abdulazim']}]),
                    "13": (TEXT_FORMAT, 507),
                    "14": (TEXT_FORMAT_ORDERED_LIST, [{'title': "Killer's Kiss",
                                                          'year': 1955,
                                                          'duration': 67,
                                                          'genres': ['Crime', 'Drama', 'Film-Noir'],
                                                          'rating': 6.6,
                                                          'directors': ['Stanley Kubrick'],
                                                          'cast': ['Frank Silvera', 'Irene Kane', 'Jamie Smith', 'Jerry Jarrett']},
                                                         {'title': 'Paths of Glory',
                                                          'year': 1957,
                                                          'duration': 88,
                                                          'genres': ['Drama', 'War'],
                                                          'rating': 8.4,
                                                          'directors': ['Stanley Kubrick'],
                                                          'cast': ['Kirk Douglas',
                                                           'Ralph Meeker',
                                                           'Adolphe Menjou',
                                                           'George Macready']},
                                                         {'title': 'Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb',
                                                          'year': 1964,
                                                          'duration': 95,
                                                          'genres': ['Comedy', 'War'],
                                                          'rating': 8.4,
                                                          'directors': ['Stanley Kubrick'],
                                                          'cast': ['Peter Sellers',
                                                           'George C. Scott',
                                                           'Sterling Hayden',
                                                           'Keenan Wynn']},
                                                         {'title': '2001: A Space Odyssey',
                                                          'year': 1968,
                                                          'duration': 149,
                                                          'genres': ['Adventure', 'Sci-Fi'],
                                                          'rating': 8.3,
                                                          'directors': ['Stanley Kubrick'],
                                                          'cast': ['Keir Dullea',
                                                           'Gary Lockwood',
                                                           'William Sylvester',
                                                           'Daniel Richter']},
                                                         {'title': 'Fear and Desire',
                                                          'year': 1953,
                                                          'duration': 62,
                                                          'genres': ['Drama', 'Thriller', 'War'],
                                                          'rating': 5.4,
                                                          'directors': ['Stanley Kubrick'],
                                                          'cast': ['Frank Silvera', 'Kenneth Harp', 'Paul Mazursky', 'Stephen Coit']},
                                                         {'title': 'The Killing',
                                                          'year': 1956,
                                                          'duration': 84,
                                                          'genres': ['Crime', 'Drama', 'Film-Noir'],
                                                          'rating': 8.0,
                                                          'directors': ['Stanley Kubrick'],
                                                          'cast': ['Sterling Hayden',
                                                           'Coleen Gray',
                                                           'Vince Edwards',
                                                           'Jay C. Flippen']},
                                                         {'title': 'Barry Lyndon',
                                                          'year': 1975,
                                                          'duration': 185,
                                                          'genres': ['Adventure', 'Drama', 'War'],
                                                          'rating': 8.1,
                                                          'directors': ['Stanley Kubrick'],
                                                          'cast': ["Ryan O'Neal", 'Marisa Berenson', 'Patrick Magee', 'Hardy Krüger']},
                                                         {'title': 'Full Metal Jacket',
                                                          'year': 1987,
                                                          'duration': 116,
                                                          'genres': ['Drama', 'War'],
                                                          'rating': 8.3,
                                                          'directors': ['Stanley Kubrick'],
                                                          'cast': ['Matthew Modine',
                                                           'R. Lee Ermey',
                                                           "Vincent D'Onofrio",
                                                           'Adam Baldwin']},
                                                         {'title': 'Eyes Wide Shut',
                                                          'year': 1999,
                                                          'duration': 159,
                                                          'genres': ['Drama', 'Mystery', 'Thriller'],
                                                          'rating': 7.5,
                                                          'directors': ['Stanley Kubrick'],
                                                          'cast': ['Tom Cruise', 'Nicole Kidman', 'Todd Field', 'Sydney Pollack']},
                                                         {'title': 'Spartacus',
                                                          'year': 1960,
                                                          'duration': 197,
                                                          'genres': ['Adventure', 'Biography', 'Drama'],
                                                          'rating': 7.9,
                                                          'directors': ['Stanley Kubrick'],
                                                          'cast': ['Kirk Douglas',
                                                           'Laurence Olivier',
                                                           'Jean Simmons',
                                                           'Charles Laughton']},
                                                         {'title': 'The Shining',
                                                          'year': 1980,
                                                          'duration': 146,
                                                          'genres': ['Drama', 'Horror'],
                                                          'rating': 8.4,
                                                          'directors': ['Stanley Kubrick'],
                                                          'cast': ['Jack Nicholson',
                                                           'Shelley Duvall',
                                                           'Danny Lloyd',
                                                           'Scatman Crothers']},
                                                         {'title': 'A Clockwork Orange',
                                                          'year': 1971,
                                                          'duration': 136,
                                                          'genres': ['Crime', 'Sci-Fi'],
                                                          'rating': 8.3,
                                                          'directors': ['Stanley Kubrick'],
                                                          'cast': ['Malcolm McDowell',
                                                           'Patrick Magee',
                                                           'Michael Bates',
                                                           'Warren Clarke']}]),
                    "15": (TEXT_FORMAT_ORDERED_LIST, [{'title': 'Wisconsin Death Trip',
                                                          'year': 1999,
                                                          'duration': 76,
                                                          'genres': ['Biography', 'Crime', 'Drama'],
                                                          'rating': 6.6,
                                                          'directors': ['James Marsh'],
                                                          'cast': ['Ian Holm', 'Jeffrey Golden', 'Jo Vukelich', 'Marcus Monroe']},
                                                         {'title': 'Small Town Wisconsin',
                                                          'year': 2020,
                                                          'duration': 109,
                                                          'genres': ['Comedy', 'Drama'],
                                                          'rating': 7.2,
                                                          'directors': ['Niels Mueller'],
                                                          'cast': ['David Sullivan',
                                                           'Bill Heck',
                                                           'Kristen Johnston',
                                                           'Cooper J. Friedman']},
                                                         {'title': 'Bootleg Wisconsin',
                                                          'year': 2008,
                                                          'duration': 73,
                                                          'genres': ['Drama'],
                                                          'rating': 7.7,
                                                          'directors': ['Brandon Linden'],
                                                          'cast': ['Lepolion Henderson',
                                                           'Angela Harris',
                                                           'Alissa Bailey',
                                                           'Joyce Porter']},
                                                         {'title': 'Wisconsin Supper Clubs: An Old Fashioned Experience',
                                                          'year': 2011,
                                                          'duration': 55,
                                                          'genres': ['Documentary', 'History'],
                                                          'rating': 6.7,
                                                          'directors': ['Ron Faiola'],
                                                          'cast': ['Bun E. Carlos']}]),
                    "16": (TEXT_FORMAT, 26),
                    "17": (TEXT_FORMAT, 3031),
                    "18": (TEXT_FORMAT_ORDERED_LIST, ['Sunset Blvd.',
                                                      'Double Indemnity',
                                                      'Rebecca',
                                                      'The Third Man',
                                                      'I Am a Fugitive from a Chain Gang']),
                    "19": (TEXT_FORMAT, 'Drama'),
                    "20": (TEXT_FORMAT_UNORDERED_LIST, ['Nicolas James', 'Bhaskhar Maurya', 'Lachlan Mlinaric', 'Russell Stanley'])}

def check_cell(qnum, actual):
    format, expected = expected_json[qnum[1:]]
    try:
        if format == TEXT_FORMAT:
            return simple_compare(expected, actual)
        elif format == TEXT_FORMAT_UNORDERED_LIST:
            return list_compare_unordered(expected, actual)
        elif format == TEXT_FORMAT_ORDERED_LIST:
            return list_compare_ordered(expected, actual)
        elif format == TEXT_FORMAT_DICT:
            return dict_compare(expected, actual)
        else:
            if expected != actual:
                return "expected %s but found %s " % (repr(expected), repr(actual))
    except:
        if expected != actual:
            return "expected %s" % (repr(expected))
    return PASS


def simple_compare(expected, actual, complete_msg=True):
    msg = PASS
    if type(expected) == type:
        if expected != actual:
            if type(actual) == type:
                msg = "expected %s but found %s" % (expected.__name__, actual.__name__)
            else:
                msg = "expected %s but found %s" % (expected.__name__, repr(actual))
    elif type(expected) != type(actual) and not (type(expected) in [float, int] and type(actual) in [float, int]):
        msg = "expected to find type %s but found type %s" % (type(expected).__name__, type(actual).__name__)
    elif type(expected) == float:
        if not math.isclose(actual, expected, rel_tol=REL_TOL, abs_tol=ABS_TOL):
            msg = "expected %s" % (repr(expected))
            if complete_msg:
                msg = msg + " but found %s" % (repr(actual))
    else:
        if expected != actual:
            msg = "expected %s" % (repr(expected))
            if complete_msg:
                msg = msg + " but found %s" % (repr(actual))
    return msg

def namedtuple_compare(expected, actual):
    msg = PASS
    for field in expected._fields:
        val = simple_compare(getattr(expected, field), getattr(actual, field))
        if val != PASS:
            msg = "at attribute %s of namedtuple %s, " % (field, type(expected).__name__) + val
            return msg
    return msg


def list_compare_ordered(expected, actual, obj="list"):
    msg = PASS
    if type(expected) != type(actual):
        msg = "expected to find type %s but found type %s" % (type(expected).__name__, type(actual).__name__)
        return msg
    for i in range(len(expected)):
        if i >= len(actual):
            msg = "expected missing %s in %s" % (repr(expected[i]), obj)
            break
        if type(expected[i]) in [int, float, bool, str]:
            val = simple_compare(expected[i], actual[i])
        elif type(expected[i]) in [list]:
            val = list_compare_ordered(expected[i], actual[i], "sub" + obj)
        elif type(expected[i]) in [dict]:
            val = dict_compare(expected[i], actual[i])
        elif type(expected[i]).__name__ == obfuscate1():
            val = simple_compare(expected[i], actual[i])
        if val != PASS:
            msg = "at index %d of the %s, " % (i, obj) + val
            break
    if len(actual) > len(expected) and msg == PASS:
        msg = "found unexpected %s in %s" % (repr(actual[len(expected)]), obj)
    if len(expected) != len(actual):
        msg = msg + " (found %d entries in %s, but expected %d)" % (len(actual), obj, len(expected))

    if len(expected) > 0 and type(expected[0]) in [int, float, bool, str]:
        if msg != PASS and list_compare_unordered(expected, actual, obj) == PASS:
            try:
                msg = msg + " (list may not be ordered as required)"
            except:
                pass
    return msg


def list_compare_helper(larger, smaller):
    msg = PASS
    j = 0
    for i in range(len(larger)):
        if i == len(smaller):
            msg = "expected %s" % (repr(larger[i]))
            break
        found = False
        while not found:
            if j == len(smaller):
                val = simple_compare(larger[i], smaller[j - 1], False)
                break
            val = simple_compare(larger[i], smaller[j], False)
            j += 1
            if val == PASS:
                found = True
                break
        if not found:
            msg = val
            break
    return msg


def list_compare_unordered(expected, actual, obj="list"):
    msg = PASS
    if type(expected) != type(actual):
        msg = "expected to find type %s but found type %s" % (type(expected).__name__, type(actual).__name__)
        return msg
    try:
        sort_expected = sorted(expected)
        sort_actual = sorted(actual)
    except:
        msg = "unexpected datatype found in %s; expected entries of type %s" % (obj, obj, type(expected[0]).__name__)
        return msg

    if len(actual) == 0 and len(expected) > 0:
        msg = "in the %s, missing" % (obj) + expected[0]
    elif len(actual) > 0 and len(expected) > 0:
        val = simple_compare(sort_expected[0], sort_actual[0])
        if val.startswith("expected to find type"):
            msg = "in the %s, " % (obj) + simple_compare(sort_expected[0], sort_actual[0])
        else:
            if len(expected) > len(actual):
                msg = "in the %s, missing " % (obj) + list_compare_helper(sort_expected, sort_actual)
            elif len(expected) < len(actual):
                msg = "in the %s, found un" % (obj) + list_compare_helper(sort_actual, sort_expected)
            if len(expected) != len(actual):
                msg = msg + " (found %d entries in %s, but expected %d)" % (len(actual), obj, len(expected))
                return msg
            else:
                val = list_compare_helper(sort_expected, sort_actual)
                if val != PASS:
                    msg = "in the %s, missing " % (obj) + val + ", but found un" + list_compare_helper(sort_actual,
                                                                                               sort_expected)
    return msg

def list_compare_special_init(expected, special_order):
    real_expected = []
    for i in range(len(expected)):
        if real_expected == [] or special_order[i-1] != special_order[i]:
            real_expected.append([])
        real_expected[-1].append(expected[i])
    return real_expected


def list_compare_special(expected, actual, special_order):
    expected = list_compare_special_init(expected, special_order)
    msg = PASS
    expected_list = []
    for expected_item in expected:
        expected_list.extend(expected_item)
    val = list_compare_unordered(expected_list, actual)
    if val != PASS:
        msg = val
    else:
        i = 0
        for expected_item in expected:
            j = len(expected_item)
            actual_item = actual[i: i + j]
            val = list_compare_unordered(expected_item, actual_item)
            if val != PASS:
                if j == 1:
                    msg = "at index %d " % (i) + val
                else:
                    msg = "between indices %d and %d " % (i, i + j - 1) + val
                msg = msg + " (list may not be ordered as required)"
                break
            i += j

    return msg


def dict_compare(expected, actual, obj="dict"):
    msg = PASS
    if type(expected) != type(actual):
        msg = "expected to find type %s but found type %s" % (type(expected).__name__, type(actual).__name__)
        return msg
    try:
        expected_keys = sorted(list(expected.keys()))
        actual_keys = sorted(list(actual.keys()))
    except:
        msg = "unexpected datatype found in keys of dict; expect a dict with keys of type %s" % (
            type(expected_keys[0]).__name__)
        return msg
    val = list_compare_unordered(expected_keys, actual_keys, "dict")
    if val != PASS:
        msg = "bad keys in %s: " % (obj) + val
    if msg == PASS:
        for key in expected:
            if expected[key] == None or type(expected[key]) in [int, float, bool, str]:
                val = simple_compare(expected[key], actual[key])
            elif type(expected[key]) in [list]:
                val = list_compare_ordered(expected[key], actual[key], "value")
            elif type(expected[key]) in [dict]:
                val = dict_compare(expected[key], actual[key], "sub" + obj)
            if val != PASS:
                msg = "incorrect val for key %s in %s: " % (repr(key), obj) + val
    return msg


def check(qnum, actual):
    msg = check_cell(qnum, actual)
    if msg == PASS:
        return True
    print("<b style='color: red;'>ERROR:</b> " + msg)

def check_file_size(path):
    size = os.path.getsize(path)
    assert size < MAX_FILE_SIZE * 10**3, "Your file is too big to be processed by Gradescope; please delete unnecessary output cells so your file size is < %s KB" % MAX_FILE_SIZE
