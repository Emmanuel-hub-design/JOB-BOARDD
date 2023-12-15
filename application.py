import click
import sqlite3

@click.command()
def insert_application():
    connection = sqlite3.connect('JOB_BOARDD.db')
    cursor = connection.cursor()
    
    job_id = click.prompt('Enter Job ID', type=int)
    user_id = click.prompt('Enter User ID', type=int)
    cover_letter = click.prompt('Enter Cover Letter', type=str)
    resume = click.prompt('Enter Resume Path', type=str)

    command3 = """CREATE TABLE IF NOT EXISTS application (
                    application_id INTEGER PRIMARY KEY,
                    job_id INTEGER,
                    user_id INTEGER,
                    cover_letter TEXT,
                    resume BLOB,
                    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (job_id) REFERENCES job_title(job_id),
                    FOREIGN KEY (user_id) REFERENCES user(user_id)
                )"""
    cursor.execute(command3)

    insert_application_data = """
        INSERT INTO application (job_id, user_id, cover_letter, resume)
        VALUES (?, ?, ?, ?)
    """
    cursor.execute(insert_application_data, (job_id, user_id, cover_letter, resume))

    cursor.execute("SELECT * FROM application")
    print("\nApplication Table:")
    print(cursor.fetchall())  # Display the data inserted into the application table

    connection.commit()
    connection.close()

if __name__ == '__main__':
    insert_application()
