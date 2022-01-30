"""
a migration with a syntax error
"""

import me_no_existy

import caribou


def upgrade(connection):
    sql = """
        CREATE TABLE games
        ( id    NUMBER
        , name  TEXT
        )"""
    connection.execute(sql)

    sql = """
        CREATE TABLE players
        ( id        NUMBER
        , username  TEXT
        )"""
    connection.execute(sql)


def downgrade(connection):
    for table in ["games", "players"]:
        connection.execute("drop table %s" % table)
