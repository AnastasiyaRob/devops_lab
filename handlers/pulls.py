import requests


def response():
    url = "https://api.github.com/repos/alenaPy/devops_lab/pulls"
    parameter = "?per_page=100&state=all"
    json_data = requests.get(url + parameter).json()
    return json_data


def all_data(json_data):
    data = []
    for i in range(len(json_data)):
        data += [{"num": json_data[i]["number"],
                  "title": json_data[i]["title"],
                  "link": json_data[i]["html_url"]}]
    return data


def accepted_data(json_data):
    data = []
    for i in range(len(json_data)):
        if json_data[i]["labels"] and \
                json_data[i]["labels"][0]["name"] == 'accepted':
            data += [{"num": json_data[i]["number"],
                     "title": json_data[i]["title"],
                      "link": json_data[i]["html_url"]}]
    return data


def needs_work_data(json_data):
    data = []
    for i in range(len(json_data)):
        if json_data[i]["labels"] and \
                json_data[i]["labels"][0]["name"] == 'needs work':
            data += [{"num": json_data[i]["number"],
                     "title": json_data[i]["title"],
                      "link": json_data[i]["html_url"]}]
    return data


def open_data(json_data):
    data = []
    for i in range(len(json_data)):
        if json_data[i]["state"] == 'open':
            data += [{"num": json_data[i]["number"],
                     "title": json_data[i]["title"],
                      "link": json_data[i]["html_url"]}]
    return data


def closed_data(json_data):
    data = []
    for i in range(len(json_data)):
        if json_data[i]["state"] == 'closed':
            data += [{"num": json_data[i]["number"],
                     "title": json_data[i]["title"],
                      "link": json_data[i]["html_url"]}]
    return data


def get_pulls(state):
    a = response()
    b = all_data(a)
    c = accepted_data(a)
    d = needs_work_data(a)
    e = closed_data(a)
    f = open_data(a)
    if state == 'open':
        return f
    elif state == 'closed':
        return e
    elif state == 'needs work':
        return d
    elif state == 'accepted':
        return c
    else:
        return b
