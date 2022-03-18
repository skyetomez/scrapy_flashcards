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

print(french_words[:])
