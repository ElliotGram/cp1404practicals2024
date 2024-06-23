def read_csv_file(filename):
    data = []
    with open(filename, 'r', encoding='utf-8-sig') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')  # Extract headers from the first line
        for line in lines[1:]:
            values = line.strip().split(',')
            row = {headers[i]: values[i] for i in range(len(headers))}
            data.append(row)
    return data

def main():
    filename = 'wimbledon.csv'
    data = read_csv_file(filename)
    champions_count = count_wimbledon_champions(data)
    countries_string = get_countries_of_champions(data)
    display_wimbledon_statistics(champions_count, countries_string)

def count_wimbledon_champions(data):

def get_countries_of_champions(data):

def display_wimbledon_statistics(champions_count, countries_string):