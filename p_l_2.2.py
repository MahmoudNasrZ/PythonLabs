#! /usr/bin/python3
import json
import re
from datetime import datetime

USERS_FILE = "users.json"
PROJECTS_FILE = "projects.json"

def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def is_valid_email(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)

def is_valid_phone(phone):
    return re.match(r"^01[0-2,5]{1}[0-9]{8}$", phone)

def register():
    users = load_data(USERS_FILE)
    email = input("Email: ")
    if not is_valid_email(email):
        print("Invalid email!")
        return
    password = input("Password: ")
    if password != input("Confirm Password: "):
        print("Passwords do not match!")
        return
    phone = input("Mobile Number: ")
    if not is_valid_phone(phone):
        print("Invalid phone number!")
        return
    if any(user['email'] == email for user in users):
        print("Email already registered!")
        return
    users.append({"email": email, "password": password, "phone": phone, "activated": True})
    save_data(USERS_FILE, users)
    print("Registration successful!")

def login():
    users = load_data(USERS_FILE)
    email = input("Email: ")
    password = input("Password: ")
    for user in users:
        if user['email'] == email and user['password'] == password:
            print("Login successful!")
            return email
    print("Invalid credentials!")
    return None

def create_project(user_email):
    projects = load_data(PROJECTS_FILE)
    title = input("Project Title: ")
    details = input("Project Details: ")
    try:
        target = int(input("Target Amount: "))
        if target <= 0:
            raise ValueError
    except ValueError:
        print("Invalid amount!")
        return
    start_date = input("Start Date (YYYY-MM-DD): ")
    end_date = input("End Date (YYYY-MM-DD): ")
    try:
        if datetime.strptime(start_date, "%Y-%m-%d") >= datetime.strptime(end_date, "%Y-%m-%d"):
            print("Invalid date range!")
            return
    except ValueError:
        print("Invalid date format!")
        return
    projects.append({"title": title, "details": details, "target": target, "start_date": start_date, "end_date": end_date, "owner": user_email})
    save_data(PROJECTS_FILE, projects)
    print("Project created successfully!")

def view_projects():
    projects = load_data(PROJECTS_FILE)
    if not projects:
        print("No projects available.")
        return
    for project in projects:
        print(f"{project['title']} - Target: {project['target']}")

def search_project():
    projects = load_data(PROJECTS_FILE)
    search_date = input("Search by Date (YYYY-MM-DD): ")
    try:
        results = [p for p in projects if p['start_date'] == search_date]
    except ValueError:
        print("Invalid date format!")
        return
    if not results:
        print("No projects found.")
        return
    for project in results:
        print(f"{project['title']} - Target: {project['target']}")

def main():
    while True:
        print("\nCrowdfunding App")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                while True:
                    print("\n1. Create Project")
                    print("2. View Projects")
                    print("3. Search Projects")
                    print("4. Logout")
                    user_choice = input("Choose an option: ")
                    if user_choice == "1":
                        create_project(user)
                    elif user_choice == "2":
                        view_projects()
                    elif user_choice == "3":
                        search_project()
                    elif user_choice == "4":
                        break
                    else:
                        print("Invalid choice!")
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()