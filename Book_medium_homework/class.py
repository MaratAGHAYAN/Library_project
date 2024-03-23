import random
import re
class Book:
    def __init__(self, title, number_of_buy_or_return, unchanged = None, price = None): # Կոնստրուկտոր
        self.title = title
        self.number_of_buy_or_return = number_of_buy_or_return
        self.unchanged = number_of_buy_or_return
        self.initial_value = number_of_buy_or_return
        self.price = price

    def buy_book(self): # Այս ֆունկցիան կանչելու ժամանակ տվյալ գրքերից պակասելու է մեկ հատ բայց ֆունկցիան աշխատում է այն ժամանակ երբ վաճառողը վերցրել է գրքի գումարը
        if self.number_of_buy_or_return > 0:
            self.number_of_buy_or_return -= 1
            print(f"Did you sell for {self.price}$ ? (yes \ no)")
            yes_no = input()
            if yes_no.lower() == "yes":
                print("\nSold")
                with open ("Book_count.txt", "a") as file: # Ֆայլի մեջ ավտոմատ գրանցվում է թե ինչ գիրք է վաճառվել
                    file.write(f"Bought: {self.title}\n")
                return f"leftover - {self.number_of_buy_or_return}"
            elif yes_no.lower() == "no": 
                print("We only sell at the given price\n")
            else:
                print("wrong!")
        else:
            return f"No this book in the library."
    

    def return_book(self): # Վերցված գիրքը(որի նպատակը կարդալն ու վերադարձնելն է) հանձնվում է գրադարան
        if self.initial_value == self.number_of_buy_or_return: # Եթե կոնկրետ գրքի քանակից ավել են վերադարձնում, տպում է, "Չկա հանձնած գիրք"
            print("No book submitted.")
            return f"leftover - {self.number_of_buy_or_return} "
        self.number_of_buy_or_return += 1
        with open ("Book_count.txt", "a") as file:  # Ֆայլի մեջ ավտոմատ գրանցվում է վերադարձված գիրքը

            file.write(f"Returned: {self.title}\n")
        return f"leftover - {self.number_of_buy_or_return} "
    

    def read_book(self,wich_book):  # Այս ֆունկցիան անվճար գիրք վերցնելու համար է, որի համար հաճախորդը պետք է լինի չափահաս, լինի անձնագրով
            if self.number_of_buy_or_return > 0:
                while True:         
                    passport_number = input("Write to the customer for registration passport number(for example. AA1234567): ")
                    pattern_passport_number = r'^[A-Z]{2}\d{7}$'  # Սա անձնագրի համարի ձևաչափն է, նպատակը՝ համարի քանակից ավել պակաս չգրել և ունի նաև հիասքանչ գործիք որի շնորհիվ պահպանվում է տառերի և թվերի հերթականությունը, քանակը
                    match = re.match(pattern_passport_number, passport_number)
                    if match:  
                        print("The password number is correct.")                
                        while True: # քանի դեռ ճիշտ է անձնագրի համարը այն թույլ կտա ներմուծեք նաև հեռախոսահամարը նույն սկզբունքով
                            number = input("Write to the customer for registration phone number(for example. +37412345678): ")
                            pattern_number = r'^\+\d{11}$'  # հեռախոսահամարի ձևաչափը
                            match_number = re.match(pattern_number, number)
                            if match_number:
                                print("The phone number is correct.")
                                name_surname = str(input("Input the customer Name and Surname: "))
                                with open('customer_info.txt', 'a') as file:  # գրանցվում է ֆայլում հաճախորդի տվյալները և գիրքը
                                    file.write(f"Book: {wich_book}, Name_surname: {name_surname}, Passport Number: {passport_number}, Phone Number: {number}\n")
                                break
                            else:
                                print("Incorrect phone number!")
                        break
                    else: print("Incorrect passport number!")
                self.number_of_buy_or_return -= 1    # եթե գրանցումները ճիշտ է, գրքի քանակից հանվում է մեկ և տրվում հաճախորդին
                with open ("Book_to_read_count.txt", "a") as file:   
                    file.write(f"Obsessed books {self.title}\n")  # հանձնած գրքերը գրվում է առանձին ֆայլում
                return f"leftover - {self.number_of_buy_or_return}"
            else:
                return f"No this book in the library."


def generate_random_read_book(read_books_list):  # այս ֆունկցիան ռանդոմ տարբերակով ընտրում է գրքեր books_for_sale այս ցուցակից
    read_books_copy = read_books_list.copy()  
    random_index = random.randint(0, len(read_books_copy) - 1)
    random_read_book = read_books_copy.pop(random_index)
    return random_read_book


def generate_number(previous_number): # այս ֆունկցիան ռանդոմ տարբերակով գեներացնում է թիվ, որը պետք է պետք է գալու երբ PDF կամ audio տարբերակով գրքերի քանակի համար թե քանի հոգի են օգտվել
    new_number = random.randint(previous_number + 1, previous_number * 2)
    return new_number


generated_number = random.randint(1, 1)   # տողը առաջացնում է պատահական ամբողջ թիվ տվյալ միջակայքում

books_for_sale = [
        Book("Friends, Lovers, and the Big Terrible Thing by Matthew Perry:", 50, 50, 16),
        Book("The Women by Kristin Hannah", 7, 7, 22),
        Book("The Lost Bride Trilogy by Nora Roberts", 37, 37, 22),
        Book("All the Light We Cannot See by Anthony Doerr", 15, 15, 18),
        Book("The Couple Next Door by Shari Lapena", 80, 80, 5),
        Book("Little Women by Louisa May Alcott", 39, 39, 6)
        ]

read_books = [
        Book("The Pilgrim's Progress by John Bunyan", 5),
        Book("Christian's Journey by John Bunyan", 10),
        Book("Gulliver's Travels by Jonathan Swift", 8),
        Book("Clarissa by Samuel Richardson", 15), 
        Book("Journey To Hell by John Bunyan", 3)
        ]



while True:

    print("\n1.Take\n2.Return\n3.Other\n")    # ընտրելով 3 տարբերակներից մեկը առաջարկելու է իր տարբերակները ևս
    getback_sale = (input("\nWrite: "))   # այս փոփոխականը ստունում է այդ բանալինային բառը
                                    
    if getback_sale.lower() == "take": # եթե այդ բառը հավասար է, take ապա այն առաջարկելու է թե անվճար եք վերցնում թե գնում ես եթե անվճար է վերցնում է հաճախորդի տվյալները և տալի գիրքը
        print("paid or free")
        offline_paid_or_free = str(input().lower())
        print("\n")
        if offline_paid_or_free == "paid": # գնում ես գումարով, գումարը տալուց հետո գիրքը տալիս են քեզ
            which_book = int(input("Which book (1 or 2 or 3 or 4 or 5 or 6)? "))
            if 1 <= which_book <= len(books_for_sale):
                selected_book = books_for_sale[which_book - 1]  
                selected_book.buy_book()
            else:
                print("Book not found.")
        elif offline_paid_or_free == "free":  
            which_book = int(input("Which book (1 or 2 or 3 or 4 or 5)? "))
            if 1 <= which_book <= len(read_books):
                selected_book = read_books[which_book - 1] 
                selected_book.read_book(which_book)   
                print("\nGive the book to the customer:\n")         
            else:
                print("Book not found.")

    elif getback_sale.lower() == "return": # եթե բառը ստանում է վերադարձնել ապա ուղղակի հարցնելու է թե որ գիրքն է բայց չի ջնջելու այդ մարդու տվյալները ֆայլից, քանի որ որպես պատմություն պահպանվելու է
        which_book = int(input("Which book (1 or 2 or 3 or 4 or 5)? "))
        if 1 <= which_book <= len(read_books):
            print(read_books[which_book - 1].return_book())
        else:
            print("Book not found.")

    elif getback_sale.lower() == "other":  # եթե բառը ստանում է other ապա առաջարկելու է իր տարբերակները 
        print("  1.List(offline books(titel, price, count))\n  2.Audio and PDF books(titel, price, paid-count)\n  3.Price_online(online books)\n  4.Price_offline(offline books) ")
        unknow = int(input("\nWrite option: "))
        print("\n")

        if unknow == 1:   # ցույց է տալու վաճառքի և կարդալու գրքերի ցանկը
            print("\nBooks for sale\n")
            for index, book in enumerate(books_for_sale, start=1):
                print(f"Book {index}: {book.title} - Count: {book.number_of_buy_or_return}/{book.unchanged} - {book.price}$ ")
            print("\nBooks to raed\n")
            for index, book in enumerate(read_books, start=1):
                print(f"Book {index}: {book.title} - Count: {book.number_of_buy_or_return}/{book.unchanged}")
       
        elif unknow == 2:     # ցույց է տալու PDF և audio ձևաչափով գրքերի ցանկը         
            generated_number = generate_number(generated_number)
            print(f"PDF free: Count: {generated_number}.\n")
            print("PDF fee: ")
            total_price = 0  
            for i in books_for_sale:
                randoom_read_book_fee = generate_random_read_book(books_for_sale)
                generated_number = generate_number(generated_number)
                print(f" Book: {randoom_read_book_fee.title}. Paid: - {randoom_read_book_fee.price}$. Count: {generated_number}.")
            generated_number = generate_number(generated_number)
            print(f"\nAudio free: Count: {generated_number}.\n")
            print("Audio fee: ")
            total_price = 0
            for i in books_for_sale:
                randoom_read_book_fee = generate_random_read_book(books_for_sale)
                generated_number = generate_number(generated_number)
                print(f" Book: {randoom_read_book_fee.title}. Paid: - {randoom_read_book_fee.price}$. Count: {generated_number}.")
        
        elif unknow == 3:   # ցույց է տալու PDF և audio ձևաչափով գնված գրքերից ստացած եկամուտը
            total_price_pdf = 0
            for i in books_for_sale:
                randoom_read_book_fee = generate_random_read_book(books_for_sale)
                total_price_pdf += randoom_read_book_fee.price 
            print(f"PDF: total_price: {total_price_pdf}$") 
            total_price = 0
            for i in books_for_sale:
                randoom_read_book_fee = generate_random_read_book(books_for_sale)
                total_price += randoom_read_book_fee.price  
            print(f"Audio: total_price: {total_price}$")

        elif unknow == 4:   # ցույց է տալու օֆֆլայն տարբերակով գնված գրքերից ստացած եկամուտը
            total_sold_price = sum(book.price * (book.unchanged - book.number_of_buy_or_return) for book in books_for_sale)
            print(f"\nTotal amount earned from offline books sold: {total_sold_price}$")

    else:
        print("Write correctly") 
    if getback_sale.lower() == "wrong":   # եթե կամայական ժամանակ օգտագործողը գրի "wrong" ապա խնդիրը կգա իր սկզբնական ձևի
        continue        
