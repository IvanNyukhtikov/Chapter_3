
def single_root_words(root_word, *other_words, same_words=None):
    same_words = []
    for i in other_words:
        if i.lower().find(root_word.lower()) != -1 or i.lower() in root_word.lower():
            same_words.append(i)
    print(same_words)

single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')