"""ETA:1 hour 30 minutes"""
"""CP1404/CP5632 Practical - Basic testing for Guitar class"""
from prac_07.guitar import Project


def main():
    projects = []

    get_project_information(projects)

    display_project(projects)


def get_project_information(projects):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        project_to_add = Project(name, year, cost)
        projects.append(project_to_add)
        print(project_to_add, "added.")
        name = input("Name: ")

    return projects


def display_project(projects):
    if projects:
        print("These are my projects:")
        sorted_projects = sorted(projects, key=lambda x: x.year)


    else:
        print("No projects")


main()
