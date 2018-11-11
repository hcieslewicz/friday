# coding=utf-8
import json
import re

class Address():
    def split_street_name_and_number(self, combined_street):
        combined_street = combined_street.strip()

        # List with needed regexes. They don't have to be precompiled, cause there is no performance drop
        # with this small number. They are not inline (regex1|regex2|...) just for readability.
        regex_list = [
                        r'^(?P<street>[a-zA-ZäöüÄÖÜß\s\d]+),?\s(?P<house>[N]?[o]?.?\s?\d+\s?\w?)$',
                        r'^(?P<house>\d+)[\s|,]\s?(?P<street>[\s*\w*]+)$',
        ]
        street_name = None
        house_number = None

        for regex in regex_list:
            m = re.search(regex, combined_street, re.UNICODE)
            if m:
                street_name = m.group('street')
                house_number = m.group('house')
                break

        a = {}
        a["street"] = street_name
        a["housenumber"] = house_number
        return json.dumps(a, ensure_ascii=False)
