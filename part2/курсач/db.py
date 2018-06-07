import psycopg2
import random
import pandas as pd

def connect_db():
    try:
        conn = psycopg2.connect("dbname='git' user='postgres' host='localhost' password='admin'")
        return conn
    except:
         return "I am unable to connect to the database"



def connect_slave_db():
    try:
        conn_slave  = psycopg2.connect("dbname='git_slave' user='postgres' host='localhost' password='admin'")
        return conn_slave
    except:
        return "I am unable to connect to the database"



def generate_data():
    conn = connect_db()
    cursor = conn.cursor()

    for i in range(100):
        try:
            user_id = 'name'
            assembly = random.uniform(0, 0.15)
            c = random.uniform(0, 0.05)
            c1 = random.uniform(0, 0.05)
            c2 = random.uniform(0, 0.1)
            html = random.uniform(0, 0.1)
            css = random.uniform(0, 0.15)
            javascript = random.uniform(0, 0.1)
            php = random.uniform(0, 0.1)
            python = random.uniform(0, 0.1)
            angular2 = random.uniform(0, 0.1)
            vue = random.uniform(0, 0.1)
            java = random.uniform(0, 0.2)
            scala = random.uniform(0, 0.1)
            if(assembly + c + c1+c2+html+css+javascript+php+python+angular2+vue+java+scala) > 1:
                continue
            else:
                # print(user_id, assembly, c, c1, c2, html, css, javascript, php, python, angular2, vue, java, scala)
                cursor.execute(
                    'INSERT INTO public.git(user_id, assembly, c, c_plus_plus, c_sharp, html, css, javascript, php, python, angular2, vue, java, scala) '
                    'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (user_id, assembly, c, c1, c2, html, css, javascript, php, python, angular2, vue, java, scala))
                conn.commit()
                print('generation object ...')
        except ValueError:
            continue

def read_data():
    df = pd.read_csv('user-languages.csv', escapechar='`', low_memory=True)
    # print(df)
    # # print(df.loc[1,'state'])
    # # print(df.loc[1, 'state_abbreviation'])
    conn = connect_db()
    cursor = conn.cursor()
    for i in range(0,len(df)-1):
        try:
            user_id = df.loc[i, 'user_id']
            assembly = df.loc[i, 'assembly']
            c = df.loc[i, 'c']
            c1 = df.loc[i, 'c++']
            c2 = df.loc[i, 'c#']
            html = df.loc[i, 'html']
            css = df.loc[i, 'css']
            javascript = df.loc[i, 'javascript']
            php = df.loc[i, 'php']
            python = df.loc[i, 'python']
            angular2 = df.loc[i, 'angular2']
            vue = df.loc[i, 'vue']
            java = df.loc[i, 'java']
            scala = df.loc[i, 'scala']
            # print(user_id, assembly, c, c1, c2, html, css, javascript, php, python, angular2, vue, java, scala)
            cursor.execute(
                'INSERT INTO public.git(user_id, assembly, c, c_plus_plus, c_sharp, html, css, javascript, php, python, angular2, vue, java, scala) '
                'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                (user_id, assembly, c, c1, c2, html, css, javascript, php, python, angular2, vue, java, scala))
            conn.commit()
        except ValueError:
             continue


# if __name__ == '__main__':
if __name__ == '__main__':
    connect = connect_slave_db()
    print(__file__.__name__ ,  connect)

    read_data()
    # assembly = random.uniform(0, 0.1)
    # print(assembly)
    generate_data()