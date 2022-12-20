book = input()
books_checked = 0
is_found = False

curr_book = input()
while curr_book != 'No More Books':
    curr_book = input()
    books_checked += 1

    if curr_book == book:
        is_found = True
        print(f'You checked {books_checked} books and found it.')
        break

if not is_found:
    print('The book you search is not here!')
    print(f'You checked {books_checked} books.')
