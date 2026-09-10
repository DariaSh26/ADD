#
# import csv
# import requests
#
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = response.json()
#
# with open('todos1.csv', 'w', newline= '') as f:
#     names = ["userId", "id", "title", "completed"]
#     file_writer = csv.DictWriter(f,  delimiter=";", fieldnames=names, lineterminator='\r')
#     file_writer.writeheader()
#     file_writer.writerows(todos)

