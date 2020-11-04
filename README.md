# carialamat.scrapy
This is a Scrapy project to scrape address from Indonesian Address site at from https://www.carialamat.com/.
This project is only meant for learning scraping web site to get an address from it.

## Extracted Data
This project extract name and address. The extracted data looks like sample :
```
{
    'name': 'PT Victory Global Mandiri', 
    'address': 'Gg Belimbing 12 RT 006/05 Jakarta            '
}
```

## Running The Spiders
You can run a spider using the scrapy crawl command, such as:

```
$ scrapy crawl carialamat
```

If you want to save the scraped data to a file, you can pass the -o option:

```
$ scrapy crawl carialamat -o results/data.json
```