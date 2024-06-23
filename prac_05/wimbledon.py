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