"""
Web verion of url quiz application
reference: https://github.com/rebeccamgriffin/FlaskQuiz

"""

import os
from flask import Flask, render_template, request
app = Flask(__name__)

questions = [
    {
        "id": "1",
        "question": "https://qxf2.com/cost-management/home?#/savings-plans/overview? This gives access overview of saving plans, now how should I access overview of Utilisation report then how should I access it\n- a) https://qxf2.com/cost-management/home?#/utilisation-report/overview?\n" "b) https://qxf2.com/cost-management/home?#/overview/utilisation-report?\n" "c) https://qxf2.com/cost-management/savings-plans?#/home/overview?\n",
        "answers": ["a)", "b)", "c)"],
        "correct": "a)"
    }
]

@app.route("/quiz", methods=['POST', 'GET'])
def quiz():
    if request.method == 'GET':
        return render_template("index.html", data=questions)
    else:
        result = 0
        total = 0
        for question in questions:
            if request.form[question.get('id')] == question.get('correct'):
                result += 1
            total += 1
        return render_template('results.html', total=total, result=result)


if __name__ == "__main__":
    app.run(debug=True)
