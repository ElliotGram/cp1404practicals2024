"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subjects(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Convert the number of students to an integer
        data.append(parts)  # Append the parts to the data list
    input_file.close()
    return data


def display_subjects(data):
    """Display subject details in a formatted way."""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]} students.")


if __name__ == "__main__":
    main()
