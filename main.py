import os.path
from modules.utils import load_trans_data, format_data

path_to_trans_data = os.path.join("datafiles", "operations.json")
trans_data = load_trans_data(path_to_trans_data)
trans_data_formatted = format_data(trans_data)
for data in range(5):
    print(f"{trans_data_formatted[data]['date']} {trans_data_formatted[data]['description']}")
    print(f"{trans_data_formatted[data].get('from', '')} -> {trans_data_formatted[data]['to']}")
    print(f"{trans_data_formatted[data]['operationAmount']['amount']} \
{trans_data_formatted[data]['operationAmount']['currency']['name']}")
    print()
