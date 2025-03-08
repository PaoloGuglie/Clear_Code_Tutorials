import json

data = {
    'Germany': 'Berlin',
    'UK': 'London',
    'China': 'Beijing',
    'Italy': 'Rome'
}

# Use 'with' to work with different files
with open('test_data.txt', 'w') as test_file:
    json.dump(data, test_file)