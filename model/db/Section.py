import lib.pgsql as pgsql

"""
市場一部        : TSE1st
市場二部        : TSE2nd
マザーズ        : TSEMothers
JASDAQ          : TSEJASDAQ
プライム        : TSEPrime
スタンダード    : TSEStandard
グロース        : TSEGrowth
東証および名証  : TokyoNagoya

CREATE TABLE IF NOT EXISTS section (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    code VARCHAR(20) NOT NULL
);
"""

class Section:
    def __init__(self):
        if pgsql.check_connection() == False:
            pgsql.connect()

    def insert (self, data):
        insert_query = """
        INSERT INTO section (name, code)
        VALUES (%s, %s);
        """
        pgsql.execute(insert_query, data)

    def select (self, id):
        select_query = "SELECT * FROM section WHERE id = %s;"
        return pgsql.fetch_one(select_query, (id,))

    def update (self, id, name, code):
        update_query = """
        UPDATE section
        SET name = %s, code = %s
        WHERE id = %s;
        """
        pgsql.execute(update_query, (name, code, id))

    def delete (self, id):
        delete_query = "DELETE FROM section WHERE id = %s;"
        pgsql.execute(delete_query, (id,))

