import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    user = simpledialog.askstring('title', 'Write a question for the 8 ball to answer')
    # Make a variable and initialize it to a random number between 0 and 3
    oliver = random.randint(0, 3)
    # If the random number is 0
    if oliver == 0:
        messagebox.showinfo('title', 'yes')

        # tell the user "Yes"

    # If the random number is 1
    if oliver == 1:
        messagebox.showinfo('title', 'no')

        # tell the user "No"

    # If the random number is 2
    if oliver == 2:
        messagebox.showinfo('title', 'Maybe you should ask Google?')

        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
    if oliver == 3:
        messagebox.showinfo('title', 'I cannot answer that')
        # write your own answer
