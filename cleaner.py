__author__ = 'prakhardogra'

def clean(tweet):
    list = []
    cleaned_list = []
    " ".join(tweet.split("\n"))

    for word in tweet.split(" "):
        '''
        if "#" in word:
            word = word.replace("#","")
        if "," in word:
            word = word.replace(",","")
        if "?" in word:
            word = word.replace("?"," ")
        if ":" in word:
            word = word.replace(':','')
        if "'s" in word:
            word = word.replace("'s",'')
        if ")" in word:
            word = word.replace(')','')
        if "(" in word:
            word = word.replace('(','')
        if "\n" in word:
            word = word.replace('\n','')
        '''
        word = word.replace("#","").replace("|","").replace("*","").replace(",","").replace("-"," ").replace("!"," ").replace("?"," ").replace(':','').replace(')','').replace('(','').replace('=','').replace('&amp','').replace('\n','').replace('"','').replace("'","").replace(';','').replace('RT','').replace('_',' ')
        list.append(word.lower())
        list = [x for x in list if not any(c.isdigit() for c in x)]
    string = " ".join(list)
    #print list
    for word in string.split(" "):
        if "http" in word:      # remove links from tweet
            continue
        if "@" in word:     # remove user mentions from tweet
            continue
        if "" == word:
            continue
        while "." in word:
            word = word.replace("."," ")
        if " " == word:
                continue
        while " " in word:
            word = word.replace(" ","")
        if "" == word:
            continue
        cleaned_list.append(word)
    #print cleaned_list
    return " ".join(cleaned_list)

#print clean("#FitnessTrackers seem to be all the rage these days, but are they REALLY helping?\nhttps://t.co/7vmliVWfMw https://t.co/vhoSA2DBtL")