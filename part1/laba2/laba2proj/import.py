# import csv, sys, os
# from laba2proj.laba2proj import settings
# project_dir="/Users/Alisandra/Desktop/3_courses/bd/pro/laba2/laba2proj/cinema_app"
# sys.path.append(project_dir)
# os.environ['DJANGO_SETTINGS_MODULE'] = settings
#
# import django
# django.setup()
# from laba2proj.cinema_app.models import Cinema
# data = csv.reader(open("/Users/Alisandra/Desktop/3_courses/bd/pro/laba2/laba2proj/test.csv"), delimiter=",")
# print(data)
# for row in data:
#     if row[0] != 'create_date':
#         post = Pos


with open('/Users/Alisandra/Desktop/3_courses/bd/pro/laba2/laba2proj/test.csv', 'r+') as data_file:
    for row in data_file:
        print(row)