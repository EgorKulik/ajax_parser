import requests
import lxml
import csv


def get_html(url):
    r = requests.get(url)

    return r.text


def write_csv(data):
    with open('ajaks.csv', 'a', encoding='utf-8') as f:
        order = ['name', 'url', 'desc', 'traf', 'percent']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def get_data(html):
    pass


def main():

    for i in range(1, 6051):

        url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'.format(i)
        response = get_html(url).strip()
        d = response.split('\n')[1:]

        for row in d:
            colums = row.strip().split('\t')
            name = colums[0].strip()
            url = colums[1].strip()
            desc = colums[2].strip()
            traf = colums[3].strip()
            percent = colums[4].strip()

            data = {'name':name,
                    'url':url,
                    'desc': desc,
                    'traf': traf,
                    'percent': percent}
            write_csv(data)
            print(colums)


if __name__ == '__main__':
    main()
