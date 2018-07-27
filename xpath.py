from scrapy.selector import Selector


with open('test.html','r') as f:
    data = f.read()


    selector = Selector(data)

    r = selector.xpath('/bookstore')
    print(r)



