from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///skill.sqlite3"
db = SQLAlchemy(app)


class Database_skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skills = db.Column(db.String(100), nullable=False)
    intrests = db.Column(db.String(100), nullable=False)
    parents = db.Column(db.String(50))

    def __repr__(self):
        return str(self.id) + self.skills


@app.route("/index", methods=["GET", "POST"])
def database():
    if request.method == "POST":
        db_skills = request.form['skillsearch']
        db_intrests = request.form['intrest']
        db_parents = request.form['parentrecommendation']
        database = Database_skills(skills=db_skills, intrests=db_intrests, parents=db_parents)
        db.session.add(database)
        db.session.commit()
        return redirect('/output')
    else:
        posts = Database_skills.query.all()
        return render_template('output.html', posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
