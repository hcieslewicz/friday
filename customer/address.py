import json
import re

class Address():
    def split_street_name_and_number(self, combined_street):
        print "string to work with: %s" % combined_street
        combined_street = combined_street.strip()

        regex_list = [r'^(?P<street>.*?\D),? (?P<house>\d+\s?\w?)$',
                      r'^(?P<street>.*?\D[\s?\D?]+) (?P<house>\d+\s?\w?)$',
                      r'^(?P<house>\d+)[\s|,]\s?(?P<street>[\s*\w*]+)$']

        for regex in regex_list:
            print "regex: %s" % regex
            m = re.search(regex, combined_street)
            if m:
                print "m.group(0): %s" % m.group(0)
                #print "m.group(1): %s" % m.group(1)
                #print "m.group(2): %s" % m.group(2)
                #street_name = m.group(1)
                #house_number = m.group(2)
                street_name = m.group('street')
                house_number = m.group('house')
                print "street_name: %s" % street_name
                print "house_number: %s" % house_number
                break




        a = {}
        a["street"] = street_name
        a["housenumber"] = house_number
        return json.dumps(a, ensure_ascii=False)





