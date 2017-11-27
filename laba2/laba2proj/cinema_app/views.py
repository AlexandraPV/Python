from django.shortcuts import render
import _mysql
import csv
from django.db import connection

# Create your views here.
def show(request):
    return render(request, "index.html", {})

def write(request):

    cursor = connection.cursor()
    cursor.execute("""SELECT title FROM testdb.cinema_app_cinema WHERE seats>9""")
    r = cursor.fetchall()

    print(r)

    b = cursor.execute("""SELECT title FROM testdb.cinema_app_cinema WHERE seats>9""")
    print(b)

    with open('/Users/Alisandra/Desktop/3_courses/bd/pro/laba2/laba2proj/seance.csv', 'r+') as data_file:
       reader = csv.DictReader(data_file)

       for row in reader:
           print(row)
           cursor.execute("""INSERT INTO `testdb`.`seance` ( `name_s`, `time`) VALUES ( %s, %s)""",
                          (row['name_s'], row['time']))

           #cursor.execute("""INSERT INTO `testdb`.`cinema_app_cinema` ( `city`, `seats`, `title`) VALUES ( %s, %s, %s)""", (row['city'], row['seats'], row['title']))

           #cursor.execute("""INSERT INTO testdb.cinema_app_cinema ('id', 'city', 'seats', 'title') VALUES ('8', 'jhbhj', '345', 'sdfxcg')""")
               #for key, val in row.items():

              #print(row)

    with open('/Users/Alisandra/Desktop/3_courses/bd/pro/laba2/laba2proj/city.csv', 'r+') as data_file1:
       reader1 = csv.DictReader(data_file1)

       for row in reader1:
           print(row)
           cursor.execute("""INSERT INTO `testdb`.`city` ( `name_c`, `country`) VALUES ( %s, %s)""", (row['name_c'], row['country']))

    return render(request, "index.html", {'b': b})

def delete(request):
    return render(request, "index.html", {})

def update(request):
    return render(request, "index.html", {})

def add(request):
    return render(request, "index.html", {})