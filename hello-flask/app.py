
from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello_world():
    db = mysql.connector.connect(
        host="mydb",
        user="root",
        password="my-secret-pw",
        database="mysql"
    )

    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    version = cursor.fetchone()[0]

    cursor.close()
    db.close()

    return f"Hello World! MySQL version: {version}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
