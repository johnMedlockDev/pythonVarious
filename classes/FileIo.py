import csv
import json


class FileIo:

    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        f = open(self.filename, 'r')
        print(f.read())

    def append_file(self, text):
        f = open(self.filename, 'a')
        f.write(text)
        f.close()

    def overwrite_file(self, text):
        f = open(self.filename, 'w')
        f.write(text)
        f.close()

    def read_json(self):
        data = json.load(open(self.filename))
        for i in data["name"]:
            print(i)

    def write_json(self, dic):
        with open(self.filename, 'w') as json_file:
            json.dump(dic, json_file)

    def read_csv(self):
        csvfile = open(self.filename)
        readcsv = csv.reader(csvfile, delimiter=',')
        for row in csvfile:
            print(row[0], row[1], row[2])
        csvfile.close()
