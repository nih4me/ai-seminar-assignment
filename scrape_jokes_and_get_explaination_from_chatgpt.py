import scrapy
from chatgpt_api import invoke_chatgpt_for_jokes_explaination

# Scaping from 'https://www.countryliving.com/life/entertainment/a36178514/hilariously-funny-jokes/'
class CountryLivingSpider(scrapy.Spider):
    name = 'countrylivingspider'
    start_urls = ['https://www.countryliving.com/life/entertainment/a36178514/hilariously-funny-jokes/']

    def parse(self, response):
        jokes_lists = response.css('ul.et3p2gv0')
        for jokes in jokes_lists:
            for joke in jokes.css('li'):
                joke_content = joke.css('::text').get()
                joke_explaination = invoke_chatgpt_for_jokes_explaination(joke_content)
                yield {
                    'joke': joke_content,
                    'source': 'https://www.countryliving.com',
                    'explaination': joke_explaination
                }