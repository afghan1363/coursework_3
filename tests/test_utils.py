import os.path

from modules import utils

path_for_test = os.path.join("..", "datafiles", "for_test.json")


def test_load_trans_data():
    assert utils.load_trans_data(path_for_test) == [{
        "id": 522357576,
        "state": "EXECUTED",
        "date": "2019-07-12T20:41:47.882230",
        "operationAmount": {
            "amount": "51463.70",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 48894435694657014368",
        "to": "Счет 38976430693692818358"
    }]


def test_format_card_number():
    assert utils.format_card_number("Visa Platinum 2256483756542539") == "Visa Platinum 2256 48** **** 2539"
    assert utils.format_card_number("Visa Gold 2256483756542539") == "Visa Gold 2256 48** **** 2539"


def test_format_account_number():
    assert utils.format_account_number("Счет 48894435694657014368") == "Счет **4368"


def test_format_date():
    assert utils.format_date("2019-07-12T20:41:47.882230") == "12.07.2019"


def test_format_data():
    assert utils.format_data({
        "id": 522357576,
        "state": "EXECUTED",
        "date": "2019-07-12T20:41:47.882230",
        "operationAmount": {
            "amount": "51463.70",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Gold 225648375654253",
        "to": "Счет 38976430693692818358"
    }) == {{
        "id": 522357576,
        "state": "EXECUTED",
        "date": "12.07.2019",
        "operationAmount": {
            "amount": "51463.70",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Gold 2256 48** **** 2539",
        "to": "Счет **4368"
    }}
