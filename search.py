import re
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

