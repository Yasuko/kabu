import lib.pgsql as pgsql

"""
IDトークン取得 auth_refresh

id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
idToken VARCHAR(255) NOT NULL,
createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
"""

class OptionsType:
    refreshtoken: str = ""
    idToken: str = ""

class AuthRefresh:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS auth_refresh (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        idToken VARCHAR(255) NOT NULL,
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    DB=None

    def __init__(self, DB):
        self.DB = DB

    # データを追加する関数
    def create_table(self):
        print('Creating table auth_refresh')
        try:
            self.DB.execute(self.create_table_query)
        except Exception as e:
            print(e)
            exit()


"""
Sample Doc

https://jpx.gitbook.io/j-quants-ja/api-reference/idtoken

"""