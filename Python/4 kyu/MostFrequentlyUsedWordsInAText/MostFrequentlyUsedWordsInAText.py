def top_3_words(text):
    words={}
    for p in '!"#$%&()*+,./:;<=>?@[\]^_`{|}~-':
        text = text.replace(p, ' ')
    for w in text.lower().split():
        if w.replace("'", '') != '':
            words[w] = words.get(w, 0) + 1
    return [y[0] for y in sorted(words.items(), key=lambda x: x[1], reverse=True)[:3]]

