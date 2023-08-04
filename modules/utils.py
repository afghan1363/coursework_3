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


def format_card_number(card):
    format_card = card.split(" ")
    card_list = list(format_card[-1])
    card_list[6:12] = "*" * len(card[6:12])
    card_number = "".join(card_list)
    format_card[-1] = ' '.join([card_number[i:i + 4] for i in range(0, len(card_number), 4)])
    hidden_card = " ".join(format_card)
    return hidden_card

def format_account_number(account):
    account_list = account.split(" ")
    account_list[-1] = "*" * 2 + account_list[-1][-4:]
    hidden_account = " ".join(account_list)
    return hidden_account



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
        hide_sender = sender[:-10] + "*" * 6 + sender [-4:]
        hidden_sender = " ".join([hide_sender[i:i-4] for i in range(-1, -12, 4)]) # wrong!!!
        data["from"] = hidden_sender
        receiver = data["to"]
        hidden_receiver = "*" * 2 + receiver[-4:]
        data["to"] = hidden_receiver


