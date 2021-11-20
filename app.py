import logging
from datetime import datetime
from flask import Flask, abort, request, redirect
from flask import render_template

from utils.csv_provider import import_csv, get_employee_by_id
from utils.sqlite_provider import save_driver_call, get_driver_calls

app = Flask(__name__)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


def format_datetime(value, format="%d/%m/%Y"):
    if value is None:
        return ""
    dt = datetime.strptime(value, format)
    return dt.strftime('%d %b %Y')


# Register the template filter with the Jinja Environment
app.jinja_env.filters['formatdatetime'] = format_datetime


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile/<driver_id>', methods=['GET', 'POST'])
def profile(driver_id):
    if request.method == 'GET':
        data = get_employee_by_id(driver_id)
        driver_calls = get_driver_calls(driver_id)
        if not data:
            abort(404, description="Resource not found. Driver ID is not correct.")
        return render_template('profile.html', data=data, driver_calls=driver_calls)

    if request.method == 'POST':
        save_driver_call(request.form)
        return redirect(request.url)


@app.route('/employees')
def employees():
    employees_data = import_csv()
    return render_template('employees.html', employees=employees_data)


@app.route('/employee-dashboard')
def employee_dashboard():
    driver_calls = get_driver_calls()
    return render_template('employee-dashboard.html', driver_calls=driver_calls)


if __name__ == '__main__':
    app.run(debug=True)
