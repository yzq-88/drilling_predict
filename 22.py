import psycopg2

def create_connection():
    try:
        # 设置数据库连接信息
        connection = psycopg2.connect(
            dbname="ok",
            user="postgres",
            password="123456",
            host="localhost",  # 通常为"localhost"或具体服务器IP地址
            port="5432"  # 默认端口号为5432
        )

        print("Connection to PostgreSQL DB successful")
        return connection

    except Exception as error:
        print(f"The error '{error}' occurred")

def close_connection(connection):
    connection.close()
    print("Connection closed")

# 使用示例
connection = create_connection()

# 在此处执行您的数据库操作，例如查询或插入

close_connection(connection)
