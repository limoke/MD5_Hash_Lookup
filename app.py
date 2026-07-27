from flask import Flask, render_template, request
import sqlite3
import re

app = Flask(__name__)

DATABASE = "database.db"
MD5_PATTERN = re.compile(r"^[0-9a-fA-F]{32}$")


def is_valid_md5(value):
    return bool(MD5_PATTERN.match(value))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/lookup", methods=["POST"])
def lookup():

    md5_hash = request.form["md5_hash"].strip().lower()

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()


    cursor.execute(
        "SELECT plaintext FROM hashlist WHERE md5_hash = ?",
        (md5_hash,)
    )


    result = cursor.fetchone()

    connection.close()


    if result:

        plaintext = result[0]

        return render_template(
            "index.html",
            result=f"Plaintext: {plaintext}"
        )


    else:

        return render_template(
            "index.html",
            result="No matching hash identified. Please try again."
        )



if __name__ == "__main__":
    app.run(debug=True)