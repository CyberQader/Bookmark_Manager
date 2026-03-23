my_favourite_webs = []

maximumwebs = 5
while maximumwebs > 0 :

    web = input(f'Website Name Without https:// :')

    my_favourite_webs.append(f'https://{web.strip().lower()}')
    maximumwebs -=1
    print(f'Website Added {maximumwebs} Place Left')
    print(my_favourite_webs)

else:
    print(f'Book Marks Is Full')

    if len(my_favourite_webs) > 0 :
        my_favourite_webs.sort()
        index=0
        print(f'Printing The List Of Websites In Your BookMark')

        while index < len(my_favourite_webs):
            print(my_favourite_webs[index])
            index +=1
            print(f'Completed successfully!')