from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

subjects = {
    "maths": 100, "minor": 100, "oe1": 50, "oe2": 50,
    "iks": 50, "coi": 50, "computer_networks": 50, "c_programming": 50
}

credits = {
    "maths": 4, "minor": 4, "oe1": 2, "oe2": 2,
    "iks": 2, "coi": 2, "computer_networks": 2, "c_programming": 2
}

def get_grade_details(percentage):
    if percentage >= 90:
        return 10
    elif percentage >= 80:
        return 10
    elif percentage >= 70:
        return 9
    elif percentage >= 60:
        return 8
    elif percentage >= 55:
        return 7
    elif percentage >= 50:
        return 6
    elif percentage >= 45:
        return 5
    elif percentage >= 40:
        return 4
    else:
        return 0

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    marks = data["marks"]

    percentages = [
        marks["maths"] * 100 / subjects["maths"],
        marks["minor"] * 100 / subjects["minor"],
        marks["oe1"] * 100 / subjects["oe1"],
        marks["oe2"] * 100 / subjects["oe2"],
        marks["iks"] * 100 / subjects["iks"],
        marks["coi"] * 100 / subjects["coi"],
        marks["computer_networks"] * 100 / subjects["computer_networks"],
        marks["c_programming"] * 100 / subjects["c_programming"],
        60
    ]

    grade_points = [get_grade_details(p) for p in percentages]

    sgpa = (
        grade_points[0] * credits["maths"] +
        grade_points[1] * credits["minor"] +
        grade_points[2] * credits["oe1"] +
        grade_points[3] * credits["oe2"] +
        grade_points[4] * credits["iks"] +
        grade_points[5] * credits["coi"] +
        grade_points[6] * credits["computer_networks"] +
        grade_points[7] * credits["c_programming"] +
        grade_points[8] * 2
    ) / 22

    return jsonify({"sgpa": round(sgpa, 2)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

