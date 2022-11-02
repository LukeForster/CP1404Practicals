def main():
    records = get_records()
    # print(records)
    championships_per_champion, countries = get_champions(records)
    # print(championships_per_champion)
    # print(countries)
    display_champions(championships_per_champion, countries)


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
    championships_per_champion = {}
    countries = set()
    # print(countries)
    for record in records:
        countries.add(record[1])
        try:
            championships_per_champion[record[2]] += 1
        except KeyError:
            championships_per_champion[record[2]] = 1
    return championships_per_champion, countries



def display_champions(championships_per_champion, countries):
    print('Wimbledon champions: ')
    # print(wins_per_champion.items)
    for name, count in championships_per_champion.items():
        print(name, count)
    print('')
    print(f'These {len(countries)} countries have won Wimbledon: ')
    # for country in sorted(countries):
    #     print(', '.join(country))
    print(', '.join(country for country in sorted(countries)))



main()