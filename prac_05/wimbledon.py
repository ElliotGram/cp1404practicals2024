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
    champions_count = {}
    for row in data:
        champion = row['Champion']
        if champion in champions_count:
            champions_count[champion] += 1
        else:
            champions_count[champion] = 1
    return champions_count


def get_countries_of_champions(data):
    countries_set = set()
    for row in data:
        countries_set.add(row['Country'])
    countries_list = sorted(countries_set)  # Sort countries alphabetically
    countries_string = ', '.join(countries_list)
    return countries_string


def display_wimbledon_statistics(champions_count, countries_string):
    print("Wimbledon Champions:")
    for champion, count in sorted(champions_count.items()):
        print(f"{champion} {count}")

    print("\nThese countries have won Wimbledon:")
    print(countries_string)
