from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

employees = [
    {"id": 1, "name": "John Doe", "department": "HR"},
    {"id": 2, "name": "Jane Smith", "department": "IT"}
]

@app.route('/')
def index():
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form['name']
    department = request.form['department']
    employees.append({
        "id": len(employees) + 1,
        "name": name,
        "department": department
    })
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
