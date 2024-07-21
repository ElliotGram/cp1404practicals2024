import csv
from datetime import datetime
from prac_07.project import Project

"""ETA:1 hour 30 minutes"""
"""Actual Time: 1hour 45minutes"""
"""CP1404/CP5632 Practical - Project"""

MENU = [
    "- (L)oad projects",
    "- (S)ave projects",
    "- (D)isplay projects",
    "- (F)ilter projects by date",
    "- (A)dd new project",
    "- (U)pdate project",
    "- (Q)uit"
]


def main():
    projects = []

    # Load projects from default file
    load_projects("projects.txt", projects)

    # Display initial loaded projects
    display_projects(projects)
    print(MENU)
    # Initial menu choice
    choice = ""
    while choice != 'q':

        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            load_projects(filename, projects)
            display_projects(projects)
        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            update_project(projects)
            display_projects(projects)
        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? ").lower()
            if save_choice.startswith('y'):
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid choice. Please try again.")


def load_projects(filename, projects):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')
        for row in reader:
            name = row['Name']
            start_date = datetime.strptime(row['Start Date'], '%d/%m/%Y').date()
            priority = int(row['Priority'])
            cost_estimate = float(row['Cost Estimate'])
            completion_percentage = int(row['Completion Percentage'])

            project = Project(name, start_date.year, "", cost_estimate)  # Assuming no arithmetic_sequence in CSV
            projects.append(project)


def save_projects(filename, projects):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerow(['Name', 'Start Date', 'Priority', 'Cost Estimate', 'Completion Percentage'])
        for project in projects:
            writer.writerow([project.name, f"{project.year}", "", f"{project.cost:.2f}", ""])


def display_projects(projects):
    if projects:
        print("These are the projects:")
        sorted_projects = sorted(projects, key=lambda x: x.year)
        for project in sorted_projects:
            print(project)
    else:
        print("No projects loaded.")


def filter_projects_by_date(projects):
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.strptime(date_str, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.year > filter_date.year or (
                project.year == filter_date.year and project.start_date > filter_date)]
        display_projects(filtered_projects)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    date_str = input("Start date (dd/mm/yyyy): ")
    try:
        start_date = datetime.strptime(date_str, "%d/%m/%Y").date()
        priority = int(input("Priority: "))
        cost_estimate = float(input("Cost estimate: $"))
        completion_percentage = int(input("Percent complete: "))

        project = Project(name, start_date.year, "", cost_estimate)  # Assuming no arithmetic_sequence
        projects.append(project)
        print("Project added successfully.")
    except ValueError:
        print("Invalid input format. Please try again.")


def update_project(projects):
    display_projects_with_indices(projects)
    try:
        index = int(input("Project choice: "))
        if 0 <= index < len(projects):
            project = projects[index]
            new_percentage = input(f"New Percentage (leave blank to retain {project.completion_percentage}%): ")
            new_priority = input(f"New Priority (leave blank to retain {project.priority}): ")

            if new_percentage:
                project.completion_percentage = int(new_percentage)
            if new_priority:
                project.priority = int(new_priority)
            print("Project updated successfully.")
        else:
            print("Invalid project choice.")
    except ValueError:
        print("Invalid input. Please enter a valid project index.")


def display_projects_with_indices(projects):
    if projects:
        print("Projects:")
        for i, project in enumerate(projects):
            print(f"{i} {project}")
    else:
        print("No projects loaded.")


if __name__ == "__main__":
    main()
