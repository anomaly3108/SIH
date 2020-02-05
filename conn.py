from flask import Flask, render_template, request
import main

app = Flask(__name__)


@app.route('/')
def student():
    return render_template('index.html')


@app.route('/output', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        db_skills = request.form['skillsearch']
        db_intrests = request.form['intrest']
        db_parents = request.form['parentrecommendation']
        # posts = db_skills
        # user_intrest = db_intrests
        # user_parents = db_parents
        jobs = main.jobs(db_skills)
        intrests = main.from_intrests(db_intrests)
        parents = main.from_parents(db_parents)
        return render_template("output.html", post=jobs, out_intrest=intrests, out_parents=parents,in_skills=db_skills,in_intrest=db_intrests,in_parent=db_parents)


if __name__ == '__main__':
    app.run(debug=True)
