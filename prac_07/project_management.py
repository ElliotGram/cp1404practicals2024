import csv
from datetime import datetime
from prac_07.project import Project

"""ETA:1 hour 30 minutes"""
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


def print_menu():
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (Q)uit")


if __name__ == "__main__":
    main()