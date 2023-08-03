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
