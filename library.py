from flask import Flask, render_template, request

app = Flask(__name__)
import csv


def aviral(number):
    jobs = []
    with open('jobs.csv', newline='') as File:
        reader = csv.reader(File)
        for i, row in enumerate(reader):
            if i in number:
                jobs.append(row[1])
    return jobs


def skills():
    array = []
    with open('jobs.csv', newline='') as File:
        reader = csv.reader(File)
        for i, row in enumerate(reader):
            array.append(row[3][1:][:-1].split(","))
    return array


def user(inp, skillist):
    array = []
    number = []
    for x in inp:
        for i, y in enumerate(skillist):
            if x in y:
                if y not in array:
                    array.append(y)
                    number.append(i)
    return array, number


def inp(posts):
    user_skill = posts.split(",")
    return user_skill

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
        inp(posts)
        return render_template("output.html", post=db_skills)


if __name__ == "__main__":
    app.run(debug=True)
