# Python reading files
import json
import csv

file_path = "/home/malikahmadrasheed/Downloads/output.csv"


try:
            with open(file_path,mode="r") as file:
                   
                   content = csv.reader(file)
                   for line in content:
                    print(line[0])
                   # content = json.load(file)
                   # content = file.read()
                   # print(content["name"])

except FileNotFoundError:
        print("File Not Found")

except PermissionError:
        print("Permission Denied")