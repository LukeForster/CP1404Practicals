import wikipedia

title = input('Title: ')
while title != '':
    try:
        print(wikipedia.search(title))
        print(wikipedia.summary(title))
        print(wikipedia.page(title))
        title = input('Title: ')
    except wikipedia.exceptions.DisambiguationError:
        print('Too ambiguous')
        title = input('Title: ')
    except wikipedia.exceptions.PageError:
        print('No Pages')
        title = input('Title: ')

