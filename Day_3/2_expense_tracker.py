#created by Nazmuz Saif

import csv
from datetime import datetime

from unicodedata import category


def add_expense():
    category = input('Category: ')
    amount = float(input('Amount: '))
    description = input('Description: ')
    date =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open('expenses.csv', 'a') as file:
        file.write(f'{date},{category},{float(amount)},{description}\n')

    print('expense added.')


def view_all():
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.reader(file)
            if len(list(reader)) == 0:
                print('No expenses found.')
                return
            total = 0
            for row in reader:
                total += float(row[2])
                print(f'Time - {row[0]} | Category - {row[1]} | Amount - {float(row[2]):.2f} | Description - {row[3]}')
            print(f'Total - {total:.2f}')
    except FileNotFoundError:
        print('No expenses file!')


def view_by():
    try:
        with open('expenses.csv', 'r') as file:
            reader = file.readlines()
        if len(reader) == 0:
            print('No expenses found.')
            return

        categorys = {}
        for row in reader:
            date, category, amount, description = row.split(',')
            amount = float(amount)

            if category in categorys:
                categorys[category] += amount
            else:
                categorys[category] = amount

        alltotal = 0
        for category, total in categorys.items():
            alltotal += total
            print(f'{category} - {total:.2f}')

        print(f'Total - {alltotal:.2f}')

    except FileNotFoundError:
        print('No expenses file!')


while True:
    print('---EXPENSE TRACKER---')
    print('1. Add Expense')
    print('2. View All Expense')
    print('3. View by Category')
    print('4. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        add_expense()

    elif choice == '2':
        view_all()

    elif choice == '3':
        view_by()

    elif choice == '4':
        print("system off")
        break
    else:
        print('Invalid choice')