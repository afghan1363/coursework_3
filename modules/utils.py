import json


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


def format_date(date):
    date_ext = date.split("T")[0]
    date_formated = ".".join(date_ext.split("-")[::-1])
    return date_formated


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
    :param trans_data: List with transactions
    :return: None
    """

    def key_to_sort(key):
        """
        For sort by needed key
        :param key: is given in function sort()
        :return: data in given key
        """
        return key["data"]

    trans_data.sort(key=key_to_sort, reverse=True)
    for data in trans_data:
        parsed_date = data["date"].split("T")[0].replace("-", ".")
        data["date"] = parsed_date
