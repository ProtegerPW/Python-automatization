#! /usr/bin/python3

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableToPrint):

    rowLength = [0] * len(tableToPrint)

    for i in range(len(tableToPrint)):
        for j in range(len(tableToPrint[i])):
            if rowLength[i] < len(tableToPrint[i][j]):
                rowLength[i] = len(tableToPrint[i][j])

    for i in range(len(tableToPrint[0])):
        for j in range(len(tableToPrint)):
            print(tableToPrint[j][i].rjust(rowLength[j]), end="  ")
        print("")

printTable(tableData)