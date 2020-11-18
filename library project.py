
import datetime

def gettime():
    return datetime.datetime.now()


while True:
    print("\n\t---Libarary: Plz Buy Your Book---\n")
    print("1 - Display Book\n2 - Lend Book\n3 - Add Book\n4 - Return Book\n")
    _number = int(input("Enter Your Choice : \n"))
    if _number == 1:
        class Book:
            def __init__(self, p, c, m, h, e, b):
                self.p = p
                self.c = c
                self.m = m
                self.h = h
                self.e = e
                self.b = b

            def wel(self):
                return f"This is All Subject:\n{self.p}\n{self.c}\n{self.m}\n{self.h}\n{self.e}\n{self.b}\n"


        p1 = Book("Physics", "Chemistry", "Math", "History", "English", "Bio")
        print(p1.wel())

    elif _number == 2:
        print("Taking your book for reading ---")
        print("1 - Physics\n2 - Chemistry\n3 - Math\n4 - History\n5 - English\n6 - Bio\n")
        _books = int(input("Plz Take Your Book, Plz choose Your option : "))
        if _books == 1:
            value = "You are Taking Physics Book"
            x = datetime.datetime.now()
            y = x.strftime("%A")
            with open("physics.txt", "a") as op:
                op.write(str([str(gettime())]) + y + ": " + value + "\n")
            print("Thanx for taking this subject and after reading this.\n \tplz Return this Book..")
        elif _books == 2:
            value = "You are Taking Chemistry Book"
            x = datetime.datetime.now()
            y = x.strftime("%A")
            with open("chemistry.txt", "a") as op:
                op.write(str([str(gettime())]) + y + ": " + value + "\n")
            print("Thanx for taking this subject and after reading this.\n \tplz Return this Book..")
        elif _books == 3:
            value = "You are Taking Math Book"
            x = datetime.datetime.now()
            y = x.strftime("%A")
            with open("Math.txt", "a") as op:
                op.write(str([str(gettime())]) + y + ": " + value + "\n")
            print("Thanx for taking this subject and after reading this.\n \tplz Return this Book..")
        elif _books == 4:
            value = "You are Taking History Book"
            x = datetime.datetime.now()
            y = x.strftime("%A")
            with open("History.txt", "a") as op:
                op.write(str([str(gettime())]) + y + ": " + value + "\n")
            print("Thanx for taking this subject and after reading this.\n \tplz Return this Book..")
        elif _books == 5:
            value = "You are Taking English Book"
            x = datetime.datetime.now()
            y = x.strftime("%A")
            with open("English.txt", "a") as op:
                op.write(str([str(gettime())]) + y + ": " + value + "\n")
            print("Thanx for taking this subject and after reading this.\n \tplz Return this Book..")
        elif _books == 6:
            value = "You are Taking Bio Book"
            x = datetime.datetime.now()
            y = x.strftime("%A")
            with open("Bio.txt", "a") as op:
                op.write(str([str(gettime())]) + y + ": " + value + "\n")
            print("Thanx for taking this subject and after reading this.\n \tplz Return this Book..")
        else:
            print("valid input. Plz enter again")

    elif _number == 3:
        print("You can Add your book for Selling ..")
        _add = input("plz Enter Your Books name : ")
        print(f"That's Your books Name : {_add}")
        value = f"{_add} Added sucessfully"
        x = datetime.datetime.now()
        y = x.strftime("%A")
        with open("Add book.txt", "a") as op:
            op.write(str([str(gettime())]) + y + ": " + value + "\n")
        print(f"Your {_add} Added Sucessfully..")

    elif _number == 4:
        print("\t\tReturn Your Book\n")
        print("1 - Physics\n2 - Chemistry\n3 - Math\n4 - History\n5 - English\n6 - Bio\n")
        return_book = int(input("Plz choose your Book : "))
        if return_book == 1:
            print("That's your Book Timing Here when You are Taking this book.")
            with open("physics.txt") as op:
                x = op.read()
                print(x)
            print("1 - Return This Book\n2 - Not")
            _ret = int(input("Type Here : "))
            if _ret == 1:
                value = "Return Physics book"
                x = datetime.datetime.now()
                y = x.strftime("%A")
                with open("returning_book.txt", "a") as op:
                    op.write(str([str(gettime())]) + y + ": " + value + "\n")
                with open("returning_book.txt", "r") as op:
                    x = op.read()
                    print(x)
            elif _ret == 2:
                print("not return your book\n")
                print("Thanx for Choosing")

        if return_book == 2:
            print("That's your Book Timing Here when You are Taking this book.")
            with open("chemistry.txt") as op:
                x = op.read()
                print(x)
            print("1 - Return This Book\n2 - Not")
            _ret = int(input("Type Here : "))
            if _ret == 1:
                value = "Return Chemistry book"
                x = datetime.datetime.now()
                y = x.strftime("%A")
                with open("returning_book.txt", "a") as op:
                    op.write(str([str(gettime())]) + y + ": " + value + "\n")
                with open("returning_book.txt", "r") as op:
                    x = op.read()
                    print(x)
            elif _ret == 2:
                print("not return your book\n")
                print("Thanx for Choosing")

        if return_book == 3:
            print("That's your Book Timing Here when You are Taking this book.")
            with open("math.txt") as op:
                x = op.read()
                print(x)
            print("1 - Return This Book\n2 - Not")
            _ret = int(input("Type Here : "))
            if _ret == 1:
                value = "Return Math book"
                x = datetime.datetime.now()
                y = x.strftime("%A")
                with open("returning_book.txt", "a") as op:
                    op.write(str([str(gettime())]) + y + ": " + value + "\n")
                with open("returning_book.txt", "r") as op:
                    x = op.read()
                    print(x)
            elif _ret == 2:
                print("not return your book\n")
                print("Thanx for Choosing")

        if return_book == 4:
            print("That's your Book Timing Here when You are Taking this book")
            with open("history.txt") as op:
                x = op.read()
                print(x)
            print("1 - Return This Book\n2 - Not")
            _ret = int(input("Type Here : "))
            if _ret == 1:
                value = "Return History book"
                x = datetime.datetime.now()
                y = x.strftime("%A")
                with open("returning_book.txt", "a") as op:
                    op.write(str([str(gettime())]) + y + ": " + value + "\n")
                with open("returning_book.txt", "r") as op:
                    x = op.read()
                    print(x)
            elif _ret == 2:
                print("not return your book\n")
                print("Thanx for Choosing")

        if return_book == 5:
            print("That's your Book Timing Here when You are Taking this book")
            with open("english.txt") as op:
                x = op.read()
                print(x)
            print("1 - Return This Book\n2 - Not")
            _ret = int(input("Type Here : "))
            if _ret == 1:
                value = "Return English book"
                x = datetime.datetime.now()
                y = x.strftime("%A")
                with open("returning_book.txt", "a") as op:
                    op.write(str([str(gettime())]) + y + ": " + value + "\n")
                with open("returning_book.txt", "r") as op:
                    x = op.read()
                    print(x)
            elif _ret == 2:
                print("not return your book\n")
                print("Thanx for Choosing")

        if return_book == 6:
            print("That's your Book Timing Here when You are Taking this book")
            with open("bio.txt") as op:
                x = op.read()
                print(x)
            print("1 - Return This Book\n2 - Not")
            _ret = int(input("Type Here : "))
            if _ret == 1:
                value = "Return Bio book"
                x = datetime.datetime.now()
                y = x.strftime("%A")
                with open("returning_book.txt", "a") as op:
                    op.write(str([str(gettime())]) + y + ": " + value + "\n")
                with open("returning_book.txt", "r") as op:
                    x = op.read()
                    print(x)
            elif _ret == 2:
                print("not return your book\n")
                print("Thanx for Choosing")
            else:
                print("valid input.plz Enter again.")

    else:
        print("valid input.plz Enter again.")

    print("\t\t\tThanx for choosing this Library.....\n\n")