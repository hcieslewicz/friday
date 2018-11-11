# coding=utf-8
import sys
from os import path
#sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest
from context import customer
import json



def test_address_line_splitting():
    addr = customer.address.Address()
    print "aaa: %s" % addr.split_street_name_and_number("Winterallee 3")
    assert addr.split_street_name_and_number("Winterallee 3") == json.dumps({"street": "Winterallee", "housenumber": "3"}, ensure_ascii=False)
    assert addr.split_street_name_and_number("Musterstrasse 45") == json.dumps({"street": "Musterstrasse", "housenumber": "45"}, ensure_ascii=False)
    assert addr.split_street_name_and_number("Blaufeldweg 123B") == json.dumps({"street": "Blaufeldweg", "housenumber": "123B"}, ensure_ascii=False)
    assert addr.split_street_name_and_number("Am Bächle 23") == json.dumps({"street": "Am Bächle", "housenumber": "23"}, ensure_ascii=False)
    assert addr.split_street_name_and_number("Auf der Vogelwiese 23 b") == json.dumps({"street": "Auf der Vogelwiese", "housenumber": "23 b"}, ensure_ascii=False)
    assert addr.split_street_name_and_number("4, rue de la revolution") == json.dumps({"street": "rue de la revolution", "housenumber": "4"}, ensure_ascii=False)
    assert addr.split_street_name_and_number("200 Broadway Av") == json.dumps({"street": "Broadway Av", "housenumber": "200"}, ensure_ascii=False)
    assert addr.split_street_name_and_number("Calle Aduana, 29") == json.dumps({"street": "Calle Aduana", "housenumber": "29"}, ensure_ascii=False)
    assert addr.split_street_name_and_number("Calle 39 No 1540") == json.dumps({"street": "Calle 39", "housenumber": "No 1540"}, ensure_ascii=False)
