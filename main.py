import subprocess

def run_spider(spider_name, output_file):
    scrapy_executable = 'C:/Users/alex1/Desktop/DZ9/venv/Scripts/scrapy'
    command = f'{scrapy_executable} crawl {spider_name} -o {output_file}'
    subprocess.run(command, shell=True, cwd='C:/Users/alex1/Desktop/DZ9/quotes_scraper')

if __name__ == '__main__':

    run_spider('quotes_spider', 'quotes.json')

    run_spider('authors_spider', 'authors.json')
