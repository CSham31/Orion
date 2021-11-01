from __future__ import print_function
import csv
import eel
import hungarian_edit
import tsp

# eel.init('web',
#          allowed_extensions=['.js', '.html'])
eel.init("web",
         allowed_extensions=['.js', '.html'])
@eel.expose  # expose this function to Javascript
#assignmnet
def writeToCSV1(data):
    csv_file = open('data1.csv', 'w')
    csv_file.write(data)
    csv_file.close()
    hungarian_edit.main()
    # with open('output1.csv', 'r') as csvfile:
    #     csvreader = csv.reader(csvfile)
    #     string = ""
    #     for row in csvreader:
    #         string += "=>".join(row)+"\n"
    #     print(string)
    #     return string

    # eel.addText(string)
    # eel.sleep(0.1)
    # print(string)


@eel.expose  # expose this function to Javascript
#route
def writeToCSV2(data):
    csv_file = open('data2.csv', 'w')
    csv_file.write(data)
    csv_file.close()
    tsp.main()
    # with open('output1.csv', 'r') as csvfile:
    #     csvreader = csv.reader(csvfile)
    #     string = ""
    #     for row in csvreader:
    #         string += "=>".join(row)+"\n"
    #     print(string)
    #     return string

#TSP
@eel.expose
def readCSV2(): 
    with open('output2.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        string = ""
        for row in csvreader:
            string += "=>".join(row)+"\n"
        print(string)
        return string

#ASSIGNMENT
@eel.expose
def readCSV1():
    with open('output1.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        string = ""
        for row in csvreader:
            string += "=".join(row)+"\n"
        print(string)
        return string


eel.start('home.html')  # start size=(600,600)
