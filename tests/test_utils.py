import os.path
import pathlib
from modules import utils

# path_for_test = os.path.join(os.path.abspath(__file__),"..", "datafiles", "for_test.json")
CURRENT_DIR = os.path.dirname(__file__)
data_path = pathlib.Path(__file__).parent.parent.joinpath("datafiles", "for_test.json")
data_for_test_path = os.path.join(CURRENT_DIR, os.path.pardir, "datafiles", "for_test.json")
data_for_test_path_abs = os.path.abspath(data_for_test_path)
pass


def test_load_trans_data():
    assert utils.load_trans_data(data_path) == [{
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
        "to": "Visa Test 3897643069369281"
    },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }
    ]


def test_format_card_number():
    assert utils.format_card_number("Visa Platinum 2256483756542539") == "Visa Platinum 2256 48** **** 2539"
    assert utils.format_card_number("Visa Gold 2256483756542539") == "Visa Gold 2256 48** **** 2539"


def test_format_account_number():
    assert utils.format_account_number("Счет 48894435694657014368") == "Счет **4368"


def test_format_date():
    assert utils.format_date("2019-07-12T20:41:47.882230") == "12.07.2019"


def test_format_data():
    assert utils.format_data([{
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
        "from": "Visa Gold 2256483756542539",
        "to": "Счет 38976430693692818358"
    }]) == [{
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
        "to": "Счет **8358"
    }]
    assert utils.format_data([{
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
        "to": "Счет 38976430693692818358"
    }]) == [{
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
        "to": "Счет **8358"
    }]
    assert utils.format_data([{
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
        "to": "Visa Test 3897643069369281"
    }]) == [{
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
        "to": "Visa Test 3897 64** **** 9281"
    }]
    assert utils.format_data([{
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
        "from": "Счет 38976430693692818311",
        "to": "Счет 38976430693692818358"
    }]) == [{
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
        "from": "Счет **8311",
        "to": "Счет **8358"
    }]
