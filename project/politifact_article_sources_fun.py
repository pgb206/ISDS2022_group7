source_block = article.find(class_='m-superbox__content')\
                    .find_all('p') #Find article's source block and paragraphs

source_body = []
source_link = []

for paragraph in source_block:
    source_body.append(paragraph.text) #Find text in source paragraph and append

for paragraph in source_block:
    try:
        source_link.append(paragraph.a['href']) #append link if it's there
    except:
        continue
    source_link.append('No link') #Append 'no link' if there's no url. 
                                    #Is this how we wanna do it??