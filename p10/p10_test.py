#!/usr/bin/python
import os, json, math
from collections import namedtuple

MAX_FILE_SIZE = 300 # units - KB
REL_TOL = 6e-04  # relative tolerance for floats
ABS_TOL = 15e-03  # absolute tolerance for floats

PASS = "PASS"

TEXT_FORMAT = "text"  # question type when expected answer is a str, int, float, or bool
TEXT_FORMAT_NAMEDTUPLE = "text namedtuple"  # question type when expected answer is a namedtuple
TEXT_FORMAT_UNORDERED_LIST = "text list_unordered"  # question type when the expected answer is a list where the order does *not* matter
TEXT_FORMAT_ORDERED_LIST = "text list_ordered"  # question type when the expected answer is a list where the order does matter
TEXT_FORMAT_SPECIAL_ORDERED_LIST = "text list_special_ordered"  # question type when the expected answer is a list where order does matter, but with possible ties. Elements are ordered according to values in special_ordered_json (with ties allowed)
TEXT_FORMAT_DICT = "text dict"  # question type when the expected answer is a dictionary

def return_expected_json():
    expected_json =    {"1": (TEXT_FORMAT_ORDERED_LIST, ['stars_5.csv',
                                                     'stars_4.csv',
                                                     'stars_3.csv',
                                                     'stars_2.csv',
                                                     'stars_1.csv',
                                                     'planets_5.csv',
                                                     'planets_4.csv',
                                                     'planets_3.csv',
                                                     'planets_2.csv',
                                                     'planets_1.csv',
                                                     'mapping_5.json',
                                                     'mapping_4.json',
                                                     'mapping_3.json',
                                                     'mapping_2.json',
                                                     'mapping_1.json']),
                    "2": (TEXT_FORMAT_ORDERED_LIST, [os.path.join("data", "stars_5.csv"),
                                                    os.path.join("data", "stars_4.csv"),
                                                    os.path.join("data", "stars_3.csv"),
                                                    os.path.join("data", "stars_2.csv"),
                                                    os.path.join("data", "stars_1.csv"),
                                                    os.path.join("data", "planets_5.csv"),
                                                    os.path.join("data", "planets_4.csv"),
                                                    os.path.join("data", "planets_3.csv"),
                                                    os.path.join("data", "planets_2.csv"),
                                                    os.path.join("data", "planets_1.csv"),
                                                    os.path.join("data", "mapping_5.json"),
                                                    os.path.join("data", "mapping_4.json"),
                                                    os.path.join("data", "mapping_3.json"),
                                                    os.path.join("data", "mapping_2.json"),
                                                    os.path.join("data", "mapping_1.json")]),
                    "3": (TEXT_FORMAT_ORDERED_LIST, [os.path.join("data", "stars_5.csv"),
                                                    os.path.join("data", "stars_4.csv"),
                                                    os.path.join("data", "stars_3.csv"),
                                                    os.path.join("data", "stars_2.csv"),
                                                    os.path.join("data", "stars_1.csv"),
                                                    os.path.join("data", "planets_5.csv"),
                                                    os.path.join("data", "planets_4.csv"),
                                                    os.path.join("data", "planets_3.csv"),
                                                    os.path.join("data", "planets_2.csv"),
                                                    os.path.join("data", "planets_1.csv")]),
                    "4": (TEXT_FORMAT_ORDERED_LIST, [os.path.join("data", "stars_5.csv"),
                                                    os.path.join("data", "stars_4.csv"),
                                                    os.path.join("data", "stars_3.csv"),
                                                    os.path.join("data", "stars_2.csv"),
                                                    os.path.join("data", "stars_1.csv")]),
                    "star_object": (TEXT_FORMAT_NAMEDTUPLE, Star(spectral_type='G2 V', stellar_effective_temperature=5780.0,
                                                                stellar_radius=1.0, stellar_mass=1.0, stellar_luminosity=0.0,
                                                                stellar_surface_gravity=4.44, stellar_age=4.6)),
                    "5": (TEXT_FORMAT_NAMEDTUPLE, Star(spectral_type='K0 III', stellar_effective_temperature=4813.0,
                                                        stellar_radius=11.0, stellar_mass=2.2, stellar_luminosity=1.763,
                                                        stellar_surface_gravity=2.63, stellar_age=4.5)),
                    "6": (TEXT_FORMAT_NAMEDTUPLE, Star(spectral_type=None, stellar_effective_temperature=13500.0,
                                                        stellar_radius=0.01, stellar_mass=0.69, stellar_luminosity=-2.4,
                                                        stellar_surface_gravity=None, stellar_age=None)),
                    "7": (TEXT_FORMAT, 0.016741496598639403),
                    "8": (TEXT_FORMAT, 4.290235955056181),
                    "9": (TEXT_FORMAT, 4632.0),
                    "10": (TEXT_FORMAT, 'HD 81817'),
                    "11": (TEXT_FORMAT, 4.217130505709651),
                    "planet_object": (TEXT_FORMAT_NAMEDTUPLE, Planet(planet_name='Jupiter', host_name='Sun',
                                                                    discovery_method='Imaging', discovery_year=1610,
                                                                    controversial_flag=False, orbital_period=4333.0,
                                                                    planet_radius=11.209, planet_mass=317.828,
                                                                    semi_major_radius=5.2038, eccentricity=0.0489,
                                                                    equilibrium_temperature=110, insolation_flux=0.0345)),
                    "12": (TEXT_FORMAT_NAMEDTUPLE, Planet(planet_name='17 Sco b', host_name='17 Sco',
                                                          discovery_method='Radial Velocity', discovery_year=2020,
                                                          controversial_flag=False, orbital_period=578.38,
                                                          planet_radius=12.9, planet_mass=1373.01872, semi_major_radius=1.45,
                                                          eccentricity=0.06, equilibrium_temperature=None, insolation_flux=None)),
                    "13": (TEXT_FORMAT_ORDERED_LIST,[Planet(planet_name='Kepler-1478 b', host_name='Kepler-1478', discovery_method='Transit', discovery_year=2016, controversial_flag=False, orbital_period=26.0840594, planet_radius=1.73, planet_mass=3.64, semi_major_radius=0.1681, eccentricity=0.0, equilibrium_temperature=598.0, insolation_flux=85.28),
                                                     Planet(planet_name='Kepler-1479 b', host_name='Kepler-1479', discovery_method='Transit', discovery_year=2016, controversial_flag=False, orbital_period=14.53261362, planet_radius=1.83, planet_mass=4.01, semi_major_radius=0.1173, eccentricity=0.0, equilibrium_temperature=746.0, insolation_flux=98.57),
                                                     Planet(planet_name='Kepler-1480 b', host_name='Kepler-1480', discovery_method='Transit', discovery_year=2016, controversial_flag=False, orbital_period=22.12679948, planet_radius=1.67, planet_mass=3.43, semi_major_radius=0.1525, eccentricity=0.0, equilibrium_temperature=721.0, insolation_flux=16.32),
                                                     Planet(planet_name='Kepler-1481 b', host_name='Kepler-1481', discovery_method='Transit', discovery_year=2016, controversial_flag=False, orbital_period=5.94220998, planet_radius=1.23, planet_mass=2.04, semi_major_radius=0.059, eccentricity=0.0, equilibrium_temperature=797.0, insolation_flux=71.94),
                                                     Planet(planet_name='Kepler-1482 b', host_name='Kepler-1482', discovery_method='Transit', discovery_year=2016, controversial_flag=False, orbital_period=12.25383217, planet_radius=1.01, planet_mass=1.01, semi_major_radius=0.1016, eccentricity=0.0, equilibrium_temperature=678.0, insolation_flux=86.5)]),

                    "14": (TEXT_FORMAT_ORDERED_LIST, [Planet(planet_name='Kepler-452 b', host_name='Kepler-452', discovery_method='Transit', discovery_year=2015, controversial_flag=True, orbital_period=384.843, planet_radius=1.63, planet_mass=3.29, semi_major_radius=1.046, eccentricity=0.0, equilibrium_temperature=265.0, insolation_flux=1.1),
                                                      Planet(planet_name='Kepler-747 b', host_name='Kepler-747', discovery_method='Transit', discovery_year=2016, controversial_flag=True, orbital_period=35.61760587, planet_radius=5.27, planet_mass=24.1, semi_major_radius=0.1916, eccentricity=0.0, equilibrium_temperature=456.0, insolation_flux=10.19),
                                                      Planet(planet_name='V830 Tau b', host_name='V830 Tau', discovery_method='Radial Velocity', discovery_year=2016, controversial_flag=True, orbital_period=4.927, planet_radius=14.0, planet_mass=222.481, semi_major_radius=0.057, eccentricity=0.0, equilibrium_temperature=None, insolation_flux=None),
                                                      Planet(planet_name='nu Oct A b', host_name='nu Oct A', discovery_method='Radial Velocity', discovery_year=2016, controversial_flag=True, orbital_period=417.0, planet_radius=13.3, planet_mass=762.78818, semi_major_radius=1.25, eccentricity=0.11, equilibrium_temperature=None, insolation_flux=None)]),
                    "15": (TEXT_FORMAT_ORDERED_LIST, [Planet(planet_name='Wolf 1061 c', host_name='Wolf 1061', discovery_method='Radial Velocity', discovery_year=2015, controversial_flag=False, orbital_period=17.8719, planet_radius=1.66, planet_mass=3.41, semi_major_radius=0.089, eccentricity=0.11, equilibrium_temperature=None, insolation_flux=1.3),
                                                     Planet(planet_name='Wolf 1061 d', host_name='Wolf 1061', discovery_method='Radial Velocity', discovery_year=2015, controversial_flag=False, orbital_period=217.21, planet_radius=2.69, planet_mass=7.7, semi_major_radius=0.47, eccentricity=0.55, equilibrium_temperature=None, insolation_flux=0.06),
                                                     Planet(planet_name='YZ Cet b', host_name='YZ Cet', discovery_method='Radial Velocity', discovery_year=2017, controversial_flag=False, orbital_period=2.02087, planet_radius=0.913, planet_mass=0.7, semi_major_radius=0.01634, eccentricity=0.06, equilibrium_temperature=471.0, insolation_flux=8.21),
                                                     Planet(planet_name='YZ Cet c', host_name='YZ Cet', discovery_method='Radial Velocity', discovery_year=2017, controversial_flag=False, orbital_period=3.05989, planet_radius=1.05, planet_mass=1.14, semi_major_radius=0.02156, eccentricity=0.0, equilibrium_temperature=410.0, insolation_flux=4.72),
                                                     Planet(planet_name='YZ Cet d', host_name='YZ Cet', discovery_method='Radial Velocity', discovery_year=2017, controversial_flag=False, orbital_period=4.65626, planet_radius=1.03, planet_mass=1.09, semi_major_radius=0.02851, eccentricity=0.07, equilibrium_temperature=357.0, insolation_flux=2.7)]),
                    "16": (TEXT_FORMAT_ORDERED_LIST, [Planet(planet_name='Kepler-19 c', host_name='Kepler-19', discovery_method='Transit Timing Variations', discovery_year=2011, controversial_flag=False, orbital_period=28.731, planet_radius=3.68, planet_mass=13.1, semi_major_radius=None, eccentricity=0.21, equilibrium_temperature=None, insolation_flux=None),
                                                     Planet(planet_name='Kepler-19 d', host_name='Kepler-19', discovery_method='Radial Velocity', discovery_year=2017, controversial_flag=False, orbital_period=62.95, planet_radius=5.06, planet_mass=22.5, semi_major_radius=None, eccentricity=0.05, equilibrium_temperature=None, insolation_flux=None),
                                                     Planet(planet_name='Kepler-191 b', host_name='Kepler-191', discovery_method='Transit', discovery_year=2014, controversial_flag=False, orbital_period=9.939632, planet_radius=1.34, planet_mass=2.36, semi_major_radius=0.087, eccentricity=0.0, equilibrium_temperature=722.0, insolation_flux=64.29),
                                                     Planet(planet_name='Kepler-191 c', host_name='Kepler-191', discovery_method='Transit', discovery_year=2014, controversial_flag=False, orbital_period=17.738506, planet_radius=1.86, planet_mass=4.12, semi_major_radius=0.128, eccentricity=0.0, equilibrium_temperature=596.0, insolation_flux=29.74),
                                                     Planet(planet_name='Kepler-191 d', host_name='Kepler-191', discovery_method='Transit', discovery_year=2016, controversial_flag=False, orbital_period=5.94504102, planet_radius=2.28, planet_mass=5.82, semi_major_radius=0.0599, eccentricity=0.0, equilibrium_temperature=857.0, insolation_flux=127.64)]),
                    "17": (TEXT_FORMAT, 325),
                    "18": (TEXT_FORMAT_NAMEDTUPLE, Star(spectral_type='K8 V', stellar_effective_temperature=5144.0,
                                                        stellar_radius=0.79, stellar_mass=0.82, stellar_luminosity=-0.401,
                                                        stellar_surface_gravity=4.55, stellar_age=7.48)),
                    "19": (TEXT_FORMAT, 12.87916666666667),
                    "20": (TEXT_FORMAT_ORDERED_LIST, [Planet(planet_name='Kepler-1663 b', host_name='Kepler-1663',
                                                            discovery_method='Transit', discovery_year=2020,
                                                            controversial_flag=False, orbital_period=17.6046, planet_radius=3.304,
                                                            planet_mass=10.9, semi_major_radius=0.1072, eccentricity=0.0,
                                                            equilibrium_temperature=362.0, insolation_flux=4.07)])}
    return expected_json

def check_cell(qnum, actual):
    expected_json = return_expected_json()
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
        elif format == TEXT_FORMAT_NAMEDTUPLE:
            return namedtuple_compare(expected ,actual)
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

namedtuples = ['Star', 'Planet']
star_attributes = ['spectral_type',
                  'stellar_effective_temperature',
                  'stellar_radius',
                  'stellar_mass',
                  'stellar_luminosity',
                  'stellar_surface_gravity',
                  'stellar_age']
# Create a namedtuple type, Star
Star = namedtuple("Star", star_attributes)
planets_attributes = ['planet_name',
                     'host_name',
                     'discovery_method',
                     'discovery_year',
                     'controversial_flag',
                     'orbital_period',
                     'planet_radius',
                     'planet_mass',
                     'semi_major_radius',
                     'eccentricity',
                     'equilibrium_temperature',
                     'insolation_flux']
# Create a namedtuple type, Planet
Planet = namedtuple("Planet", planets_attributes)

def namedtuple_compare(expected, actual):
    msg = PASS
    try:
        actual_fields = actual._fields
    except AttributeError:
        msg = "expected namedtuple but found %s" % (type(actual).__name__)
        return msg
    if type(expected).__name__ != type(actual).__name__:
        msg = "expected namedtuple %s but found namedtuple %s" % (type(expected).__name__, type(actual).__name__)
        return msg
    expected_fields = expected._fields
    msg = list_compare_ordered(list(expected_fields), list(actual_fields), "namedtuple attributes")
    if msg != PASS:
        return msg
    for field in expected_fields:
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
        elif type(expected[i]).__name__ in namedtuples:
            val = namedtuple_compare(expected[i], actual[i])
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
                msg = msg + " (%s may not be ordered as required)" % (obj)
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
            elif type(expected[key]).__name__ in namedtuples:
                val = namedtuple_compare(expected[key], actual[key])
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
