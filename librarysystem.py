import csv

class KinChallenge(object):
    def __init__(self):
        self.book_list = []
    '''
        this function opens and reads in a csv file
        and returns a list of dictionaries
    '''
    def create_list_of_dicts(self):
        # open the csv file
        with open("books.csv") as csv_file:
            # read in the csv file into a Dict Reader
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            # create an empty list to hold the result
            #book_list = []
            # loop through each row in the csv reader
            for row in csv_reader:
                # create an empty dictionary
                book_dict = {}
                # loop through each column and value 
                for col, val in row.items():
                    # add key value pair to dictionary
                    book_dict[col] = val
                # make a copy of the dictionary
                book_dict_copy = book_dict.copy()
                # append the copy of the dictioinary to the list
                self.book_list.append(book_dict_copy)
                # clear the book_dict dictionary so it can be used again
                book_dict.clear()

            return self.book_list
        
    '''
        function that compiles the total number 
        of pages read across categories
    '''
    def print_total_pages(self, my_list):
       # set a counter to 0
        pages_read = 0
        # for each item in the list
        for item in self.book_list:
            # get the value of Pages
            pages = int(item['Pages'])
            # if book is fully read then add all pages
            if item['Read'] == 'Fully':
                # add to the total
                pages_read += pages
            # if book is partially read, get half of the pages
            elif item['Read'] == 'Partially':
                half_of_pages = pages//2
                # add to the total
                pages_read += half_of_pages
            # if book is unread then add 0 pages
            elif item['Read'] == 'Unread':
                pages_read += 0

            
        print(f"Total Pages Read: {pages_read}")


    '''
         function that gets the category and 
         add it to each entry in the list of 
         dictionaries
    '''
    def add_text_category(self, book_list):
        # tuple of codes to lookup
        codes = [ 
                (000, 'Computer Science, Information & General Works'),
                (100, 'Philosophy & Psychology'),
                (200, 'Religion'),
                (300, 'Social Sciences'),
                (400, 'Language'),
                (500, 'Pure Science'),
                (600, 'Applied Science'),
                (700, 'Arts & Recreation'),
                (800, 'Literature'),
                (900, 'History & Geography')
            
            ]
        # for each item in the list
        for item in self.book_list:
            # get the first 3 characters of the dewey decimal number
            ddn = item['DDN'][0:3]
            # convert the ddn to an int
            given_code = int(ddn)
    
            # set previous to None
            prev = None
            # for every code and category in codes
            for code, category in codes:
                # if the code in the tuple is bigger than the code we have then break out of the loop
                if code > given_code:
                    break
                # set the previous to the last category
                prev = category
            # add new key value pair(i.e Category:Literature) to the list of dictionaries
            item['Category'] = prev

        return self.book_list

    '''
        function that adds each page count to the categories
    '''
    def get_pagecount_of_each_category(self, book_list):
        # create an empty dictionary object
        final = {}
        # for each book in the dictionary
        for book in self.book_list:
            # get the value of the categories
            get_category = book['Category']
            # set the default of the category to 0
            final.setdefault(get_category, 0)
            # get the pages and convert to an int
            pages = int(book['Pages'])
            
            # if the book is fully read then add all the pages
            if book['Read'] == 'Fully':
                final[get_category] += pages
            # if the book is partially read then add half the pages
            elif book['Read'] == 'Partially':
                final[get_category] += pages // 2
                
        # print by category
        print("By Category:")
        for key, value in final.items():
            if value != 0:
                print(f"     {key}:{value}")


k = KinChallenge()
alist = k.create_list_of_dicts()
k.print_total_pages(alist)
k.add_text_category(alist) 
k.get_pagecount_of_each_category(alist)   

        
