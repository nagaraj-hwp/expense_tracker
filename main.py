# Creating a simple expense tracker using Python
import calc_total
import file_update


def initiate_expense_calculation():
    expense_type = input("Enter expense type, whether a complete day expense or single expense: ")
    if expense_type == "d" or expense_type == "day":
        input_day = input("Enter date of the expense(YYYY−MM−DD) or just 'today' "
                          "(careful with your expense date input): ")
        expense_date = calc_total.get_expense_date(input_day)
        file_update.add_multiple_expense(expense_date)
        file_update.update_back_up_file()
        calc_total.calculate_day_expense(expense_date)
    elif expense_type == "single" or expense_type == "s":
        input_day = input("Enter which day it should be added to(careful with your expense date input): ")
        expense_date = calc_total.get_expense_date(input_day)
        file_update.add_single_expense(expense_date)
        file_update.update_back_up_file()
    else:
        print("Your choice is not valid or unavailable here")


def initiate_total_calculation():
    unique_day_or_all = input("Specific date expense or month, week or last few days or total expense till date"
                              ": (all / day / month / week / last): ")
    if unique_day_or_all == "all":
        calc_total.calculate_total_amount()
    elif unique_day_or_all == "d" or unique_day_or_all == "day":
        day_to_calculate = calc_total.get_expense_date(input("Enter which day you wants to calculate: "))
        calc_total.calculate_day_expense(day_to_calculate)
    elif unique_day_or_all == "m" or unique_day_or_all == "month":
        month_to_calculate = input("Enter which month you wants to calculate: ")
        if month_to_calculate in calc_total.months_dict1:
            calc_total.calculate_month_expense(month_to_calculate)
        else:
            calc_total.calculate_month_expense(calc_total.months_dict[month_to_calculate.title()])
    elif unique_day_or_all == "w" or unique_day_or_all == "week":
        calc_total.calculate_last_n_days_expense(7)
    elif unique_day_or_all == "l" or unique_day_or_all == "last":
        calc_total.calculate_last_n_days_expense(int(input("Enter number of days wants to calculate: ")))
    else:
        print("Your choice is not valid or unavailable here")


def get_user_action():
    expense_or_total = input("Are you adding expense or want to calculate total: ")
    if expense_or_total == "expense" or expense_or_total == "ex" or expense_or_total == "e":
        initiate_expense_calculation()
    elif expense_or_total == "total" or expense_or_total == "t":
        initiate_total_calculation()


if __name__ == "__main__":
    get_user_action()
