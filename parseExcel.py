# Import Libraries #
import xlrd
import sqlite3
import os
import csv
import matplotlib.pyplot as plt
import numpy as np
from heapq import nlargest
import getExcel


# Create Memory Database and Database Cursor

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create Database Tables#
cursor.execute(("""CREATE TABLE arrivals_per_month_2011 (
                    month INT,
                    arrivals INT
                    )"""))

cursor.execute(("""CREATE TABLE arrivals_per_month_2012 (
                    month INT,
                    arrivals INT
                    )"""))

cursor.execute(("""CREATE TABLE arrivals_per_month_2013 (
                    month INT,
                    arrivals INT
                    )"""))

cursor.execute(("""CREATE TABLE arrivals_per_month_2014 (
                    month INT,
                    arrivals INT
                    )"""))

cursor.execute(("""CREATE TABLE arrivals_per_month_2015 (
                    month INT,
                    arrivals INT
                    )"""))

cursor.execute(("""CREATE TABLE arrivals_by_transport_2011 (
                    transport TEXT,
                    arrivals INT
                    )"""))

cursor.execute(("""CREATE TABLE arrivals_by_transport_2012 (
                    transport TEXT,
                    arrivals INT
                    )"""))

cursor.execute(("""CREATE TABLE arrivals_by_transport_2013 (
                    transport TEXT,
                    arrivals INT
                    )"""))

cursor.execute(("""CREATE TABLE arrivals_by_transport_2014 (
                    transport TEXT,
                    arrivals INT
                    )"""))

cursor.execute(("""CREATE TABLE arrivals_by_transport_2015 (
                    transport TEXT,
                    arrivals INT
                    )"""))

cursor.execute(("""CREATE TABLE arrivals_by_country_2011 (
                    cname TEXT,
                    arrivals INT
                    )"""))

cursor.execute(("""CREATE TABLE arrivals_by_country_2012 (
                    cname TEXT,
                    arrivals INT
                    )"""))

cursor.execute(("""CREATE TABLE arrivals_by_country_2013 (
                    cname TEXT,
                    arrivals INT
                    )"""))

cursor.execute(("""CREATE TABLE arrivals_by_country_2014 (
                    cname TEXT,
                    arrivals INT
                    )"""))

cursor.execute(("""CREATE TABLE arrivals_by_country_2015 (
                    cname TEXT,
                    arrivals INT
                    )"""))


# Defining our insert functions.
def insert_monthly_data(year, month, arrivals):
    with conn:
        cursor.execute("INSERT INTO arrivals_per_month_"+str(year)+" VALUES(:month, :arrivals)", \
                       {'month': month, 'arrivals': arrivals})


def insert_transport_data(year, transport, arrivals):
    with conn:
        cursor.execute("INSERT INTO arrivals_by_transport_"+str(year)+" VALUES(:transport, :arrivals)", \
                       {'transport': transport, 'arrivals': arrivals})


def insert_country_data(year, cname, arrivals):
    with conn:
        cursor.execute("INSERT INTO arrivals_by_country_"+str(year)+" VALUES(:cname, :arrivals)", \
                       {'cname': cname, 'arrivals': arrivals})


# Defining our getter functions.
def get_by_month(year):
    cursor.execute("SELECT * FROM arrivals_per_month_"+str(year))
    return cursor.fetchall()


def get_arrivals(year, month):
    cursor.execute("SELECT arrivals FROM arrivals_per_month_"+str(year)+" WHERE month = "+str(month))
    return cursor.fetchone()


def get_arrivals_bytransport(year):
    cursor.execute("SELECT arrivals FROM arrivals_by_transport_"+str(year))
    return cursor.fetchall()

def get_arrivals_bycountry(year):
    cursor.execute("SELECT * FROM arrivals_by_country_" + str(year))
    return cursor.fetchall()


# Get workbook
ExcelWrkBook = [0, 1, 2, 3, 4]
ExcelWrkBook[0] = xlrd.open_workbook('transport2011.xls')
ExcelWrkBook[1] = xlrd.open_workbook('transport2012.xls')
ExcelWrkBook[2] = xlrd.open_workbook('transport2013.xls')
ExcelWrkBook[3] = xlrd.open_workbook('transport2014.xls')
ExcelWrkBook[4] = xlrd.open_workbook('transport2015.xls')

# Creating continent specific arrival data lists

europe2011 = []
asia2011 = []
africa2011 = []
america2011 = []
oceania2011 = []

europe2012 = []
asia2012 = []
africa2012 = []
america2012 = []
oceania2012 = []

europe2013 = []
asia2013 = []
africa2013 = []
america2013 = []
oceania2013 = []

europe2014 = []
asia2014 = []
africa2014 = []
america2014 = []
oceania2014 = []

europe2015 = []
asia2015 = []
africa2015 = []
america2015 = []
oceania2015 = []

# Insert from excel workbook and fill the continent specific arrival data lists

ExcelWrkSheet = ExcelWrkBook[0].sheet_by_index(11)
for row in range(76, 109):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    europe2011.insert(0, value)
for row in range(110, 119):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    asia2011.insert(0, value)
for row in range(120, 123):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    africa2011.insert(0, value)
for row in range(124, 130):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    america2011.insert(0, value)
for row in range(131, 133):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    oceania2011.insert(0, value)

ExcelWrkSheet = ExcelWrkBook[1].sheet_by_index(11)
for row in range(78, 111):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    europe2012.insert(0, value)
for row in range(112, 121):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    asia2012.insert(0, value)
for row in range(122, 125):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    africa2012.insert(0, value)
for row in range(126, 132):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    america2012.insert(0, value)
for row in range(133, 135):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    oceania2012.insert(0, value)

ExcelWrkSheet = ExcelWrkBook[2].sheet_by_index(11)
for row in range(78, 112):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    europe2013.insert(0, value)
for row in range(113, 122):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    asia2013.insert(0, value)
for row in range(123, 126):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    africa2013.insert(0, value)
for row in range(127, 133):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    america2013.insert(0, value)
for row in range(134, 136):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    oceania2013.insert(0, value)

ExcelWrkSheet = ExcelWrkBook[3].sheet_by_index(11)
for row in range(78, 112):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    europe2014.insert(0, value)
for row in range(113, 122):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    asia2014.insert(0, value)
for row in range(123, 126):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    africa2014.insert(0, value)
for row in range(127, 133):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    america2014.insert(0, value)
for row in range(134, 136):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    oceania2014.insert(0, value)

ExcelWrkSheet = ExcelWrkBook[4].sheet_by_index(11)
for row in range(77, 112):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    europe2015.insert(0, value)
for row in range(113, 122):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    asia2015.insert(0, value)
for row in range(123, 126):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    africa2015.insert(0, value)
for row in range(127, 133):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    america2015.insert(0, value)
for row in range(134, 136):
    value = int(ExcelWrkSheet.cell(row, 6).value)
    oceania2015.insert(0, value)

# Adding all the continents into a year specific list.
country2011 = europe2011 + asia2011 + africa2011 + america2011 + oceania2011
country2012 = europe2012 + asia2012 + africa2012 + america2012 + oceania2012
country2013 = europe2013 + asia2013 + africa2013 + america2013 + oceania2013
country2014 = europe2014 + asia2014 + africa2014 + america2014 + oceania2014
country2015 = europe2015 + asia2015 + africa2015 + america2015 + oceania2015
top3_2011 = nlargest(3, country2011)
top3_2012 = nlargest(3, country2012)
top3_2013 = nlargest(3, country2013)
top3_2014 = nlargest(3, country2014)
top3_2015 = nlargest(3, country2015)
top3_cname_2011 = [0, 1, 2]
top3_cname_2012 = [0, 1, 2]
top3_cname_2013 = [0, 1, 2]
top3_cname_2014 = [0, 1, 2]
top3_cname_2015 = [0, 1, 2]

ExcelWrkSheet = ExcelWrkBook[0].sheet_by_index(11)
for i in range(0, 3):
    for row in range(76, 134):
        hitrow = int(ExcelWrkSheet.cell(row, 6).value)
        if hitrow == top3_2011[i]:
            cname = str(ExcelWrkSheet.cell(row, 1).value)
            top3_cname_2011[i] = cname
            insert_country_data(2011, cname, hitrow)

print(top3_cname_2011)
ExcelWrkSheet = ExcelWrkBook[1].sheet_by_index(11)
for i in range(0, 3):
    for row in range(78, 136):
        hitrow = int(ExcelWrkSheet.cell(row, 6).value)
        if hitrow == top3_2012[i]:
            cname = str(ExcelWrkSheet.cell(row, 1).value)
            top3_cname_2012[i] = cname
            insert_country_data(2012, cname, hitrow)


ExcelWrkSheet = ExcelWrkBook[2].sheet_by_index(11)
for i in range(0, 3):
    for row in range(78, 136):
        hitrow = int(ExcelWrkSheet.cell(row, 6).value)
        if hitrow == top3_2013[i]:
            cname = str(ExcelWrkSheet.cell(row, 1).value)
            top3_cname_2013[i] = cname
            insert_country_data(2013, cname, hitrow)

ExcelWrkSheet = ExcelWrkBook[3].sheet_by_index(11)
for i in range(0, 3):
    for row in range(78, 136):
        hitrow = int(ExcelWrkSheet.cell(row, 6).value)
        if hitrow == top3_2014[i]:
            cname = str(ExcelWrkSheet.cell(row, 1).value)
            top3_cname_2014[i] = cname
            insert_country_data(2014, cname, hitrow)


ExcelWrkSheet = ExcelWrkBook[4].sheet_by_index(11)
for i in range(0, 3):
    for row in range(77, 136):
        hitrow = int(ExcelWrkSheet.cell(row, 6).value)
        if hitrow == top3_2015[i]:
            cname = str(ExcelWrkSheet.cell(row, 1).value)
            top3_cname_2015[i] = cname
            insert_country_data(2015, cname, hitrow)


# Filling the means of transport database from the excel sheets for transport mean data
for x in range(2011, 2016):
    ExcelWrkSheet = ExcelWrkBook[x - 2011].sheet_by_index(11)
    for i in range(2, 6):
        if x == 2011:
            trans_value = str(ExcelWrkSheet.cell(72, i).value)
            arr_num = int(ExcelWrkSheet.cell(134, i).value)
            insert_transport_data(x, trans_value, arr_num)
        elif x == 2015:
            trans_value = str(ExcelWrkSheet.cell(73, i).value)
            arr_num = int(ExcelWrkSheet.cell(136, i).value)
            insert_transport_data(x, trans_value, arr_num)
        else:
            trans_value = str(ExcelWrkSheet.cell(74, i).value)
            arr_num = int(ExcelWrkSheet.cell(136, i).value)
            insert_transport_data(x, trans_value, arr_num)


# Filling the database from the excel sheets. Total Arrivals
for x in range(2011, 2016):
    for i in range(12):
        if x == 2013 and i < 6:
            # Get sheet
            ExcelWrkSheet = ExcelWrkBook[x-2011].sheet_by_index(i)
            raw_data = int(ExcelWrkSheet.cell(64, 6).value)
            insert_monthly_data(int(x), i+1, raw_data)
        elif x == 2015:
            # Get sheet
            ExcelWrkSheet = ExcelWrkBook[x - 2011].sheet_by_index(i)
            raw_data = int(ExcelWrkSheet.cell(66, 6).value)
            insert_monthly_data(int(x), i + 1, raw_data)
        else:
            # Get sheet
            ExcelWrkSheet = ExcelWrkBook[x - 2011].sheet_by_index(i)
            raw_data = int(ExcelWrkSheet.cell(65, 6).value)
            insert_monthly_data(int(x), i + 1, raw_data)

# CVS Creation
# Creating CVS files for 2011-2015 by transport.
print("Exporting data into CSV............")
cursor = conn.cursor()
for x in range(2011, 2016):
    cursor.execute("SELECT * FROM arrivals_by_transport_"+str(x))
    with open("arrivals_by_transport_"+str(x)+".csv", "w", encoding='utf-16', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter="\t")
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
    dirpath = os.getcwd() + "/arrivals_by_transport_"+str(x)+".csv"
    print("Data exported Successfully into {}".format(dirpath))


# Creating CVS files for 2011-2015 monthly.
print("Exporting data into CSV............")
cursor = conn.cursor()
for x in range(2011, 2016):
    cursor.execute("select * from arrivals_per_month_"+str(x))
    with open("arrival_per_month_"+str(x)+".csv", "w", encoding='utf-16', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter="\t")
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
    dirpath = os.getcwd() + "/arrival_per_month_"+str(x)+".csv"
    print("Data exported Successfully into {}".format(dirpath))

# Creating CVS files for 2011-2015 country contribution.
print("Exporting data into CSV............")
cursor = conn.cursor()
for x in range(2011, 2016):
    cursor.execute("select * from arrivals_by_country_"+str(x))
    with open("arrival_by_country_"+str(x)+".csv", "w", encoding='utf-16', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter="\t")
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
    dirpath = os.getcwd() + "/arrival_by_country_"+str(x)+".csv"
    print("Data exported Successfully into {}".format(dirpath))

# List that holds the arrivals from all the months and all the years. In order to later add it together.
total_arrival_value = []


# Method that adds elements to a list
def arrivallist(num):
    total_arrival_value.insert(0, num)


arrivals_per_year_total = [0, 1, 2, 3, 4]
arrivals_per_trimester_total = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
arrivals_per_transport_total = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# Adding the elements of the databases to the List in order to sum them and then adding them to the per year list.
for x in range(2011, 2016):
    for i in range(1, 12):
        arrlist = get_arrivals(x, i)
        arrivals = int(arrlist[0])
        arrivallist(arrivals)
    arrivals_per_year_total[x - 2011] = sum(total_arrival_value)
    total_arrival_value.clear()

# Adding the elements of the database by transport to the list in order to create the graph
for i in range(0, 4):
    arr = get_arrivals_bytransport(2011)
    arr1 = arr[i]
    arr2 = int(arr1[0])
    arrivals_per_transport_total[i] = arr2
for i in range(4, 8):
    arr = get_arrivals_bytransport(2012)
    arr1 = arr[i - 4]
    arr2 = int(arr1[0])
    arrivals_per_transport_total[i] = arr2
for i in range(8, 12):
    arr = get_arrivals_bytransport(2013)
    arr1 = arr[i - 8]
    arr2 = int(arr1[0])
    arrivals_per_transport_total[i] =arr2
for i in range(12, 16):
    arr = get_arrivals_bytransport(2014)
    arr1 = arr[i - 12]
    arr2 = int(arr1[0])
    arrivals_per_transport_total[i] = arr2
for i in range(16, 20):
    arr = get_arrivals_bytransport(2015)
    arr1 = arr[i - 16]
    arr2 = int(arr1[0])
    arrivals_per_transport_total[i] = arr2


# Adding the elements of the databases to the List in order to get trimester totals


    # 2011 trimesters

for i in range(1, 4):
    arrlist = get_arrivals(2011, i)
    arrivals = int(arrlist[0])
    arrivallist(arrivals)
arrivals_per_trimester_total[0] = sum(total_arrival_value)
total_arrival_value.clear()
for i in range(4, 7):
    arrlist = get_arrivals(2011, i)
    arrivals = int(arrlist[0])
    arrivallist(arrivals)
arrivals_per_trimester_total[1] = sum(total_arrival_value)
total_arrival_value.clear()
for i in range(7, 10):
    arrlist = get_arrivals(2011, i)
    arrivals = int(arrlist[0])
    arrivallist(arrivals)
arrivals_per_trimester_total[2] = sum(total_arrival_value)
total_arrival_value.clear()
for i in range(10, 13):
    arrlist = get_arrivals(2011, i)
    arrivals = int(arrlist[0])
    arrivallist(arrivals)
arrivals_per_trimester_total[3] = sum(total_arrival_value)
total_arrival_value.clear()

#    2012 trimesters
for i in range(1, 4):
    arrlist = get_arrivals(2012, i)
    arrivals = int(arrlist[0])
    arrivallist(arrivals)
arrivals_per_trimester_total[4] = sum(total_arrival_value)
total_arrival_value.clear()
for i in range(4, 7):
    arrlist = get_arrivals(2012, i)
    arrivals = int(arrlist[0])
    arrivallist(arrivals)
arrivals_per_trimester_total[5] = sum(total_arrival_value)
total_arrival_value.clear()
for i in range(7, 10):
    arrlist = get_arrivals(2012, i)
    arrivals = int(arrlist[0])
    arrivallist(arrivals)
arrivals_per_trimester_total[6] = sum(total_arrival_value)
total_arrival_value.clear()
for i in range(10, 13):
    arrlist = get_arrivals(2012, i)
    arrivals = int(arrlist[0])
    arrivallist(arrivals)
arrivals_per_trimester_total[7] = sum(total_arrival_value)
total_arrival_value.clear()

# 2013 trimesters
for i in range(1, 4):
    arrlist = get_arrivals(2013, i)
    arrivals = int(arrlist[0])
    arrivallist(arrivals)
arrivals_per_trimester_total[8] = sum(total_arrival_value)
total_arrival_value.clear()
for i in range(4, 7):
    arrlist = get_arrivals(2013, i)
    arrivals = int(arrlist[0])
    arrivallist(arrivals)
arrivals_per_trimester_total[9] = sum(total_arrival_value)
total_arrival_value.clear()
for i in range(7, 10):
    arrlist = get_arrivals(2013, i)
    arrivals = int(arrlist[0])
    arrivallist(arrivals)
arrivals_per_trimester_total[10] = sum(total_arrival_value)
total_arrival_value.clear()
for i in range(10, 13):
    arrlist = get_arrivals(2013, i)
    arrivals = int(arrlist[0])
    arrivallist(arrivals)
arrivals_per_trimester_total[11] = sum(total_arrival_value)
total_arrival_value.clear()

# 2014 trimesters
for i in range(1, 4):
    arrlist = get_arrivals(2014, i)
    arrivals = int(arrlist[0])
    arrivallist(arrivals)
arrivals_per_trimester_total[12] = sum(total_arrival_value)
total_arrival_value.clear()
for i in range(4, 7):
    arrlist = get_arrivals(2014, i)
    arrivals = int(arrlist[0])
    arrivallist(arrivals)
arrivals_per_trimester_total[13] = sum(total_arrival_value)
total_arrival_value.clear()
for i in range(7, 10):
    arrlist = get_arrivals(2014, i)
    arrivals = int(arrlist[0])
    arrivallist(arrivals)
arrivals_per_trimester_total[14] = sum(total_arrival_value)
total_arrival_value.clear()
for i in range(10, 13):
    arrlist = get_arrivals(2014, i)
    arrivals = int(arrlist[0])
    arrivallist(arrivals)
arrivals_per_trimester_total[15] = sum(total_arrival_value)
total_arrival_value.clear()

# 2015 trimesters
for i in range(1, 4):
    arrlist = get_arrivals(2015, i)
    arrivals = int(arrlist[0])
    arrivallist(arrivals)
arrivals_per_trimester_total[16] = sum(total_arrival_value)
total_arrival_value.clear()
for i in range(4, 7):
    arrlist = get_arrivals(2015, i)
    arrivals = int(arrlist[0])
    arrivallist(arrivals)
arrivals_per_trimester_total[17] = sum(total_arrival_value)
total_arrival_value.clear()
for i in range(7, 10):
    arrlist = get_arrivals(2015, i)
    arrivals = int(arrlist[0])
    arrivallist(arrivals)
arrivals_per_trimester_total[18] = sum(total_arrival_value)
total_arrival_value.clear()
for i in range(10, 13):
    arrlist = get_arrivals(2015, i)
    arrivals = int(arrlist[0])
    arrivallist(arrivals)
arrivals_per_trimester_total[19] = sum(total_arrival_value)
total_arrival_value.clear()

# Graphs


# Taking the results in order to make graphs for 2011-2015 by mean of transport.

trans_means = ['Airplane2011', 'Railway2011', 'Ship2011', 'Road2011', 'Airplane2012', 'Railway2012', 'Ship2012', \
               'Road2012', 'Airplane2013', 'Railway2013', 'Ship2013', 'Road2013', 'Airplane2014', 'Railway2014', \
               'Ship2014', 'Road2014', 'Airplane2015', 'Railway2015', 'Ship2015', 'Road2015']
trans_arrivals = np.arange(len(trans_means))
plt.bar(trans_arrivals, arrivals_per_transport_total, color=(0.2, 0.4, 0.6, 0.6))
plt.yscale("log")
plt.title("Arrivals by mean of transport")
# use the plt.xticks function to custom labels
plt.xticks(trans_arrivals, trans_means, color='orange', rotation=90, fontweight='bold', fontsize='17', horizontalalignment='right')
plt.show()


# Taking the results in order to make graphs for 2011-2015 by trimester total arrivals.
trimesters = ['first2011', 'second2011', 'third2011', 'forth2011', 'first2012', 'second2012', 'third2012', 'forth2012', \
              'first2013', 'second2013', 'third2013', 'forth2013', 'first2014', 'second2014', 'third2014', 'forth2014', \
              'first2015', 'second2015', 'third2015', 'forth2015']

tri_arrivals = np.arange(len(trimesters))
plt.title("Arrivals per trimester between 2011-2015")
plt.yscale("log")
plt.bar(tri_arrivals, arrivals_per_trimester_total, color=(0.2, 0.4, 0.6, 0.6))
# use the plt.xticks function to custom labels
plt.xticks(tri_arrivals, trimesters, color='orange', rotation=90, fontweight='bold', fontsize='17', horizontalalignment='right')
plt.show()


# Taking the results in order to make graphs.
years = [2011, 2012, 2013, 2014, 2015]

y_pos = np.arange(len(years))
plt.yscale("log")
plt.bar(y_pos, arrivals_per_year_total, color=(0.2, 0.4, 0.6, 0.6))
# use the plt.xticks function to custom labels
plt.title("Total arrivals per year between 2011-2015")
plt.xticks(y_pos, years, color='orange', rotation=90, fontweight='bold', fontsize='17', horizontalalignment='right')
plt.show()


# Taking the results in order to make graphs for 2011-2015 top3 country participation.

# Using Pie chart

explode = (0.1, 0, 0)
fig1, ax1 = plt.subplots()
plt.title('2011 Top 3 Country participation')
ax1.pie(top3_2011, explode=explode, labels=top3_cname_2011, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Using Pie chart

explode = (0.1, 0, 0)
fig1, ax1 = plt.subplots()
plt.title('2012 Top 3 Country participation')
ax1.pie(top3_2012, explode=explode, labels=top3_cname_2012, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Using Pie chart

explode = (0.1, 0, 0)
fig1, ax1 = plt.subplots()
plt.title('2013 Top 3 Country participation')
ax1.pie(top3_2013, explode=explode, labels=top3_cname_2013, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Using Pie chart

explode = (0.1, 0, 0)
fig1, ax1 = plt.subplots()
plt.title('2014 Top 3 Country participation')
ax1.pie(top3_2014, explode=explode, labels=top3_cname_2014, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Using Pie chart

explode = (0.1, 0, 0)
fig1, ax1 = plt.subplots()
plt.title('2015 Top 3 Country participation')
ax1.pie(top3_2015, explode=explode, labels=top3_cname_2015, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
