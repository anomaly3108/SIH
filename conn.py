from flask import Flask, render_template, request

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
        posts = [db_skills, db_intrests, db_parents]
        return render_template("output.html", post=posts)


if __name__ == '__main__':
    app.run(debug=True)
