from flask import Flask
from DatabaseCon import Database
app = Flask(__name__)

@app.route("/test", strict_slashes=False)
def testMe():
    con = Database()
    return str(con.selectAll())

if __name__ == '__main__':
    app.run()