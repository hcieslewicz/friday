# coding=utf-8
import json
import re

class Address():
    def split_street_name_and_number(self, combined_street):
        combined_street = combined_street.strip()

        # List with needed regexes. They don't have to be precompiled, cause there is no performance drop
        # with this small number. They are not inline (regex1|regex2|...) just for readability.
        regex_list = [  r'^(?P<street>[a-zA-ZäöüÄÖÜß\s\d]+),?\s(?P<house>No\s\d+\s?\w?)$',      # Calle 39 No 1540   #
                        r'^(?P<house>\d+)[\s|,]\s?(?P<street>[\s*\w*]+)$',                      # 4, rue de la revolution
                        r'^(?P<street>[a-zA-ZäöüÄÖÜß\s]+[\s\d]*),?\s(?P<house>\d+\s?\w?)$',     # the rest of know formats
                        ]

        # This is second way of regex list with only 2 expressions. Could be more complicated to keep it up to date.
        #regex_list = [
        #    r'^(?P<street>[a-zA-ZäöüÄÖÜß\s]+[\s\d]*),?\s(?P<house>[N]?[o]?\s?\d+\s?\w?)$',
        #    r'^(?P<house>\d+)[\s|,]\s?(?P<street>[\s*\w*]+)$'
        #]


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
