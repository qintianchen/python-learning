import mysql.connector


class MySQL:
    def __init__(self, user, password, host, port, database_name):
        self.conn = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database_name
        )
        self.cursor = self.conn.cursor()

    def execute(self, sql, is_fetch = False):
        # logger.info(f"execute: {sql}")
        self.cursor.execute(sql)
        if is_fetch:
            ret = self.cursor.fetchall()
        else:
            ret = ""
        self.commit()
        return ret

    def insert(self, table_name, data: dict):
        keys = "("
        values = "("
        for key in data:
            keys += key + ","
            if isinstance(data[key], str):
                values += f"'{data[key]}',"
            else:
                values += str(data[key]) + ","
        keys = keys.rstrip(",") + ")"
        values = values.rstrip(",") + ")"
        self.execute(f"insert into {table_name} {keys} values {values}")

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    def get_full_fields(self, table_name):
        ret = self.execute(f"show full fields from {table_name}", is_fetch=True)
        # ret = self.cursor.fetchall()
        return ret

    def check_if_in_table(self, table_name, data, field) -> bool:
        ret = self.get_full_fields(table_name)
        index = 0
        for i in range(len(ret)):
            r = ret[i]
            j = r[0]
            if field == ret[i][0]:
                index = i
                break

        ret = self.execute(f"select * from {table_name}", is_fetch=True)
        # ret = self.cursor.fetchall()
        for r in ret:
            if data == r[index]:
                return True
        return False
