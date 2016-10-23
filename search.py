import re
import datetime

import fileoperation


class Search:

    def __init__(self):
        self.browse = fileoperation.Browse()
        self.data = self.browse.get_data()

    def exact_string(self, query):
        dicts_list = []
        for dicts in self.data:
            for key, value in dicts.items():

                if key == 'Task Name' or key == 'Description':
                    regex_search = re.search(r"\b"+query, value)
                    if regex_search is not None:
                        dicts_list.append(dicts)

        return dicts_list

    def by_date(self, query):

        format1 = "%m/%d/%Y"

        try:
            queried_datetime = datetime.datetime.strptime(query, format1)
        except ValueError:
            return "incorrect format"

        dicts_list = []
        for dicts in self.data:
            for key, value in dicts.items():
                if key == 'Date':
                    pass
