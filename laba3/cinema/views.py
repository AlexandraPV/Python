from django.shortcuts import render, redirect
from .models import Cinema , City , Seance
from django.db import connection

def test(request):
    cinema_all = Cinema.objects.all()
    context ={
        'cinema_all': cinema_all
    }
    return render(request , 'index.html' , context)
# Create your views here.

def search(request):
    city_all = City.objects.all()
    seance_all = Seance.objects.all()
    context ={
        'city_list': city_all,
        'city_all': city_all,
        'seance_all': seance_all,
        'seance_list': seance_all,
    }
    return render(request , 'search.html' , context)

def add(request):
    city_all = City.objects.all()
    seance_all = Seance.objects.all()
    context ={
        'city_all': city_all,
        'seance_all': seance_all
    }
    return render(request , 'add.html' , context)

def search_bm(request):
    city_all = City.objects.all()
    seance_all = Seance.objects.all()
    context ={
        'city_all': city_all,
        'seance_all': seance_all
    }
    return render(request , 'search_bm.html' , context)

def update(request):
    if request.method == "POST":
        val = request.POST['val']
        cinema_all = Cinema.objects.all()
        current_cinema = Cinema.objects.get(id=val)
        city_all = City.objects.all().exclude(id=current_cinema.city.id)
        seance_all = Seance.objects.all().exclude(id=current_cinema.seance.id)
        context ={
            'current_cinema': current_cinema,
            'city_all': city_all,
            'seance_all': seance_all,
            'cinema_all': cinema_all
        }
    return render(request , 'update.html' , context)

def post_form_add(request):
    if request.method == "POST":
        title = request.POST['title']
        city_id = request.POST['city']
        seats = request.POST['seats']
        seance_id = request.POST['seance']
        cinema_all = Cinema.objects.all()
        Cinema.objects.create(title=title, seats=seats, city_id =city_id, seance_id=seance_id)


    return redirect("/")

def delete(request):
    if request.method == "POST":
        val = request.POST['val']
        Cinema.objects.get(id=val).delete()


    return redirect("/")

def post_form_update(request):
    if request.method == "POST":
        cin_id = request.POST['id']
        title = request.POST['title']
        city_id = request.POST['city']
        seats = request.POST['seats']
        seance_id = request.POST['seance']
        cinema_all = Cinema.objects.all()
        Cinema.objects.filter(id=cin_id).update(title=title, seats=seats, city_id =city_id, seance_id=seance_id)


    return redirect("/")


def search_city(request):
    if request.method == "POST":
        name_c = request.POST['name_c']
        country = request.POST['country']
        if name_c == "0" and country == "0":
            return redirect("../search")
        elif name_c != "0" and country == "0":
            city = City.objects.filter(name=name_c)

        elif country != "0" and name_c == "0":
            city = City.objects.filter(country=country)

        elif country != "0" and name_c != "0":
            city = City.objects.filter(name=name_c, country=country)
        seance_all = Seance.objects.all()
        city_all = City.objects.all()
        context ={
            'city_list': city_all,
            'city_all': city,
            'seance_all': seance_all,
            'seance_list': seance_all,

        }
    return render(request , 'search.html' , context)


def search_seance(request):
    if request.method == "POST":
        name_s = request.POST['name_s']
        show = request.POST['show']
        time = request.POST['time']
        if name_s == "0" and show == "0" and time == "0":
            return redirect("../search")

        elif name_s != "0" and show == "0" and time == "0":
            sean = Seance.objects.filter(name=name_s)

        elif show != "0" and name_s == "0" and time == "0":
            sean = Seance.objects.filter(show_n=show)

        elif time != "0" and name_s == "0" and show == "0":
            sean = Seance.objects.filter(time=time)

        elif name_s != "0" and show != "0" and time == "0":
            sean = Seance.objects.filter(show_n=show, name=name_s)

        elif name_s == "0" and show != "0" and time != "0":
            sean = Seance.objects.filter(show_n=show, time=time)

        elif name_s != "0" and show == "0" and time != "0":
            sean = Seance.objects.filter(name=name_s, time=time)

        elif show != "0" and name_s != "0" and time != "0":
            sean = Seance.objects.filter(show_n=show, name=name_s, time=time)

        seance_all = Seance.objects.all()
        city_all = City.objects.all()
        context ={
            'city_list': city_all,
            'city_all': city_all,
            'seance_all': sean,
            'seance_list': seance_all,

        }
    return render(request , 'search.html' , context)


def kp(request):
    cursor = connection.cursor()
    cursor.execute("""SELECT cinema.cinema_cinema.id, title, seats FROM cinema.cinema_cinema
INNER JOIN cinema.cinema_seance
ON cinema.cinema_cinema.seance_id = cinema.cinema_seance.id
ORDER by cinema.cinema_seance.time""")
    find_1 = cursor.fetchall()

    cursor.execute("""SELECT DISTINCT id, title, seats FROM cinema.cinema_cinema
WHERE seance_id  IN (
    SELECT id FROM cinema.cinema_seance WHERE show_n = 1
)""")
    find_2 = cursor.fetchall()

    cursor.execute("""SELECT id, title, seats FROM cinema.cinema_cinema
WHERE city_id IN (
SELECT id FROM cinema.cinema_city WHERE country= 'Ukraine')""")
    find_3 = cursor.fetchall()

    cursor.execute("""SELECT cinema.cinema_cinema.id, cinema.cinema_cinema.title, cinema.cinema_cinema.seats, cinema.cinema_seance.name AS seance_name
FROM cinema.cinema_cinema
LEFT OUTER JOIN  cinema.cinema_seance ON cinema.cinema_cinema.seance_id = cinema.cinema_seance.id""")
    find_4 = cursor.fetchall()

    cursor.execute("""SELECT cinema_cinema.id, cinema_cinema.title, cinema_cinema.seats, cinema_seance.name, cinema_seance.time, cinema_seance.show_n, cinema_seance.about from cinema.cinema_cinema 
    left join (select * from cinema.cinema_seance where show_n=1) 
    cinema_seance ON cinema.cinema_cinema.seance_id = cinema.cinema_seance.id 
    where Not name = 'None'
    order by time""")
    find_5 = cursor.fetchall()

    cursor.execute("""SELECT id,title,seats FROM cinema.cinema_cinema
WHERE seats > (
   SELECT AVG(seats) 
      FROM cinema.cinema_cinema
)""")
    find_6 = cursor.fetchall()

    cursor.execute("""SELECT cinema.cinema_city.country, cinema.cinema_city.name AS city_name
FROM cinema.cinema_cinema
LEFT OUTER JOIN  cinema.cinema_city ON cinema.cinema_cinema.city_id = cinema.cinema_city.id

WHERE seats < (
   SELECT AVG(seats) 
      FROM cinema.cinema_cinema
) group by city_id""")
    find_7 = cursor.fetchall()

    cinema_all = Cinema.objects.all()
    context = {
        'find_1': find_1,
        'find_2': find_2,
        'find_3': find_3,
        'find_4': find_4,
        'find_5': find_5,
        'find_6': find_6,
        'find_7': find_7,
        'cinema_all': cinema_all
    }
    return render(request, 'kp.html', context)