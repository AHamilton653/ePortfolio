# Build a dictionary containing the specified movie collection
movies = [
    {'Title' : 'Munich', 'Director' : 'Steven Spielberg', 'Year' : 2005},
    {'Title' : 'The Prestige', 'Director' : 'Christopher Nolan', 'Year' : 2006}, 
    {'Title' : 'The Departed','Director' : 'Martin Scorsese', 'Year' : 2006},
    {'Title' : 'Into the Wild', 'Director' : 'Sean Penn', 'Year' : 2007},
    {'Title' : 'The Dark Knight', 'Director' : 'Christopher Nolan', 'Year' : 2008},
    {'Title' : 'Mary and Max', 'Director' : 'Adam Elliot', 'Year' : 2009},
    {'Title' : 'The King\'s Speech', 'Director' : 'Tom Hooper', 'Year' : 2010},
    {'Title' : 'The Artist', 'Director' : 'Michel Hazanavicius', 'Year' : 2011}, 
    {'Title' : 'The Help', 'Director' : 'Tate Taylor', 'Year' : 2011},
    {'Title' : 'Argo', 'Director' : 'Ben Affleck', 'Year' : 2012},
    {'Title' : '12 Years a Slave', 'Director' : 'Steve McQueen', 'Year' : 2013},
    {'Title' : 'Birdman', 'Director' : 'Alejandro G. Inarritu', 'Year' : 2014},
    {'Title' : 'Spotlight', 'Director' : 'Tom McCarthy', 'Year' : 2015},
    {'Title' : 'The BFG', 'Director' : 'Steven Spielberg', 'Year' : 2016}
]

# Prompt the user for a year
input_movie = int(input('Enter a year between 2005 and 2016:\n')) - 2005

# Displaying the title(s) and directors(s) from that year
if input_movie < 0 or input_movie > 11:
    print('N/A')
    
for title, director in movies[input_movie].items():
    print('%s, %s' % (title, director))

# Display menu
print('\nMENU\nSort by:\ny - Year\nd - Director\nt - Movie title\nq - Quit')
input_menu = input('\nChoose an option:\n')

# Carry out the desired option: Display movies by year, display movies by director, display movies by movie title, or quit
while input_menu != 'q':
    while input_menu != 'y' and input_menu != 'd' and input_menu != 't' and input_menu != 'q': #added error catching
        input_menu = input('\nERROR: Choose an option:\n')
        
        if input_menu == 'q':
            break
        
    if input_menu == 'q':
        break #end error catching
    
    if input_menu == 'y': #Display by year
        #No sorting required
        prev = None
        for x in range(0, len(movies)):
            if movies[x].get('Year') == prev:
                print('     \t%s, %s' % (movies[x].get('Title'), movies[x].get('Director')))
            else:
                print('%d:\n \t%s, %s' % (movies[x].get('Year'), movies[x].get('Title'), movies[x].get('Director')))
            prev = movies[x].get('Year')
    
    if input_menu == 'd': #display by director
        #sort list and output
        directors = sorted(movies, key = lambda i: i['Director'])
        prev = None
        for x in range(0, len(directors)):
            if directors[x].get('Director') == prev:
                print('\t%s, %d' % (directors[x].get('Title'), directors[x].get('Year')))
            else:
                print('%s:\n \t%s, %d' % (directors[x].get('Director'), directors[x].get('Title'), directors[x].get('Year')))
            prev = directors[x].get('Director')
            
    if input_menu == 't': #Display by title
        #sort list and output
        titles = sorted(movies, key = lambda i: i['Title'])
        for x in range(0, len(titles)):
                print('%s:\n \t%s, %d' % (titles[x].get('Title'), titles[x].get('Director'), titles[x].get('Year')))
                
    print('MENU\nSort by:\ny - Year\nd - Director\nt - Movie title\nq - Quit')
    input_menu = input('\nChoose an option:\n')