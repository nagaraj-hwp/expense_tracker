# Creating a simple expense tracker using Python
import datetime as dt
import json
import os
# import re
import shutil

# Can keep an empty json file
WRITEFILE = "../../ignore_dir/expense_log_test.json"


def add_single_expense(date):
    new_expense = {"Amount": int(input("Enter amount you have spent Rs ₹: ")),
                   "Description": input("Enter what you spent for: ")}
    update_expense_file(date, [new_expense])


def update_expense_file(payment_date, expense_list):
    print("payment_date is", payment_date)
    # print("expense list before feeds", expense_list)
    my_day_expense = {payment_date: expense_list}
    a = []
    if not os.path.isfile(WRITEFILE):
        a.append(my_day_expense)
        with open(WRITEFILE, mode='w') as f:
            f.write(json.dumps(a, indent=2))
    else:
        with open(WRITEFILE) as feeds_json:
            feeds = json.load(feeds_json)
            # print("existing feeds", feeds)
            if payment_date in feeds.keys():
                exist = feeds[payment_date]
                # print("exist: ", exist)
                expense_list.extend(exist)
                # print("expense list after feeds", expense_list)
            feeds[payment_date] = expense_list
            # print(feeds)
        with open(WRITEFILE, mode='w') as f:
            f.write(json.dumps(feeds, indent=2))


def add_multiple_expense(date):
    expenses = []
    entry = True
    while entry:
        new_expense = {"Amount": int(input("Enter amount you have spent Rs ₹: ")),
                       "Description": input("Enter what you spent for (Eg: 'Groceries/Travel/Food'): ")}
        expenses.append(new_expense)
        more = input("Is there any more expense to add: ").lower()
        if more == "true" or more == "y" or more == "yes":
            continue
        else:
            entry = False
    update_expense_file(date, expenses)


def get_expense_date(expense_day):
    if expense_day == "today" or expense_day == "td":
        day_to_date = str(dt.date.today())
    elif expense_day == "yesterday" or expense_day == "y":
        today = dt.date.today()
        day_to_date = str(today - dt.timedelta(days=1))
    else:
        # date_match = re.search('((\\d{4})-(\\d{2})-(\\d{2}))', expense_day)
        # expense_date = date_match[0]
        day_to_date = expense_day
    print(f"\nAdding expense for date: {day_to_date}\n")
    return day_to_date


def update_back_up_file():
    shutil.copyfile('../../ignore_dir/expense_log_test.json', '../../ignore_dir/expense_log_test_bkp.json')
    print("Updated backup file.")
