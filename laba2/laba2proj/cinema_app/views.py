from django.shortcuts import render, redirect
import _mysql
from django.http import HttpResponseRedirect
import csv
from django.db import connection



# Create your views here.
def show_table():
    cursor = connection.cursor()
    cursor.execute("""SELECT id, title, city_id, seats, seance_id FROM testdb.cinema_app_cinema""")
    list = cursor.fetchall()
    #print(list)

    list_new2 = []
    for i in list:
        cursor.execute("""SELECT name_c FROM testdb.city WHERE id=%s""", i[1])
        p = cursor.fetchall()

        cursor.execute("""SELECT name_s FROM testdb.seance WHERE id=%s""", i[3])
        se = cursor.fetchall()

        list_new = []
        for el in i:
            list_new.append(el)
        #print(list_new)
        for g1 in p:
            for g2 in g1:
                list_new[1] = g2
        for se1 in se:
            for se2 in se1:
                list_new[3] = se2
        #print(list_new)
        list_new2.append(list_new)
    return list_new2

def get_list_title():
    list_new2 = show_table()
    list_tit = []
    for g1 in list_new2:
        list_tit.append(g1[0])
        # print("g1----")
        # print(g1[0])
        # print("--------g1")

    #print(list_tit)
    return list_tit

def show(request):
    list_new2 = show_table()
    list_title = get_list_title()
    # print("list_title----")
    # print(list_title)
    # print("--------list_title")
    return render(request, "index.html", {'list':list_new2, 'list_title':list_title})

def write(request):

    cursor = connection.cursor()
    cursor.execute("""SELECT title FROM testdb.cinema_app_cinema WHERE seats>9""")
    r = cursor.fetchall()

    print(r)

    b = cursor.execute("""SELECT title FROM testdb.cinema_app_cinema WHERE seats>9""")
    print(b)
    cursor.execute("TRUNCATE TABLE testdb.city")
    cursor.execute("TRUNCATE TABLE testdb.seance")
    with open('/Users/Alisandra/Desktop/3_courses/bd/pro/laba2/laba2proj/seance.csv', 'r+') as data_file:
       reader = csv.DictReader(data_file)

       for row in reader:
           print(row)
           cursor.execute("""INSERT INTO `testdb`.`seance` ( `name_s`, `time`, `show`, `about`) VALUES ( %s, %s, %s, %s)""",
                          (row['name_s'], row['time'], row['show'], row['about']))

           #cursor.execute("""INSERT INTO `testdb`.`cinema_app_cinema` ( `city`, `seats`, `title`) VALUES ( %s, %s, %s)""", (row['city'], row['seats'], row['title']))

           #cursor.execute("""INSERT INTO testdb.cinema_app_cinema ('id', 'city', 'seats', 'title') VALUES ('8', 'jhbhj', '345', 'sdfxcg')""")


    with open('/Users/Alisandra/Desktop/3_courses/bd/pro/laba2/laba2proj/city.csv', 'r+') as data_file1:
       reader1 = csv.DictReader(data_file1)

       for row in reader1:
           print(row)
           cursor.execute("""INSERT INTO `testdb`.`city` ( `name_c`, `country`) VALUES ( %s, %s)""", (row['name_c'], row['country']))
           result = "seance.csv and city.csv files were written to DB"
    list = show_table()
    return render(request, "result.html", {'result': result, 'list': list})
    #return redirect("/")

def delete(request):
    if request.method == "POST":
        val = request.POST['val']
        print("val--------")
        print(val)
        print("---------val")

        s=val.replace("[", "")
        s = s.replace("]", "")
        print(s)
        mas = s.split(',')
        print(mas[0])
    #path=request.path
    #print(path)
    cursor = connection.cursor()
    id=mas[0]
    cursor.execute("""DELETE FROM `testdb`.`cinema_app_cinema` WHERE `id`=%s""", id)
    return redirect("/")
    #return render(request, "index.html", {})

def update(request):
    return render(request, "index.html", {})




def add(request):
    cursor = connection.cursor()
    cursor.execute("""SELECT name_s FROM testdb.seance""")

    sean = cursor.fetchall()
    print(sean)
    for i in sean:
        for g in i:
            print(g)
        print(i)

    cursor.execute("""SELECT name_c FROM testdb.city""")

    city = cursor.fetchall()
    print(city)
    for i in city:
        for g in i:
            print(g)
        print(i)
    #cursor.execute("""INSERT INTO `testdb`.`cinema_app_cinema` ( `city_id`, `seats`, `title`, `seance_id` ) VALUES ( %s, 'hj', 'jhbfj', %s)""", (imc, im))
    #cursor.execute("""SELECT city_id, seats, title, seance_id FROM testdb.cinema_app_cinema """)
    #r1 = cursor.fetchall()
    return render(request, "add.html", {'sean' : sean, 'city' : city})

def post_form_add(request):
    cursor = connection.cursor()

    if request.method == "POST":
        title  = request.POST['title']
        cursor.execute("""SELECT id FROM testdb.seance WHERE name_s = %s""", request.POST['seance'])
        seance_id = cursor.fetchall()
        print(seance_id)
        for i in seance_id:
            for g in i:
                print(g)
                seance_id = g

        cursor.execute("""SELECT id FROM testdb.city WHERE name_c = %s""", request.POST['city'])
        city_id = cursor.fetchall()
        print(city_id)
        for i in city_id:
            for g in i:
                print(g)
                city_id = g

        seats = request.POST['seats']
        cursor.execute("""INSERT INTO `testdb`.`cinema_app_cinema` ( `city_id`, `seats`, `title`, `seance_id`) VALUES ( %s, %s, %s, %s)""", (city_id, seats, title, seance_id))

        print(title)
        print(seats)
        print(seance_id)
    #return render(request, "index.html", {})
    return redirect("/")