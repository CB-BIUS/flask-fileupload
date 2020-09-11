import os
from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
# SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://CBBIUS:M35R#r#Bng@CBBIUS.mysql.pythonanywhere-services.com/CBBIUS$filecontents".format(
#     username="CBBIUS",
#     password="M35R#r#Bng",
#     hostname="CBBIUS.mysql.pythonanywhere-services.com",
#     databasename="CBBIUS$filecontents",
# )
# app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
# app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# class FileContents(db.Model):

#     __tablename__ = "filecontents"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(300))
#     data = db.Column(db.LargeBinary)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    # file = request.files['inputFile']
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    # newFile = FileContents(name=file.filename, data=file.read())
    # db.session.add(newFile)
    # db.session.commit()

    # return "<h3>Saved " + file.filename + " to the database!</h3>"

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return "<h3>Saved file to the database!</h3>"

if __name__ == '__main__':
    app.run()
