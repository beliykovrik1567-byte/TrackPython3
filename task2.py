# TODO Найдите количество книг, которое можно разместить на дискете
inf_volume = 1.44
pages = 100
strings = 50
symbols_in_string = 25
one_symbol = 4
book_weight = pages*strings*symbols_in_string*one_symbol
book_amount=int (inf_volume*1024*1024/book_weight)
print("Количество книг, помещающихся на дискету:", book_amount)
