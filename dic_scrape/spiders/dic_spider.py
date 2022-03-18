import scrapy
import unicodedata

#CSV to word list goes here
import csv

# converts CSV into dictionary
with open('word_list.csv', mode = 'r') as infile:
    reader = csv.reader(infile) 
    with open('word_list_new.csv', mode = 'w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader}
   
   
#converts dictionary into list of keys        
french_words = mydict.keys()
french_words = list(french_words)

# print(french_words[:])

# test_list = ['chaud', 'froid', "mewmew", 'pauvre','bon'] 

#test word 

def clean_vocab(word):
    word = word.encode().decode()
    key = {"%C3%A9": "é", "%20": " ","%C3%A8": "è", "%C3%A2": "â","%C3%A0":"à" }
    for uni in key:
        word.replace(uni, key[uni])
    return word



class PostsSpider(scrapy.Spider):
    # name of spider
    name = "definition"
    
    
    def start_requests(self): 
        # words = french_words
        
        for word in french_words:
            url = 'https://www.larousse.fr/dictionnaires/francais/%s' % word
            yield scrapy.Request(url)         
    
    # returns first list element and writes it to page
    # makes one page per word for now. 
    def parse(self, response):
        #returns object url makes it a string and split at the /
        vocab_item = response.url.split('/')[5]
        #filename = '%s.txt' % vocab_item
        #path = '/home/gear/Documents/funstuff/dic_scrape/text_files/%s' %filename
        # with open(path, mode = 'wt') as f: 
        #     response = response.css('.DivisionDefinition::text').get()
        #     response = str(response)[1:-1]
        #     card_item = {vocab_item : response}
        #     f.write(str(card_item))
        #     f.close()
        with open("master_list", mode = 'a') as f:   
            response = response.css('.DivisionDefinition::text').get()     
            response = str(response)
            response = unicodedata.normalize('NFKD', response)
            vocab_item = clean_vocab(vocab_item)
            card_item = {vocab_item : response}
            f.write(str(card_item))
            f.write('\n')
            f.close()
        
