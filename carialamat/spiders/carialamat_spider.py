import scrapy

class CariAlamatJakartaSpider(scrapy.Spider):
    name = 'carialamat_jakarta'
    protocol = "https://"
    start_urls = [protocol+'carialamat.com/jakarta/1']
    
    curr_page = 1

    def parse(self, response):
        lpage_num = response.css('p.block-paging > a::text')[-1].extract()
        lpage_num = int(lpage_num.strip())
        
        for alamat in response.css("div.hasil-cari"):
            is_exists = alamat.css("h1").extract_first(default=False)
            if is_exists:
                title = alamat.css("h1 > a::text").extract_first()
                text = alamat.css("p::text")[-1].extract()
            
                yield {
                    'name': title,
                    'address': text
                }
                

        self.curr_page = self.curr_page + 1
        
        curr_url = response.url
        curr_url_split = curr_url.split('/')[2:]
        curr_url_split[-1] = str(self.curr_page)
        next_url = self.protocol + '/'.join(curr_url_split)

        next_page = response.urljoin(next_url)
        yield scrapy.Request(next_page, callback=self.parse)
        
        
        
class CariAlamatSpider(scrapy.Spider):
    name = 'carialamat'
    protocol = "https://"
    base_url = "carialamat.com"
    sub_urls = ['jakarta','yogyakarta','surabaya','bandung']
    
    curr_sub_urls_index = 0
    curr_page = 1
    has_next = True
    
    
    start_urls = [
        protocol+base_url+'/'+sub_urls[curr_sub_urls_index]+'/'+str(curr_page),
    ]
    

    def parse(self, response):
        last_page_num  = response.css('p.block-paging > a::text')[-1].extract()
        last_page_num  = int(last_page_num.strip())
        
        for alamat in response.css("div.hasil-cari"):
            is_exists = alamat.css("h1").extract_first(default=False)
            if is_exists:
                title = alamat.css("h1 > a::text").extract_first()
                text = alamat.css("p::text")[-1].extract()
            
                data =  {
                    'name': title,
                    'address': text
                }
                yield data
                
        self.curr_page = self.curr_page + 1
        
        has_next_page = self.curr_page <= last_page_num
        has_next_url = self.curr_sub_urls_index <= len(self.sub_urls)-1
        
        is_last_page_plus_one = (self.curr_page==last_page_num+1) 
        is_last_url = (self.curr_sub_urls_index == len(self.sub_urls)-1)
        
        if (not has_next_page) and has_next_url:
            self.curr_page = 1 # reset counter
            self.curr_sub_urls_index += 1 # go to next sub urls index

        if not (is_last_page_plus_one and is_last_url):
            next_url = self.get_next_url()
            yield scrapy.Request(next_url, callback=self.parse)
        
        
    def get_next_url(self):
        curr_sub_url = self.sub_urls[self.curr_sub_urls_index]
        new_url = f'{self.protocol}{self.base_url}/{curr_sub_url}/{self.curr_page}'
        next_url = new_url
        return next_url
            
            
            
                
        
        