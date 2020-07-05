from tkinter import *
from tkinter import messagebox  # This is for the messageboxs that are used for the Info button and the error messages


class Application(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # This function clears the display and ensures the program is ready for the next input

    def replaceText(self, text):
        self.display.delete(0, END)  # Selects all text in the entry box
        self.display.insert(0, text)  # Replaces it with text

    # This function adds the users input to the entry box
    def appendToDisplay(self, text):
        entryText = text
        cursor = self.display.index(INSERT)
        self.display.insert(cursor, entryText)

    # This is the calculation function to find the result of the users input
    def calculateExpression(self):
        self.expression = str(self.display.get())
        self.expression = self.expression.replace("%",
                                                  "/ 100")  # replaces the percent symbol to divide the expression by 100
        try:
            self.result = eval(self.expression)
            self.AcceptedValues.append(str(self.result))  # Appends the list to accept the result
            self.replaceText(self.result)
        except (SyntaxError, ZeroDivisionError):  # This ensures that the program doesnt crash and returns an error
            messagebox.showinfo("ERROR", "Invalid input", icon="warning")
            self.replaceText("")  # Makes the user restart as the input was invalid

    # This function creates a message box that is called when the user press the INFO button. This has basic information of the program and the creator and dates
    def InfoPopup(self):
        messagebox.showinfo("Information",
                            "Python Version 3.3.0\nAuthor: Caleb Madgwick\nLast Date Edited: 02/10/2018\n\nConditions of Use:\n- If wanting to calculate percentage, end the expression with the percentage symbol\n- Must always put a leading number before the decimal point\n - Must not divide a number by 0\n -Enusre you do not include too many decimal points in one number\n- Do not press equals when nothing is inside the entrybox\n - Always ensure you use operators correctly\n- Press Enter or '=' on the keyboard to get the result of the expression\n- Press 'i' on your keyboard to bring this popup back again ")

    # This function is called when the user presses the AC button,
    def clearText(self):
        self.display.delete(0, END)  # Deletes everything in the entry box
        self.display.insert(0, "")  # Replaces the enry box with a 0, ready for new user input

    # This function is called when the DEL button is pressed
    def delete(self):
        current = str(self.display.get())
        cursor = self.display.index(INSERT)
        if cursor == 0:
            pass
        else:
            cursor -= 1
            self.display.delete(cursor)

    # This is the main list to tell the program what is allowed in the enrty box and this is also used to create the buttons
    AcceptedValues = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "/", "*", "-", "+", "0", ".", "%"]

    # This is the validation function to ensure that only the accepted values are allowed in the entry box
    def validate(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type,
                 widget_name, ):
        if (action == "1"):

            operators = "/*+-.%"
            current_string = str(self.display.get())

            if text == ".":
                if current_string == "":  # ensures that a decimal point can not be entered first
                    return False
                if current_string[-1] == ".":  # Can not enter a decimal point after there is already one there
                    return False

            if text in operators:
                if current_string == "":
                    if text == "-" or text == "+":  # Only allows + and - symbols to be entered in in a row
                        return True
                    else:
                        return False

                if current_string[-1] in operators:
                    if text == "+" or text == "-":  # Only allows + and - symbols to be entered in in a row when the cursor is behind the value
                        return True
                    else:
                        return False

            if text in self.AcceptedValues:
                try:
                    return True  # If the input is in the AcceptedValues list the input is allowed in the entrybox
                except ValueError:
                    return False  # If the input is NOT in the AcceptedValues list the input is NOT allowed in the entrybox
            else:
                return False

        else:
            return True


class Calculator(Application):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        root.bind("<Return>", lambda event: self.calculateExpression())
        root.bind("=", lambda event: self.calculateExpression())
        root.bind("i", lambda event: self.InfoPopup())
        self.createWidgets()  # This calls the main function that creastes the layout of the calculator

    def createWidgets(self):
        vcmd = (self.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V',
                '%W')  # Calls all of the validation pricipals
        self.display = Entry(self, bd=15, insertwidth=4, width=22,
                             font=("Verdana", 20, "bold"), justify=RIGHT, validate='key',
                             validatecommand=vcmd)  # Creates the size of the entry box, font and calls the validation
        self.display.insert(0, "")  # Clears the display to 0
        self.display.grid(row=0, column=0, columnspan=5)  # Size of the displayy
        self.display.focus()  # Selects the entrybox with a flashing cursor when it is opened

        # Creates the number buttons: "1", "2", "3", "4", "5", "6", "7", "8" and "9"
        for button_variable in range(3):
            if button_variable <= 3:  # Creates the buttons "1", "2" and "3"
                self.number = Button(self, bg="#D1D1D1", activebackground="#D9D9D9", text=(1 + button_variable),
                                     width=6, pady=25, font=("Helvetica", 20, "bold"),
                                     command=lambda button_variable=button_variable: self.appendToDisplay(
                                         self.AcceptedValues[
                                             button_variable]))  # Creates the background colour(Light Grey), active background colour(Lighter Grey), font size, button size and inputs the value to the entrybox
                self.number.grid(row=5, column=(0 + button_variable))  # This adds the buttons to the grid in row 5
            if button_variable <= 3:  # Creates the buttons"4", "5" and "6"
                self.number = Button(self, bg="#D1D1D1", activebackground="#D9D9D9", text=(4 + button_variable),
                                     width=6, pady=25, font=("Helvetica", 20, "bold"),
                                     command=lambda button_variable=button_variable: self.appendToDisplay(
                                         self.AcceptedValues[
                                             3 + button_variable]))  # Creates the background colour(Light Grey), active background colour(Lighter Grey), font size, button size and inputs the value to the entrybox
                self.number.grid(row=4, column=(0 + button_variable))  # This adds the buttons to the grid in row 4
            if button_variable <= 3:  # Creates the buttons "7", "8" and "9"
                self.number = Button(self, bg="#D1D1D1", activebackground="#D9D9D9", text=(7 + button_variable),
                                     width=6, pady=25, font=("Helvetica", 20, "bold"),
                                     command=lambda button_variable=button_variable: self.appendToDisplay(
                                         self.AcceptedValues[
                                             6 + button_variable]))  # Creates the background colour(Light Grey), active background colour(Lighter Grey), font size, button size and inputs the value to the entrybox
                self.number.grid(row=3, column=(0 + button_variable))  # This adds the buttons to the grid in row 3

        # Creates the operator buttons: "/", "*", "-" and "+"
        for button_variable in range(4):
            if button_variable <= 4:
                self.number = Button(self, bg="#FF9745", activebackground="#FFA056",
                                     text=(self.AcceptedValues[9 + button_variable]), width=6, pady=25,
                                     font=("Helvetica", 20, "bold"),
                                     command=lambda button_variable=button_variable: self.appendToDisplay(
                                         self.AcceptedValues[
                                             9 + button_variable]))  # Creates the background colour(Orange), active background colour(Light Orange), font size, button size and inputs the value to the entrybox
                self.number.grid(row=(2 + button_variable), column=3)  # This adds the buttons to the grid in column 3

        # Creates the buttons: "0" and "."
        for button_variable in range(2):
            if button_variable <= 2:
                self.number = Button(self, bg="#D1D1D1", activebackground="#D9D9D9",
                                     text=(self.AcceptedValues[13 + button_variable]), width=6, pady=25,
                                     font=("Helvetica", 20, "bold"),
                                     command=lambda button_variable=button_variable: self.appendToDisplay(
                                         self.AcceptedValues[
                                             13 + button_variable]))  # Creates the background colour(Light Grey), active background colour(Lighter Grey), font size, button size and inputs the value to the entrybox
                self.number.grid(row=6, column=(0 + (2 * button_variable)), sticky="EW")
            if button_variable == 0:
                self.number.grid(columnspan=2)
                # The following buttons are not in a loop because they all have a command function associated with them and the loop would be just as long
        # Equal button
        self.Equalbutton = Button(self, bg="#FF9745", activebackground="#FFA056", text="=", width=6, pady=25,
                                  font=("Helvetica", 20, "bold"),
                                  command=self.calculateExpression)  # This calls the Calculate function which was defined earlier that displays the result of the inputed expression
        # Creates the background colour(Orange), active background colour(Light Orange), font size, button size and inputs the value to the entrybox
        self.Equalbutton.grid(row=6, column=3, sticky=W)  # The button is in row 6, coulmn 3

        # Clear button
        self.clear = Button(self, bg="#8F8F8F", activebackground="#999999", text="AC", width=6, pady=25,
                            font=("Helvetica", 20, "bold"),
                            command=self.clearText)  # This calls the Clear function which deletes all the values in the entry box an replaces it with a "0"
        # Creates the background colour(Grey), active background colour(Light Grey), font size, button size and inputs the value to the entrybox
        self.clear.grid(row=2, column=0)  # The button is in row 6 collumm 3

        # Information button
        info = Button(self, bg="#636262", activebackground="#575757", text="INFO", width=6, height=1, pady=0,
                      font=("Helvetica", 20, "bold"),
                      command=self.InfoPopup)  # This button calls the information function where a messagebox is displayed to the user
        # Creates the background colour(Dark Grey), active background colour(light Dark Grey), font size, button size and inputs the value to the entrybox
        info.grid(row=1, column=0, columnspan=4, sticky="WE")  # The button is in row 1 collumm 0

        # Percent button
        percent = Button(self, bg="#8F8F8F", activebackground="#999999", text="%", width=6, pady=25,
                         font=("Helvetica", 20, "bold"), command=lambda: self.appendToDisplay(
                "%"))  # This adds a percentage symbol to the entrybox, and when the user presses the "=" button the expression is divided by 100 and is called for in the calculate function
        # Creates the background colour(Grey), active background colour(Light Grey), font size, button size and inputs the value to the entrybox
        percent.grid(row=2, column=2)

        # Backspace button
        delete = Button(self, bg="#8F8F8F", activebackground="#999999", text="DEL", width=6, pady=25,
                        font=("Helvetica", 20, "bold"), command=self.delete)
        # Creates the background colour(Grey), active background colour(Light Grey), font size, button size and inputs the value to the entrybox
        delete.grid(row=2, column=1)


root = Tk()
root.title("CALCULATOR")  # The title of the program
root.resizable(0, 1)  # Ensures the screen size is not resizable
calc = Calculator(root).pack()
app = Application(root)
root.mainloop()  # Closes the main loop and ends the code
