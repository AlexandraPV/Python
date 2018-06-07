import psycopg2
from db import connect_slave_db , connect_db


def main_db():
    connect_db_master = connect_db()
    cursor = connect_db_master.cursor()
    cursor.execute('SELECT * FROM git')
    all_obj_master = cursor.fetchall()
    connect_db_slave = connect_slave_db()
    cursor_slave = connect_db_slave.cursor()
    print('replecation runnig...')
    for elem in all_obj_master:
        try:
            cursor_slave.execute(
                'INSERT INTO git_slave.git_slave(id , user_id, assembly, c, c_plus_plus, c_sharp, html, css, javascript, php, python, angular2, vue, java, scala) '
                'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                (str(elem[0]),elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], elem[7], elem[8], elem[9], elem[10], elem[11], elem[12], elem[13] , elem[14]))
            connect_db_slave.commit()
            print('Replecation object ...')
        except psycopg2.IntegrityError:
            connect_db_slave.rollback()
            continue
    print('replecation finish')


if __name__ == '__main__':
    main_db()
