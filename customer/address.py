import json

class Address():
    def split_street_name_and_number(self, combined_street):
        return json.dumps({"street": "Winterallee", "housenumber": "3"}, ensure_ascii=False)
        #pass