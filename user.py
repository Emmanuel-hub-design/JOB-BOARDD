import click
import sqlite3

@click.command()
@click.option('--user_id', prompt='Enter User ID', type=int)
@click.option('--username', prompt='Enter Username')
@click.option('--email', prompt='Enter Email')
@click.option('--password', prompt='Enter Password', hide_input=True, confirmation_prompt=True)
@click.option('--role', prompt='Enter Role')
def insert_user_data(user_id, username, email, password, role):
    connection = sqlite3.connect('JOB_BOARDD.db')
    cursor = connection.cursor()

    command1 = """CREATE TABLE IF NOT EXISTS user (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    email TEXT,
                    password TEXT,
                    role TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )"""
    cursor.execute(command1)

    insert_user_data = """
        INSERT INTO user (user_id, username, email, password, role)
        VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(insert_user_data, (user_id, username, email, password, role))

    cursor.execute("SELECT * FROM user")
    print("\nUser Table:")
    print(cursor.fetchall())

    connection.commit()
    connection.close()

if __name__ == '__main__':
    insert_user_data()
