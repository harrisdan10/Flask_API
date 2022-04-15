import pandas as pd

def search_filter(filter_by):
    file = 'devilfruit.csv'
    criteria = []
    splitter = [x.strip() for x in filter_by.split(",")]
    for value in splitter:
        if value in ["Character", "Devil Fruit", "Class", "Subclass", "Awakened", "Status", "All"]:
            criteria.append(value)

    return search(file, criteria)

#
def search(file, criteria):
    info = pd.read_csv(file)
    if "All" not in criteria:
        info.drop(info.columns.difference(criteria), 1, inplace=True)
    return info.to_dict(orient='records')

