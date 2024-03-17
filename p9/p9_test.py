#!/usr/bin/python
import os
import json
import math

MAX_FILE_SIZE = 500 # units - KB
REL_TOL = 6e-04  # relative tolerance for floats
ABS_TOL = 15e-03  # absolute tolerance for floats

PASS = "PASS"

TEXT_FORMAT = "text"  # question type when expected answer is a str, int, float, or bool
# question type when expected answer is a namedtuple
TEXT_FORMAT_NAMEDTUPLE = "text namedtuple"
# question type when the expected answer is a list where the order does *not* matter
TEXT_FORMAT_UNORDERED_LIST = "text list_unordered"
# question type when the expected answer is a list where the order does matter
TEXT_FORMAT_ORDERED_LIST = "text list_ordered"
# question type when the expected answer is a list of namedtuples where the order does matter
TEXT_FORMAT_ORDERED_LIST_NAMEDTUPLE = "text list_ordered namedtuple"
# question type when the expected answer is a list where order does matter, but with possible ties. Elements are ordered according to values in special_ordered_json (with ties allowed)
TEXT_FORMAT_SPECIAL_ORDERED_LIST = "text list_special_ordered"
# question type when the expected answer is a dictionary
TEXT_FORMAT_DICT = "text dict"


expected_json = {"1": (TEXT_FORMAT, 7.1),
                 "2": (TEXT_FORMAT_ORDERED_LIST, [{'title': 'Spider-Man: Into the Spider-Verse',
                                                'year': 2018,
                                                'duration': 117,
                                                'genres': ['Action', 'Adventure', 'Animation'],
                                                'rating': 8.4,
                                                'directors': ['Bob Persichetti', 'Peter Ramsey', 'Rodney Rothman'],
                                                'cast': ['Shameik Moore',
                                                'Jake Johnson',
                                                'Hailee Steinfeld',
                                                'Mahershala Ali']},
                                                {'title': 'Spider-Man Venom Saga',
                                                'year': 2005,
                                                'duration': 100,
                                                'genres': ['Animation'],
                                                'rating': 8.4,
                                                'directors': ['Bob Richardson'],
                                                'cast': ['James Avery',
                                                'Sara Ballantine',
                                                'John Beard',
                                                'Roscoe Lee Browne']}]),
                 "3": (TEXT_FORMAT_ORDERED_LIST, [{'title': 'Crouching Tiger, Hidden Dragon',
                                                      'year': 2000,
                                                      'duration': 120,
                                                      'genres': ['Action', 'Adventure', 'Drama'],
                                                      'rating': 7.9,
                                                      'directors': ['Ang Lee'],
                                                      'cast': ['Chow Yun-Fat', 'Michelle Yeoh', 'Ziyi Zhang', 'Chang Chen']},
                                                     {'title': 'Babylon A.D.',
                                                      'year': 2008,
                                                      'duration': 90,
                                                      'genres': ['Action', 'Adventure', 'Sci-Fi'],
                                                      'rating': 5.5,
                                                      'directors': ['Mathieu Kassovitz'],
                                                      'cast': ['Vin Diesel',
                                                       'Michelle Yeoh',
                                                       'Mélanie Thierry',
                                                       'Gérard Depardieu']},
                                                     {'title': 'Wing Chun',
                                                      'year': 1994,
                                                      'duration': 96,
                                                      'genres': ['Action', 'Comedy', 'Drama'],
                                                      'rating': 7.0,
                                                      'directors': ['Woo-Ping Yuen'],
                                                      'cast': ['Michelle Yeoh',
                                                       'Donnie Yen',
                                                       'King-Tan Yuen',
                                                       'Catherine Yan Hung']},
                                                     {'title': 'Crouching Tiger, Hidden Dragon: Sword of Destiny',
                                                      'year': 2016,
                                                      'duration': 96,
                                                      'genres': ['Action', 'Adventure', 'Drama'],
                                                      'rating': 6.1,
                                                      'directors': ['Woo-Ping Yuen'],
                                                      'cast': ['Donnie Yen',
                                                       'Michelle Yeoh',
                                                       'Harry Shum Jr.',
                                                       'Natasha Liu Bordizzo']},
                                                     {'title': 'Tai Chi Master',
                                                      'year': 1993,
                                                      'duration': 96,
                                                      'genres': ['Action', 'Comedy', 'Drama'],
                                                      'rating': 7.2,
                                                      'directors': ['Woo-Ping Yuen'],
                                                      'cast': ['Jet Li', 'Michelle Yeoh', 'Fennie Yuen']},
                                                     {'title': 'Tomorrow Never Dies',
                                                      'year': 1997,
                                                      'duration': 119,
                                                      'genres': ['Action', 'Adventure', 'Thriller'],
                                                      'rating': 6.5,
                                                      'directors': ['Roger Spottiswoode'],
                                                      'cast': ['Pierce Brosnan',
                                                       'Jonathan Pryce',
                                                       'Michelle Yeoh',
                                                       'Teri Hatcher']},
                                                     {'title': 'Gunpowder Milkshake',
                                                      'year': 2021,
                                                      'duration': 114,
                                                      'genres': ['Action', 'Crime', 'Thriller'],
                                                      'rating': 6.0,
                                                      'directors': ['Navot Papushado'],
                                                      'cast': ['Karen Gillan', 'Lena Headey', 'Carla Gugino', 'Michelle Yeoh']},
                                                     {'title': 'The Soong Sisters',
                                                      'year': 1997,
                                                      'duration': 145,
                                                      'genres': ['Drama', 'History', 'Romance'],
                                                      'rating': 7.0,
                                                      'directors': ['Mabel Cheung'],
                                                      'cast': ['Maggie Cheung', 'Michelle Yeoh', 'Vivian Wu', 'Winston Chao']},
                                                     {'title': 'Dynamite Fighters',
                                                      'year': 1987,
                                                      'duration': 91,
                                                      'genres': ['Action', 'Drama'],
                                                      'rating': 6.4,
                                                      'directors': ['David Chung'],
                                                      'cast': ['Michelle Yeoh', 'Richard Ng', 'Tung-Shing Yee', 'Lowell Lo']},
                                                     {'title': 'Boss Level',
                                                      'year': 2020,
                                                      'duration': 100,
                                                      'genres': ['Action', 'Adventure', 'Comedy'],
                                                      'rating': 6.8,
                                                      'directors': ['Joe Carnahan'],
                                                      'cast': ['Frank Grillo', 'Mel Gibson', 'Naomi Watts', 'Michelle Yeoh']},
                                                     {'title': 'The Mummy: Tomb of the Dragon Emperor',
                                                      'year': 2008,
                                                      'duration': 112,
                                                      'genres': ['Action', 'Adventure', 'Fantasy'],
                                                      'rating': 5.2,
                                                      'directors': ['Rob Cohen'],
                                                      'cast': ['Brendan Fraser', 'Jet Li', 'Maria Bello', 'Michelle Yeoh']},
                                                     {'title': 'Far North',
                                                      'year': 2007,
                                                      'duration': 89,
                                                      'genres': ['Crime', 'Drama', 'Romance'],
                                                      'rating': 6.1,
                                                      'directors': ['Asif Kapadia'],
                                                      'cast': ['Michelle Yeoh', 'Michelle Krusiec', 'Sean Bean', 'Gary Pillai']},
                                                     {'title': 'Master Z: The Ip Man Legacy',
                                                      'year': 2018,
                                                      'duration': 107,
                                                      'genres': ['Action', 'Biography', 'Crime'],
                                                      'rating': 6.5,
                                                      'directors': ['Woo-Ping Yuen'],
                                                      'cast': ['Jin Zhang', 'Dave Bautista', 'Michelle Yeoh', 'Tony Jaa']},
                                                     {'title': 'Silver Hawk',
                                                      'year': 2004,
                                                      'duration': 99,
                                                      'genres': ['Action', 'Adventure', 'Sci-Fi'],
                                                      'rating': 5.0,
                                                      'directors': ['Jingle Ma'],
                                                      'cast': ['Michelle Yeoh', 'Kôichi Iwaki', 'Brandon Chang', 'Luke Goss']},
                                                     {'title': 'The Heroic Trio',
                                                      'year': 1993,
                                                      'duration': 88,
                                                      'genres': ['Action', 'Fantasy', 'Thriller'],
                                                      'rating': 6.5,
                                                      'directors': ['Johnnie To'],
                                                      'cast': ['Michelle Yeoh', 'Anita Mui', 'Maggie Cheung', 'Damian Lau']},
                                                     {'title': 'Easy Money',
                                                      'year': 1987,
                                                      'duration': 92,
                                                      'genres': ['Action', 'Crime', 'Thriller'],
                                                      'rating': 5.1,
                                                      'directors': ['Stephen Shin'],
                                                      'cast': ['George Lam', 'Michelle Yeoh', 'Kent Cheng', 'Feng Ku']},
                                                     {'title': 'Crazy Rich Asians',
                                                      'year': 2018,
                                                      'duration': 120,
                                                      'genres': ['Comedy', 'Drama', 'Romance'],
                                                      'rating': 6.9,
                                                      'directors': ['Jon M. Chu'],
                                                      'cast': ['Constance Wu', 'Henry Golding', 'Michelle Yeoh', 'Gemma Chan']},
                                                     {'title': 'The Stunt Woman',
                                                      'year': 1996,
                                                      'duration': 95,
                                                      'genres': ['Action', 'Drama'],
                                                      'rating': 6.1,
                                                      'directors': ['Ann Hui'],
                                                      'cast': ['Michelle Yeoh', 'Sammo Kam-Bo Hung', 'Ken Lo', 'Hoi Mang']},
                                                     {'title': 'Mechanic: Resurrection',
                                                      'year': 2016,
                                                      'duration': 98,
                                                      'genres': ['Action', 'Adventure', 'Crime'],
                                                      'rating': 5.7,
                                                      'directors': ['Dennis Gansel'],
                                                      'cast': ['Jason Statham',
                                                       'Jessica Alba',
                                                       'Tommy Lee Jones',
                                                       'Michelle Yeoh']},
                                                     {'title': 'The Children of Huang Shi',
                                                      'year': 2008,
                                                      'duration': 125,
                                                      'genres': ['Drama', 'War'],
                                                      'rating': 7.0,
                                                      'directors': ['Roger Spottiswoode'],
                                                      'cast': ['Jonathan Rhys Meyers',
                                                       'Radha Mitchell',
                                                       'Chow Yun-Fat',
                                                       'Michelle Yeoh']},
                                                     {'title': 'Supercop',
                                                      'year': 1992,
                                                      'duration': 96,
                                                      'genres': ['Action', 'Comedy', 'Crime'],
                                                      'rating': 6.9,
                                                      'directors': ['Stanley Tong'],
                                                      'cast': ['Jackie Chan', 'Michelle Yeoh', 'Maggie Cheung', 'Kenneth Tsang']},
                                                     {'title': 'Final Recipe',
                                                      'year': 2013,
                                                      'duration': 97,
                                                      'genres': ['Drama'],
                                                      'rating': 6.7,
                                                      'directors': ['Gina Kim'],
                                                      'cast': ['Markus Waldow', 'Michelle Yeoh', 'Henry Lau', 'Chin Han']},
                                                     {'title': 'Reign of Assassins',
                                                      'year': 2010,
                                                      'duration': 117,
                                                      'genres': ['Action', 'Adventure'],
                                                      'rating': 6.8,
                                                      'directors': ['Chao-Bin Su', 'John Woo'],
                                                      'cast': ['Michelle Yeoh', 'Jung Woo-sung', 'Xueqi Wang', 'Barbie Hsu']},
                                                     {'title': 'Everything Everywhere All at Once',
                                                      'year': 2022,
                                                      'duration': 139,
                                                      'genres': ['Action', 'Adventure', 'Comedy'],
                                                      'rating': 8.0,
                                                      'directors': ['Dan Kwan', 'Daniel Scheinert'],
                                                      'cast': ['Michelle Yeoh',
                                                       'Stephanie Hsu',
                                                       'Jamie Lee Curtis',
                                                       'Ke Huy Quan']},
                                                     {'title': 'Yes, Madam!',
                                                      'year': 1985,
                                                      'duration': 93,
                                                      'genres': ['Action', 'Comedy', 'Crime'],
                                                      'rating': 6.6,
                                                      'directors': ['Corey Yuen'],
                                                      'cast': ['Michelle Yeoh', 'Cynthia Rothrock', 'John Sham', 'Hoi Mang']},
                                                     {'title': 'Supercop 2',
                                                      'year': 1993,
                                                      'duration': 104,
                                                      'genres': ['Action', 'Comedy', 'Crime'],
                                                      'rating': 6.1,
                                                      'directors': ['Stanley Tong'],
                                                      'cast': ['Michelle Yeoh', 'Rongguang Yu', 'Emil Chau', 'Athena Chu']},
                                                     {'title': 'Memoirs of a Geisha',
                                                      'year': 2005,
                                                      'duration': 145,
                                                      'genres': ['Drama', 'Romance'],
                                                      'rating': 7.3,
                                                      'directors': ['Rob Marshall'],
                                                      'cast': ['Ziyi Zhang', 'Ken Watanabe', 'Michelle Yeoh', 'Suzuka Ohgo']},
                                                     {'title': 'Heroic Trio 2: Executioners',
                                                      'year': 1993,
                                                      'duration': 101,
                                                      'genres': ['Action', 'Sci-Fi', 'Thriller'],
                                                      'rating': 5.8,
                                                      'directors': ['Siu-Tung Ching', 'Johnnie To'],
                                                      'cast': ['Maggie Cheung', 'Michelle Yeoh', 'Anita Mui', 'Damian Lau']},
                                                     {'title': 'The Touch',
                                                      'year': 2002,
                                                      'duration': 103,
                                                      'genres': ['Action', 'Adventure', 'Romance'],
                                                      'rating': 4.6,
                                                      'directors': ['Peter Pau'],
                                                      'cast': ['Michelle Yeoh', 'Ben Chaplin', 'Richard Roxburgh', 'Sihung Lung']},
                                                     {'title': 'Royal Warriors',
                                                      'year': 1986,
                                                      'duration': 96,
                                                      'genres': ['Action', 'Drama'],
                                                      'rating': 6.8,
                                                      'directors': ['David Chung'],
                                                      'cast': ['Michelle Yeoh', 'Michael Wong', 'Hiroyuki Sanada', 'Ying Bai']},
                                                     {'title': 'Butterfly and Sword',
                                                      'year': 1993,
                                                      'duration': 88,
                                                      'genres': ['Action', 'Adventure', 'Fantasy'],
                                                      'rating': 5.9,
                                                      'directors': ['Michael Mak'],
                                                      'cast': ['Tony Chiu-Wai Leung', 'Michelle Yeoh', 'Joey Wang', 'Elvis Tsui']},
                                                     {'title': 'The Lady',
                                                      'year': 2011,
                                                      'duration': 132,
                                                      'genres': ['Biography', 'Drama', 'History'],
                                                      'rating': 7.0,
                                                      'directors': ['Luc Besson'],
                                                      'cast': ['Michelle Yeoh',
                                                       'David Thewlis',
                                                       'Jonathan Raggett',
                                                       'Jonathan Woodhouse']},
                                                     {'title': 'Wonder Seven',
                                                      'year': 1994,
                                                      'duration': 90,
                                                      'genres': ['Action'],
                                                      'rating': 5.4,
                                                      'directors': ['Siu-Tung Ching'],
                                                      'cast': ['Michelle Yeoh', 'Ning Li', 'Andy Chi-On Hui', 'Kent Cheng']},
                                                     {'title': 'Holy Weapon',
                                                      'year': 1993,
                                                      'duration': 98,
                                                      'genres': ['Action', 'Comedy', 'Fantasy'],
                                                      'rating': 5.8,
                                                      'directors': ['Jing Wong', 'Dennis Chan'],
                                                      'cast': ['Michelle Yeoh',
                                                       "Carol 'Do Do' Cheng",
                                                       'Maggie Cheung',
                                                       'Sandra Kwan Yue Ng']}]),
                 "4": (TEXT_FORMAT_DICT, {'Action': 23975,
                                        'Crime': 21265,
                                        'Romance': 27456,
                                        'Comedy': 58377,
                                        'Drama': 108544,
                                        'Documentary': 10366,
                                        'Music': 4845,
                                        'Mystery': 9707,
                                        'Adventure': 14929,
                                        'Animation': 3856,
                                        'Family': 9142,
                                        'Western': 4591,
                                        'Thriller': 20583,
                                        'Sci-Fi': 5764,
                                        'Biography': 5065,
                                        'History': 5272,
                                        'Fantasy': 7221,
                                        'Horror': 16971,
                                        'Musical': 5264,
                                        'War': 4900,
                                        'Sport': 2190,
                                        'Film-Noir': 856,
                                        'News': 153,
                                        'Reality-TV': 17,
                                        'Short': 11,
                                        'Talk-Show': 1}),
                 "5": (TEXT_FORMAT_DICT, {'Drama': 8,
                                        'History': 3,
                                        'Thriller': 4,
                                        'Crime': 5,
                                        'Sci-Fi': 1,
                                        'War': 1,
                                        'Mystery': 1,
                                        'Action': 2,
                                        'Horror': 1}),
                 "6": (TEXT_FORMAT_DICT, {'2011 to 2020': 2134,
                                             '1971 to 1980': 377,
                                             '1981 to 1990': 612,
                                             '1991 to 2000': 623,
                                             '2021 to 2030': 396,
                                             '2001 to 2010': 931,
                                             '1951 to 1960': 242,
                                             '1961 to 1970': 320,
                                             '1931 to 1940': 52,
                                             '1941 to 1950': 37,
                                             '1921 to 1930': 19,
                                             '1911 to 1920': 21}),
                 "7": (TEXT_FORMAT_DICT, {'Drama': 6.85,
                                        'Fantasy': 6.1,
                                        'Mystery': 7.8,
                                        'Comedy': 5.95,
                                        'Romance': 6.4,
                                        'Crime': 7.2,
                                        'Horror': 5.0,
                                        'Sci-Fi': 4.6,
                                        'Thriller': 5.7,
                                        'Musical': 6.3,
                                        'Music': 6.5,
                                        'War': 7.45,
                                        'Western': 3.0,
                                        'Biography': 6.9,
                                        'Adventure': 4.4,
                                        'Family': 6.1}),
                 "8": (TEXT_FORMAT_SPECIAL_ORDERED_LIST, ['Mystery',
                                                        'War',
                                                        'Crime',
                                                        'Biography',
                                                        'Drama',
                                                        'Music',
                                                        'Romance',
                                                        'Musical',
                                                        'Fantasy',
                                                        'Family',
                                                        'Comedy',
                                                        'Thriller',
                                                        'Horror',
                                                        'Sci-Fi',
                                                        'Adventure',
                                                        'Western']),
                 "9": (TEXT_FORMAT_ORDERED_LIST, [{'title': 'Mean Streets',
                                                      'year': 1973,
                                                      'duration': 112,
                                                      'genres': ['Crime', 'Drama', 'Thriller'],
                                                      'rating': 7.2,
                                                      'directors': ['Martin Scorsese'],
                                                      'cast': ['Robert De Niro', 'Harvey Keitel', 'David Proval', 'Amy Robinson']},
                                                     {'title': 'Taxi Driver',
                                                      'year': 1976,
                                                      'duration': 114,
                                                      'genres': ['Crime', 'Drama'],
                                                      'rating': 8.2,
                                                      'directors': ['Martin Scorsese'],
                                                      'cast': ['Robert De Niro',
                                                       'Jodie Foster',
                                                       'Cybill Shepherd',
                                                       'Albert Brooks']},
                                                     {'title': 'New York, New York',
                                                      'year': 1977,
                                                      'duration': 155,
                                                      'genres': ['Drama', 'Music', 'Musical'],
                                                      'rating': 6.6,
                                                      'directors': ['Martin Scorsese'],
                                                      'cast': ['Liza Minnelli',
                                                       'Robert De Niro',
                                                       'Lionel Stander',
                                                       'Barry Primus']},
                                                     {'title': 'Raging Bull',
                                                      'year': 1980,
                                                      'duration': 129,
                                                      'genres': ['Biography', 'Drama', 'Sport'],
                                                      'rating': 8.2,
                                                      'directors': ['Martin Scorsese'],
                                                      'cast': ['Robert De Niro', 'Cathy Moriarty', 'Joe Pesci', 'Frank Vincent']},
                                                     {'title': 'The King of Comedy',
                                                      'year': 1982,
                                                      'duration': 109,
                                                      'genres': ['Comedy', 'Crime', 'Drama'],
                                                      'rating': 7.8,
                                                      'directors': ['Martin Scorsese'],
                                                      'cast': ['Robert De Niro',
                                                       'Jerry Lewis',
                                                       'Diahnne Abbott',
                                                       'Sandra Bernhard']},
                                                     {'title': 'Goodfellas',
                                                      'year': 1990,
                                                      'duration': 145,
                                                      'genres': ['Biography', 'Crime', 'Drama'],
                                                      'rating': 8.7,
                                                      'directors': ['Martin Scorsese'],
                                                      'cast': ['Robert De Niro', 'Ray Liotta', 'Joe Pesci', 'Lorraine Bracco']},
                                                     {'title': 'Cape Fear',
                                                      'year': 1991,
                                                      'duration': 128,
                                                      'genres': ['Crime', 'Thriller'],
                                                      'rating': 7.3,
                                                      'directors': ['Martin Scorsese'],
                                                      'cast': ['Robert De Niro', 'Nick Nolte', 'Jessica Lange', 'Juliette Lewis']},
                                                     {'title': 'Casino',
                                                      'year': 1995,
                                                      'duration': 178,
                                                      'genres': ['Crime', 'Drama'],
                                                      'rating': 8.2,
                                                      'directors': ['Martin Scorsese'],
                                                      'cast': ['Robert De Niro', 'Sharon Stone', 'Joe Pesci', 'James Woods']},
                                                     {'title': 'The Irishman',
                                                      'year': 2019,
                                                      'duration': 209,
                                                      'genres': ['Biography', 'Crime', 'Drama'],
                                                      'rating': 7.8,
                                                      'directors': ['Martin Scorsese'],
                                                      'cast': ['Robert De Niro', 'Al Pacino', 'Joe Pesci', 'Harvey Keitel']}]),
                 "10": (TEXT_FORMAT_UNORDERED_LIST, ['Juan Bustillo Oro',
                                                         'Martin Scorsese',
                                                         'Martin Fric',
                                                         'Sandip Ray',
                                                         'Sam Mendes',
                                                         'David Lean',
                                                         'Luchino Visconti',
                                                         'King Hu',
                                                         'Masaki Kobayashi',
                                                         'Sam Peckinpah',
                                                         'Joseph L. Mankiewicz',
                                                         'Satsuo Yamamoto',
                                                         'Akira Kurosawa',
                                                         'Aditya Sarpotdar',
                                                         'Quentin Tarantino',
                                                         'Leonardo Favio',
                                                         'Joel Coen',
                                                         'François Truffaut',
                                                         'Francis Lawrence',
                                                         'Emeric Pressburger',
                                                         'Goran Markovic',
                                                         'Vytautas Zalakevicius',
                                                         'Marc Forster',
                                                         'Isao Takahata',
                                                         'Satyajit Ray',
                                                         'Aziz M. Osman',
                                                         'Carlos Enrique Taboada',
                                                         'Danny Boyle',
                                                         'I. Kolyada',
                                                         'Prince Oak Oakleyski',
                                                         'Paul Greengrass',
                                                         'T.S. Nagabharana'])}

special_json = {"8": [['Mystery'],
                     ['War'],
                     ['Crime'],
                     ['Biography'],
                     ['Drama'],
                     ['Music'],
                     ['Romance'],
                     ['Musical'],
                     ['Fantasy', 'Family'],
                     ['Comedy'],
                     ['Thriller'],
                     ['Horror'],
                     ['Sci-Fi'],
                     ['Adventure'],
                     ['Western']]}


def compare_outputs(expected, actual, format):
    try:
        if format == TEXT_FORMAT:
            return simple_compare(expected, actual)
        elif format == TEXT_FORMAT_ORDERED_LIST:
            return list_compare_ordered(expected, actual)
        elif format == TEXT_FORMAT_UNORDERED_LIST:
            return list_compare_unordered(expected, actual)
        elif format == TEXT_FORMAT_SPECIAL_ORDERED_LIST:
            return list_compare_special(expected, actual)
        elif format == TEXT_FORMAT_DICT:
            return dict_compare(expected, actual)
        else:
            if expected != actual:
                return "expected %s but found %s " % (repr(expected), repr(actual))
    except:
        if expected != actual:
            return "expected %s" % (repr(expected))
        else:
            return PASS

def check_cell_text(qnum, actual):
    format, expected = expected_json[qnum[1:]]
    if format == TEXT_FORMAT_SPECIAL_ORDERED_LIST:
        expected_ordering = special_json[qnum[1:]]
        return compare_outputs(expected_ordering, actual, format)
    else:
        return compare_outputs(expected, actual, format)


def simple_compare(expected, actual, complete_msg=True):
    msg = PASS
    if type(expected) == type:
        if expected != actual:
            if type(actual) == type:
                msg = "expected %s but found %s" % (
                    expected.__name__, actual.__name__)
            else:
                msg = "expected %s but found %s" % (
                    expected.__name__, repr(actual))
    elif type(expected) != type(actual) and not (type(expected) in [float, int] and type(actual) in [float, int]):
        msg = "expected to find type %s but found type %s" % (
            type(expected).__name__, type(actual).__name__)
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

def obfuscate1():
    return 'Not yet'

def list_compare_ordered(expected, actual, obj="list"):
    msg = PASS
    if type(expected) != type(actual):
        msg = "expected to find type %s but found type %s" % (
            type(expected).__name__, type(actual).__name__)
        return msg
    for i in range(len(expected)):
        if i >= len(actual):
            msg = "expected missing %s in %s" % (repr(expected[i]), obj)
            break
        if type(expected[i]) in [int, float, bool, str]:
            val = simple_compare(expected[i], actual[i])
        elif type(expected[i]) in [list, tuple]:
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
        msg = msg + \
            " (found %d entries in %s, but expected %d)" % (
                len(actual), obj, len(expected))

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
            msg = "in the %s, " % (
                obj) + simple_compare(sort_expected[0], sort_actual[0])
        else:
            if len(expected) > len(actual):
                msg = "in the %s, missing " % (
                    obj) + list_compare_helper(sort_expected, sort_actual)
            elif len(expected) < len(actual):
                msg = "in the %s, found un" % (
                    obj) + list_compare_helper(sort_actual, sort_expected)
            if len(expected) != len(actual):
                msg = msg + \
                    " (found %d entries in %s, but expected %d)" % (
                        len(actual), obj, len(expected))
                return msg
            else:
                val = list_compare_helper(sort_expected, sort_actual)
                if val != PASS:
                    msg = "in the %s, missing " % (obj) + val + ", but found un" + list_compare_helper(sort_actual, sort_expected)
    return msg


def list_compare_special(special_expected, actual):
    msg = PASS
    expected_list = []
    for expected_item in special_expected:
        expected_list.extend(expected_item)
    val = list_compare_unordered(expected_list, actual)
    if val != PASS:
        msg = val
    else:
        i = 0
        for expected_item in special_expected:
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
        msg = "expected to find type %s but found type %s" % (
            type(expected).__name__, type(actual).__name__)
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
                msg = "incorrect val for key %s in %s: " % (
                    repr(key), obj) + val
    return msg


def check(qnum, actual):
    msg = check_cell_text(qnum, actual)
    if msg == PASS:
        return True
    print("<b style='color: red;'>ERROR:</b> " + msg)

def check_file_size(path):
    size = os.path.getsize(path)
    assert size < MAX_FILE_SIZE * 10**3, "Your file is too big to be processed by Gradescope; please delete unnecessary output cells so your file size is < %s KB" % MAX_FILE_SIZE
