from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Americana',
    'salary': 'R$: 3.500,00',
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Nova Odessa',
    'salary': 'R$: 5.500,00',
  },
  {
    'id': 3,
    'title': 'Python Programmer',
    'location': 'Sumaré',
    'salary': 'R$: 6.000,00',
  },
  {
    'id': 4,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'R$: 3.000,00',
  },
]

@app.route('/')
def hello_world():
  return render_template('home.html', 
                         jobs=JOBS,
                        company_name='Luca')

@app.route('/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)