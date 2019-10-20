import json


class CountryLinkMaker:
    def __init__(self, file: str, domain='en.wikipedia.org/wiki/'):
        self.file = file
        self.url = f'https://{domain}'
        self.country_list = []
        self.counter = 0
        with open(self.file) as file:
            countries = json.load(file)
            for country in countries:
                self.country_list.append(country['name']['common'])
        self.output = {}

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.country = self.country_list[self.counter]
            self.output[self.country] = f'{self.url}' \
                                        f'{self.country.replace(" ", "_")}'
            self.counter += 1
            return f'{self.country}: ' \
                   f'{self.url}{self.country.replace(" ", "_")}'
        except IndexError:
            raise StopIteration
        finally:
            with open('links_output.json', 'w',
                      encoding='utf-8') as output_file:
                json.dump(self.output, output_file,
                          ensure_ascii=False,
                          indent=2)


if __name__ == '__main__':
    for country_link in CountryLinkMaker('countries.json'):
        print(country_link)
