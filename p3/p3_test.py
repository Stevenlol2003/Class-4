#!/usr/bin/python

import os, json, math

MAX_FILE_SIZE = 500 # units - KB
REL_TOL = 6e-04  # relative tolerance for floats
ABS_TOL = 15e-03  # absolute tolerance for floats

PASS = "PASS"

TEXT_FORMAT = "text"  # question type when expected answer is a str, int, float, or bool

expected_json =    {"1": (TEXT_FORMAT, 977),
                    "2": (TEXT_FORMAT, 11230),
                    "3": (TEXT_FORMAT, 26500),
                    "4": (TEXT_FORMAT, 43525),
                    "5": (TEXT_FORMAT, 10125),
                    "6": (TEXT_FORMAT, 16),
                    "7": (TEXT_FORMAT, 34939.2),
                    "8": (TEXT_FORMAT, 8730.6),
                    "9": (TEXT_FORMAT, 2292.3999999999996),
                    "10": (TEXT_FORMAT, 116806),
                    "11": (TEXT_FORMAT, 289765),
                    "12": (TEXT_FORMAT, -1572.5),
                    "13": (TEXT_FORMAT, -6096.666666666667),
                    "14": (TEXT_FORMAT, 2389.0),
                    "15": (TEXT_FORMAT, 17248.0),
                    "16": (TEXT_FORMAT, 91315.0),
                    "17": (TEXT_FORMAT, -41541.5),
                    "18": (TEXT_FORMAT, 32092.5),
                    "19": (TEXT_FORMAT, -406.5),
                    "20": (TEXT_FORMAT, 2.090140253191154)}

def check_cell(qnum, actual):
    format, expected = expected_json[qnum[1:]]
    try:
        if format == TEXT_FORMAT:
            return simple_compare(expected, actual)
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

def check(qnum, actual):
    msg = check_cell(qnum, actual)
    if msg == PASS:
        return True
    print("<b style='color: red;'>ERROR:</b> " + msg)

def check_file_size(path):
    size = os.path.getsize(path)
    assert size < MAX_FILE_SIZE * 10**3, "Your file is too big to be processed by Gradescope; please delete unnecessary output cells so your file size is < %s KB" % MAX_FILE_SIZE
