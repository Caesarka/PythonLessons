print('Let\'s parse query string.')

while True:
    url = input('Please enter the URL: ')
    if url.__contains__('search?q='):
        search_query = url[url.find('q=') : url.find('&')]
        search_query = search_query.replace('q=', 'q: ')
    else:
        print('There is no query patameter in this URL')
        search_query = 'q: none'


    if url.__contains__('&lang='):
        lang = url[url.find('lang=') : : ]
        lang = lang.replace('lang=', 'lang: ')
    else:
        print('There is no lang patameter in this URL')
        lang = 'lang: none'



    print(search_query)
    print(lang)
    usrInput = input('Enter any key for repeat or q for exit')
    if usrInput == 'q':
        break