from __future__ import print_function
import csv
import eel
import hungarian_edit
import tsp

eel.init('web',
         allowed_extensions=['.js', '.html'])


@eel.expose  # expose this function to Javascript
def writeToCSV(data):
    csv_file = open('data1.csv', 'w')
    csv_file.write(data)
    csv_file.close()
    hungarian_edit.main()
    with open('output.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        string = ""
        for row in csvreader:
            string += "=>".join(row)+"\n"
        print(string)
        return string

    # eel.addText(string)
    # eel.sleep(0.1)
    # print(string)


@eel.expose
def readCSV():
    with open('output.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        string = ""
        for row in csvreader:
            string += "=>".join(row)+"\n"
        print(string)
        return string


eel.start('home.html')  # start size=(600,600)
