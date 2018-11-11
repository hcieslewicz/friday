import json
from context import customer


def test_address_line_splitting():
    addr = customer.address.Address()
    print "text to split: %s" % addr.split_street_name_and_number("Winterallee 3")
    assert addr.split_street_name_and_number("Winterallee 3") == json.dumps({"street": "Winterallee", "housenumber": "3"}, ensure_ascii=False)