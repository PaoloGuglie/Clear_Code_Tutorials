import json

with open('test_data.txt') as test_file:
    data = json.load(test_file)  # converts json back to python dictionary
    for entry in data.keys():
        print(entry)
    print("-----")
    for entry in data.values():
        print(entry)
