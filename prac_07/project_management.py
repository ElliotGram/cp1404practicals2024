import csv
from datetime import datetime
from prac_07.project import Project

"""ETA:1 hour 30 minutes"""
"""CP1404/CP5632 Practical - Project"""


def main():
    projects = []

    # Load projects from default file
    load_projects("projects.txt", projects)

    # Display initial loaded projects
    display_projects(projects)


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


def display_projects(projects):
    if projects:
        print("These are the projects:")
        sorted_projects = sorted(projects, key=lambda x: x.year)
        for project in sorted_projects:
            print(project)
    else:
        print("No projects loaded.")


if __name__ == "__main__":
    main()
