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

    list_new2 = []
    for i in list:
        cursor.execute("""SELECT name_c FROM testdb.city WHERE id=%s""", i[2])
        p = cursor.fetchall()

        cursor.execute("""SELECT name_s FROM testdb.seance WHERE id=%s""", i[4])
        se = cursor.fetchall()

        list_new = []
        for el in i:
            list_new.append(el)
        for g1 in p:
            for g2 in g1:
                list_new[2] = g2
        for se1 in se:
            for se2 in se1:
                list_new[4] = se2
        list_new2.append(list_new)
    return list_new2


def get_list_title():
    list_new2 = show_table()
    list_tit = []
    for g1 in list_new2:
        list_tit.append(g1[0])
    return list_tit

def show(request):
    list_new2 = show_table()
    list_title = get_list_title()
    return render(request, "index.html", {'list':list_new2, 'list_title':list_title})

def write(request):

    cursor = connection.cursor()
    cursor.execute("TRUNCATE TABLE testdb.city")
    cursor.execute("TRUNCATE TABLE testdb.seance")
    with open('/Users/Alisandra/Desktop/3_courses/bd/pro/laba2/laba2proj/seance.csv', 'r+') as data_file:
       reader = csv.DictReader(data_file)

       for row in reader:
           cursor.execute("""INSERT INTO `testdb`.`seance` ( `name_s`, `time`, `show_n`, `about`) VALUES ( %s, %s, %s, %s)""",(row['name_s'], row['time'], row['show'], row['about']))

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
        s=val.replace("[", "")
        s = s.replace("]", "")
        mas = s.split(',')

    cursor = connection.cursor()
    id=mas[0]
    cursor.execute("""DELETE FROM `testdb`.`cinema_app_cinema` WHERE `id`=%s""", id)
    return redirect("/")


def update(request):
    if request.method == "POST":
        val = request.POST['val']
        s = val.replace("[", "")
        s = s.replace("]", "")
        mas = s.split(',')
        id = mas[0].replace("'", "")
        id = id.replace("'", "")
        title=mas[1].replace("'", "")
        title = title.replace(" ", "")
        city_n=mas[2].replace("'", "")
        city_n = city_n.replace(" ", "")
        seats=mas[3].replace("'", "")
        seats = seats.replace(" ", "")
        print(seats)
        seance_n = mas[4].replace("'", "")
        seance_n = seance_n.replace(" ", "")
        list_new_city = []
        print(city_n)
        cursor = connection.cursor()
        city_n=str(city_n)
        seance_n=str(seance_n)
        cursor.execute("""SELECT name_c FROM testdb.city WHERE NOT name_c = %s""", city_n)
        city = cursor.fetchall()
        print(city)

        cursor.execute("""SELECT name_s FROM testdb.seance WHERE NOT name_s = %s""", seance_n)
        sean = cursor.fetchall()
        print(sean)

        list = show_table()
        print("id--------")
        print(id)
    return render(request, "update.html", {'id':id, 'title':title, 'city_n':city_n, 'seats':seats, 'seance_n':seance_n, 'list':list, 'sean' : sean, 'city' : city})


def list_city():
    cursor = connection.cursor()
    cursor.execute("""SELECT name_c FROM testdb.city GROUP BY name_c""")
    city = cursor.fetchall()
    return city


def list_seance():
    cursor = connection.cursor()
    cursor.execute("""SELECT name_s FROM testdb.seance GROUP BY name_s""")
    sean = cursor.fetchall()
    return sean

def add(request):
    cursor = connection.cursor()
    cursor.execute("""SELECT name_s FROM testdb.seance GROUP BY name_s""")

    sean = cursor.fetchall()
    print(sean)
    for i in sean:
        for g in i:
            print(g)
        print(i)

    cursor.execute("""SELECT name_c FROM testdb.city GROUP BY name_c""")

    city = cursor.fetchall()
    print(city)
    for i in city:
        for g in i:
            print(g)
        print(i)

    return render(request, "add.html", {'sean' : sean, 'city' : city})

def post_form_add(request):
    cursor = connection.cursor()

    if request.method == "POST":
        title  = request.POST['title']
        cursor.execute("""SELECT id FROM testdb.seance WHERE name_s = %s""", request.POST['seance'])
        seance_id = cursor.fetchall()

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
    return redirect("/")

def post_form_update(request):
    cursor = connection.cursor()

    if request.method == "POST":
        title  = request.POST['title']
        id = request.POST['id']
        print("______id!!!!!!!!")
        print(id)
        cursor.execute("""SELECT id FROM testdb.seance WHERE name_s = %s""", request.POST['seance'])
        seance_id = cursor.fetchall()

        for i in seance_id:
            for g in i:
                print(g)
                seance_id = g

        cursor.execute("""SELECT id FROM testdb.city WHERE name_c = %s""", request.POST['city'])
        city_id = cursor.fetchall()

        for i in city_id:
            for g in i:
                print(g)
                city_id = g


        seats = request.POST['seats']
        cursor.execute("""UPDATE `testdb`.`cinema_app_cinema` SET `title`=%s, `city_id`=%s, `seats`=%s, `seance_id`=%s WHERE `id`= %s""", (title, city_id, seats, seance_id, id))

    return redirect("/")

def list_city_all():
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM testdb.city""")
    list = cursor.fetchall()

    list_new2 = []
    for i in list:

        list_new = []
        for el in i:
            list_new.append(el)

        list_new2.append(list_new)

    city = list_new2
    return city

def list_seance_all():
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM testdb.seance""")
    list = cursor.fetchall()

    list_new2 = []
    for i in list:

        list_new = []
        for el in i:
            list_new.append(el)

        list_new2.append(list_new)

    sean = list_new2
    return sean

def search(request):
    list_new2 = show_table()
    list_title = get_list_title()
    sean = list_seance_all()
    city = list_city_all()

    cursor = connection.cursor()

    cursor.execute("""SELECT name_s FROM testdb.seance GROUP BY name_s""")
    seance_name_list = cursor.fetchall()
    list_new_name_seance = []
    for i in seance_name_list:
        for g in i:
            list_new_name_seance.append(g)

    cursor.execute("""SELECT time FROM testdb.seance GROUP BY time ORDER BY time""")
    seance_time_list = cursor.fetchall()
    list_new_time_seance = []
    for i in seance_time_list:
        for g in i:
            list_new_time_seance.append(g)

    cursor.execute("""SELECT name_c FROM testdb.city GROUP BY name_c""")
    city_name_list = cursor.fetchall()
    list_new_name_city = []
    for i in city_name_list:
        for g in i:
            list_new_name_city.append(g)

    cursor.execute("""SELECT country FROM testdb.city GROUP BY country""")
    city_country_list = cursor.fetchall()
    list_new_country_city = []
    for i in city_country_list:
        for g in i:
            list_new_country_city.append(g)


    return render(request, "search.html", {'list': list_new2, 'list_title': list_title, 'city':city, 'sean':sean, 'seance_time_list':list_new_time_seance, 'seance_name_list':list_new_name_seance,'city_name_list':list_new_name_city, 'list_new_country_city': list_new_country_city })


def search_city(request):
    list_new2 = show_table()
    list_title = get_list_title()
    sean = list_seance_all()


    cursor = connection.cursor()

    cursor.execute("""SELECT name_s FROM testdb.seance GROUP BY name_s""")
    seance_name_list = cursor.fetchall()
    list_new_name_seance = []
    for i in seance_name_list:
        for g in i:
            list_new_name_seance.append(g)

    cursor.execute("""SELECT time FROM testdb.seance GROUP BY time ORDER BY time""")
    seance_time_list = cursor.fetchall()
    list_new_time_seance = []
    for i in seance_time_list:
        for g in i:
            list_new_time_seance.append(g)

    cursor.execute("""SELECT name_c FROM testdb.city GROUP BY name_c""")
    city_name_list = cursor.fetchall()
    list_new_name_city = []
    for i in city_name_list:
        for g in i:
            list_new_name_city.append(g)

    cursor.execute("""SELECT country FROM testdb.city GROUP BY country """)
    city_country_list = cursor.fetchall()
    list_new_country_city = []
    for i in city_country_list:
        for g in i:
            list_new_country_city.append(g)

    if request.method == "POST":
        name_c = request.POST['name_c']
        country = request.POST['country']
        list_city2=[]
        if name_c=="0" and country=="0":
            return redirect("../search")
        elif name_c != "0" and country=="0":
            cursor.execute("""SELECT * FROM testdb.city WHERE name_c = %s""", name_c)
            list_city = cursor.fetchall()
        elif country !="0" and name_c =="0":
            cursor.execute("""SELECT * FROM testdb.city WHERE country = %s""", country)
            list_city = cursor.fetchall()
        elif country != "0" and name_c != "0":
            cursor.execute("""SELECT * FROM testdb.city WHERE country = %s AND name_c = %s""", (country, name_c))
            list_city = cursor.fetchall()

        for i in list_city:

            list_new = []
            for el in i:
                list_new.append(el)

            list_city2.append(list_new)

            city = list_city2
    #return redirect("../search")
    return render(request, "search.html", {'city': city, 'list': list_new2, 'list_title': list_title,'seance_time_list':list_new_time_seance, 'sean':sean, 'seance_name_list':list_new_name_seance,'city_name_list':list_new_name_city, 'list_new_country_city': list_new_country_city})


def search_seance(request):
    list_new2 = show_table()
    list_title = get_list_title()
    city = list_city_all()

    cursor = connection.cursor()

    cursor.execute("""SELECT name_s FROM testdb.seance GROUP BY name_s""")
    seance_name_list = cursor.fetchall()
    list_new_name_seance = []
    for i in seance_name_list:
        for g in i:
            list_new_name_seance.append(g)

    cursor.execute("""SELECT time FROM testdb.seance GROUP BY  time ORDER BY time""")
    seance_time_list = cursor.fetchall()
    list_new_time_seance = []
    for i in seance_time_list:
        for g in i:
            list_new_time_seance.append(g)

    cursor.execute("""SELECT name_c FROM testdb.city GROUP BY name_c""")
    city_name_list = cursor.fetchall()
    list_new_name_city = []
    for i in city_name_list:
        for g in i:
            list_new_name_city.append(g)

    cursor.execute("""SELECT country FROM testdb.city GROUP BY country""")
    city_country_list = cursor.fetchall()
    list_new_country_city = []
    for i in city_country_list:
        for g in i:
            list_new_country_city.append(g)

    if request.method == "POST":
        name_s = request.POST['name_s']
        show = request.POST['show']
        time = request.POST['time']
        print(name_s)
        print(show)
        print(time)
        list_sean2=[]
        list_sean=[]
        if name_s=="0" and show=="0" and time=="0":
            return redirect("../search")

        elif name_s != "0" and show=="0" and time=="0":
            cursor.execute("""SELECT * FROM testdb.seance WHERE name_s = %s""", name_s)
            list_sean = cursor.fetchall()

        elif show !="0" and name_s=="0" and time=="0":
            cursor.execute("""SELECT * FROM testdb.seance WHERE show_n = %s""", show)
            list_sean = cursor.fetchall()

        elif time != "0" and name_s=="0" and show =="0":
            cursor.execute("""SELECT * FROM testdb.seance WHERE time = %s""", time)
            list_sean = cursor.fetchall()

        elif name_s != "0" and show != "0" and time == "0":
            cursor.execute("""SELECT * FROM testdb.seance WHERE name_s = %s AND show_n = %s""", (name_s, show))
            list_sean = cursor.fetchall()

        elif name_s == "0" and show != "0" and time != "0":
            cursor.execute("""SELECT * FROM testdb.seance WHERE show_n = %s AND time = %s""", (show, time))
            list_sean = cursor.fetchall()

        elif show != "0" and name_s != "0" and time != "0":
            cursor.execute("""SELECT * FROM testdb.seance WHERE show_n = %s AND name_s = %s AND time =%s""", (show, name_s, time))
            list_sean = cursor.fetchall()



        for i in list_sean:

            list_new = []
            for el in i:
                list_new.append(el)

            list_sean2.append(list_new)

        sean = list_sean2
    #return redirect("../search")
    return render(request, "search.html", {'sean': sean, 'list': list_new2, 'list_title': list_title, 'city':city, 'seance_name_list':list_new_name_seance, 'seance_time_list':list_new_time_seance, 'city_name_list':list_new_name_city, 'list_new_country_city': list_new_country_city})