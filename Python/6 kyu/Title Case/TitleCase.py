def title_case(title, minor_words = ''):
    if(title == ""):
        return ""
    else:
        title = title.lower()
        title = title.split(' ')
        minor_words = minor_words.lower()
        minor_words = minor_words.split(' ')
        title[0] = title[0].capitalize()
        for i in range(1,len(title)):
            
            if title[i] not in minor_words:
                title[i] = title[i].capitalize() 
        end = " " . join(title)
        return end