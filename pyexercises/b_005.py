NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    return [x.title() for x in list(dict.fromkeys(names))]


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    sorted_names = sorted(names, reverse=True, key=lambda x: x.split()[-1])
    return sorted_names


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    this_names = [x.split()[0] for x in names]
    short_name = sorted(this_names, key=lambda x: len(x.split()[0]))
    return short_name[0]


print(dedup_and_title_case_names(NAMES))
