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


def test_format_data():
    assert utils.format_data([{"date": "2019-07-12T20:41:47.882230", "from": "Счет 48894435694657014368",
                              "to": "Счет 38976430693692818358"}]) == [{"date": "12.07.2019", "from": "Счет 4889 44** **** 4368",
                              "to": "Счет **8358"}]
