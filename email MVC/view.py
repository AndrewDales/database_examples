import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from controller import Controller


class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # Select Email label
        self.select_email_label = ttk.Label(self, text='Select Email:')
        self.select_email_label.grid(row=0, column=1)

        # Select label
        self.select_label = ttk.Label(self, text='Select:')
        self.select_label.grid(row=1, column=0)

        # Combobox to show all emails
        self.emails_cmb = ttk.Combobox(self, state='readonly')
        self.set_emails(parent.controller)
        self.emails_cmb.grid(row=1, column=1, sticky=tk.NSEW, pady=10)

        # Send Email button
        self.send_email_button = ttk.Button(self, text='Send Email', command=self.send_email)
        self.send_email_button.grid(row=1, column=2, padx=10)

        # label
        self.new_email_label = ttk.Label(self, text='New Email:')
        self.new_email_label.grid(row=3, column=0)

        # email entry
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=3, column=1, sticky=tk.NSEW)

        # save button
        self.save_button = ttk.Button(self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=3, column=2, padx=10)

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=4, column=1, sticky=tk.W)

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def set_emails(self, controller):
        """
        Set the emails
        :param controller:
        :return:
        """
        emails = controller.get_emails()
        self.emails_cmb['values'] = emails

    def send_email(self):
        """
        Send an email - only a popup message for now
        :return:
        """
        email_address = self.emails_cmb.get()
        if email_address:
            msg = f'Sending email to {email_address}'
            tk.messagebox.showinfo('Send Email', msg)

    def save_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            try:
                success_message = self.controller.save(self.email_var.get())
                self.show_success(success_message)
                self.set_emails(self.controller)
            except ValueError as error:
                self.show_error(error)

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)


    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''

        # reset the form
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')

        # create a controller
        self.controller = Controller()

        # create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # set the controller to view
        view.set_controller(self.controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()