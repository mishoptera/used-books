
def popularbrandsfunction(brand_name, title, description):
    popularbrandslist = ['disney','pixar', 'frozen', 'moana', 'toy story',
                     'americangirl', 'american girl',
                     'dr seuss', 'dr. seuss', 'drseuss', 'dr.seuss',
                     'lego', 'sesame street', 'sesamestreet', 'elmo', 'cookie monster', 'big bird',
                     'leap frog', 'leapfrog', 'minecraft', 'mine craft', 'marvel',
                     'spider-man', 'spiderman', 'hulk', 'iron man', 'thor', 'captain america',
                     'wolverine', 'black panther', 'doctor strange', 'captain marvel', 'black widow',
                     'scarlet witch', 'hawkeye', 'daredevil', 'silver surfer', 'avengers', 'xmen',
                     'x-men', 'deadpool', 'eric carle', 'hungry caterpillar', 'ericcarle',
                     'nickelodean', 'starwars', 'star wars', 'jedi', 'yoda', 'darth vader',
                     'winnie-the-pooh', 'winnie the pooh', 'tigger', 'eeyore',
                     'harrypotter', 'harry potter', 'hogwarts', 'dumbledore', 'fanstastic beasts',
                     'diary of a wimpy kid', 'wimpy kid']
    megastring = (str(brand_name) + " " + str(title) + " " + str(description)).lower()
    if any(word in megastring for word in popularbrandslist):
        return(1)
    else:
        return(0)
