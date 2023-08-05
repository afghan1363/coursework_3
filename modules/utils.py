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
            if data.get("state") == "EXECUTED":
                executed_transactions.append(data)
    return executed_transactions


def format_date(date):
    """
    Formats date from Y-m-d to d.m.Y
    :param date: YYYY-mm-ddTh:m:s
    :return: formatted date
    """
    date_ext = date.split("T")[0]
    date_formatted = ".".join(date_ext.split("-")[::-1])
    return date_formatted


def format_card_number(card):
    """
    Hides a card number
    :param card: Number with description
    :return: Hidden number
    """
    format_card = card.split(" ")
    card_list = list(format_card[-1])
    card_list[6:12] = "*" * len(card[6:12])
    card_number = "".join(card_list)
    format_card[-1] = ' '.join([card_number[i:i + 4] for i in range(0, len(card_number), 4)])
    hidden_card = " ".join(format_card)
    return hidden_card


def format_account_number(account):
    """
    Hides an account number
    :param account: Account with description
    :return: Hidden number
    """
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
        return key["date"]

    trans_data.sort(key=key_to_sort, reverse=True)
    for data in trans_data:
        data["date"] = format_date(data["date"])
        if "from" in data:
            if "Счет" in data["from"]:
                data["from"] = format_account_number(data["from"])
            else:
                data["from"] = format_card_number(data["from"])
        if "Счет" in data["to"]:
            data["to"] = format_account_number(data["to"])
        else:
            data["to"] = format_card_number(data["to"])
    return trans_data
