def main():
    records = get_records()
    # print(records)
    champion_to_count, countries = get_champions(records)
    # print(champion_to_count)
    # print(countries)
    display_champions(champion_to_count, countries)


def get_records():
    records = []
    with open('wimbledon.csv','r') as in_file:
        in_file.readline()
        for line in in_file:
            record = line.strip().split(',')
            # print(record)
            records.append(record)
    return records


def get_champions(records):
    champion_to_count = {}
    countries = set()
    # print(countries)
    for record in records:
        countries.add(record[1])
        try:
            champion_to_count[record[2]] += 1
        except KeyError:
             champion_to_count[record[2]] = 1
    return champion_to_count, countries


def display_champions(champion_to_count, countries):
    print('Wimbledon champions: ')
    for name, count in champion_to_count.items():
        print(name, count)
    print('')
    print(f'These {len(countries)} countries have won Wimbledon: ')
    print(", ".join(country for country in sorted(countries)))

main()