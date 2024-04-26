import psycopg2

host = 'localhost'
user = 'postgres'
password = '12345jn'
database = 'talaba'
port = 5432

conn = psycopg2.connect(host=host,
                        database=database,
                        user=user,
                        password=password,
                        port=port
                        )
cur = conn.cursor()
create_talabalar_table = """
     create table talabalar(
     id serial primary key,
     FISH varchar(50),
     fakulteti varchar(50),
     guruhi int);
     
"""
# cur.execute(create_talabalar_table)
# conn.commit()

insert_talaba = """
   
    insert into talabalar(FISH,fakulteti,guruhi)
    values ('Oroqov Kamoliddin','dastur injinering',232);

"""
# cur.execute(insert_talaba)
# conn.commit()

select_jadval = """
    select * from talabalar;

 """
# cur.execute(select_jadval)
# conn.commit()
# cur.execute(select_jadval)
# for i in cur.fetchall():
#     print(i)

delete_talaba = """
    DELETE FROM talabalar WHERE id = 2;

"""
# cur.execute(delete_talaba)
# conn.commit()





