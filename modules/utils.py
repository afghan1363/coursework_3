import json


def key_to_sort(key):
    """
    For sort by needed key
    :param key: is given in function sort()
    :return: data in given key
    """
    return key["data"]


def load_trans_data(path):
    """
    For load all executed transaction
    :param path: The path to transaction data
    :return: List with executed transactions
    """
    with open(path) as json_data:
        trans_data = json.load(json_data)
        executed_transactions = []
        for data in trans_data:
            if data["state"] == "EXECUTED":
                # parsed_date = data["date"].split("T")[0].replace("-", ".")
                # data["date"] = parsed_date
                executed_transactions.append(data)
    return executed_transactions


def format_data(trans_data):
    """
    Making right format to show
    :param trans_data: List with transaction
    :return: None
    """
    for data in trans_data:
        parsed_date = data["date"].split("T")[0].replace("-", ".")
        data["date"] = parsed_date
        sender = data["from"]
        hide_sender = sender[1:7] + "*" * sender[7:-4] + sender [-4:]
        hidden_sender = " ".join([hide_sender[i:i+4] for i in range(0, len(hide_sender), 4)])
        data["from"] = hidden_sender
        receiver = data["to"]
        hidden_receiver = "*" * receiver[-6:-4] + receiver[-4:]
        data["to"] = hidden_receiver
