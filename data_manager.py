import connection

@connection.connection_handler
def insert_new_user(cursor, name, score):
    cursor.execute("""
    insert into "users"(username, scores)
    values (%(name)s,%(score)s)""",
                   {'name':name, 'score':score})


@connection.connection_handler
def get_top_users(cursor):
    cursor.execute("""
    select username, scores
    from "users"
    order by scores desc 
    limit 3
    """)
    result = cursor.fetchall()
    return result