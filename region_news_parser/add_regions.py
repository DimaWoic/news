from ast import literal_eval


def dict_city():
    with open('dict_rss.txt', 'r') as file:
        stroke_dict = file.read()

    dict_city = literal_eval(stroke_dict)

    return dict_city