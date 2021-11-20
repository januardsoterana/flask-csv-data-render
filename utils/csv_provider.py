import csv

__all__ = ("import_csv", "get_employee_by_id")


def import_csv():
    with open('static/input.csv') as input_csv:
        all_data = csv.DictReader(input_csv)
        return list(all_data)


def get_employee_by_id(driver_id):
    all_data = import_csv()
    employee_data = list(filter(lambda d: d['driver_id'] == driver_id, all_data))
    if employee_data:
        data = employee_data[0]
        convert_data(data)
        return data
    else:
        return None


def convert_data(data):
    data['quit_score'] = int(data['quit_score'])
    data['previous_score'] = int(data['previous_score'])
    data['days_worked'] = int(data['days_worked'])
    data['driving_time_per_week'] = int(data['driving_time_per_week'])
    data['onduty_time_per_week'] = int(data['onduty_time_per_week'])
    data['day_sleep_time_per_week'] = int(data['day_sleep_time_per_week'])
    data['night_sleep_time_per_week'] = int(data['night_sleep_time_per_week'])
