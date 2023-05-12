from database import connection


__all__ = ["get_users", "insert_user", "check_password"]


def get_users(limit: int, offset: int, search_str: str) -> list:
    """
    Attempts to fetch into users table
    based on certain search parameters
    and can handle user fetching by project.

    ::param  limit       str
    ::param  offset      str
    ::param  search_str  str
    """
    sql_query = """
    SELECT
        uuid,
        username,
        created_at
    FROM users
    WHERE deleted_at IS NULL
    """
    params = dict(limit=limit, offset=offset)

    if search_str:
        params["search_str"] = f"{search_str}"
        sql_query += """
        AND LOWER(username) = LOWER(%(search_str)s)
        """

    sql_query += """
    ORDER BY created_at DESC, username ASC
    LIMIT %(limit)s
    OFFSET %(offset)s;
    """

    connection.pool.execute(sql_query, params)
    return connection.pool.fetchall()


def insert_user(username: str, password: str) -> list:
    """
    Attempts to insert a new user record
    within the public.users table.

    ::param username str
    ::param password str
    """
    sql_query = """
    INSERT INTO users (username, password)
    SELECT
        %(username)s,
        crypt(%(password)s, gen_salt('bf'))
    RETURNING
        uuid,
        username,
        created_at;
    """
    params = dict(username=username, password=password)
    connection.pool.execute(sql_query, params)
    return connection.pool.fetchall()


def check_password(username: str, password: str) -> list:
    """
    Attempts to securely compare password
    input against the stored and hashed
    user password.

    ::param username str
    ::param password str
    """
    sql_query = """
    SELECT TRUE
    FROM users
    WHERE deleted_at IS NULL
    AND username = %(username)s
    AND password = crypt(%(password)s, password);
    """
    params = dict(username=username, password=password)
    connection.pool.execute(sql_query, params)
    return connection.pool.fetchall()
