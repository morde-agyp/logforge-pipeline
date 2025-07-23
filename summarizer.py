# Report Generation
import csv
import json 


def saveTocsv(filename='./data/processed/apache_logs.csv',parsedLogs:dict={}):
    # 1. Save to CSV
    with open(filename, "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=parsedLogs[0].keys())
        writer.writeheader()
        writer.writerows(parsedLogs)


def saveTjson(filename='./data/processed/apache_logs.json',parsedLogs:dict={}):
    # 1. Save to CSV
    with open(filename, "w", newline='') as jsonfile:
        json.dump(parsedLogs, jsonfile, indent=4)
