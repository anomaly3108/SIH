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
        # db_intrests = request.form['intrest']
        # db_parents = request.form['parentrecommendation']
        posts = db_skills
        yo = main.bitch(posts)
        return render_template("output.html", post=yo)


if __name__ == '__main__':
    app.run(debug=True)
