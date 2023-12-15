import click
import sqlite3

@click.command()
@click.option('--user_id', prompt='Enter User ID', type=int)
@click.option('--title', prompt='Enter Job Title')
@click.option('--description', prompt='Enter Job Description')
@click.option('--location', prompt='Enter Job Location')
@click.option('--salary', prompt='Enter Job Salary', type=float)
def insert_job_data(user_id, title, description, location, salary):
    connection = sqlite3.connect('JOB_BOARDD.db')
    cursor = connection.cursor()
    
    command2 = """CREATE TABLE IF NOT EXISTS job_title (
                    job_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    title TEXT,
                    description TEXT,
                    location TEXT,
                    salary REAL,
                    posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES user(user_id)
                )"""
    cursor.execute(command2)

    insert_job_data = """
        INSERT INTO job_title (user_id, title, description, location, salary)
        VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(insert_job_data, (user_id, title, description, location, salary))

    cursor.execute("SELECT * FROM job_title")
    print("\nJob Title Table:")
    print(cursor.fetchall())

    connection.commit()
    connection.close()

if __name__ == '__main__':
    insert_job_data()



