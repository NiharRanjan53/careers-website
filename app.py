from flask import Flask, render_template, jsonify

app = Flask("__name__")

JOBS = [{
    'id': 1,
    'title': 'Python Developer',
    'location': 'New York',
    'salary': '$100,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'New York',
    'salary': '$120,000'
}, {
    'id': 3,
    'title': 'Software Engineer',
    'location': 'New York',
    'salary': '$90,000'
}, {
    'id': 4,
    'title': 'Business Analyst',
    'location': 'New York',
    'salary': '$90,000'
}]


@app.route('/')
def home_page():
  return render_template("home.html", JOBS=JOBS)


@app.route('/api/jobs')
def list_job():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
