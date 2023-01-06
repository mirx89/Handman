from tkinter import *
import tkinter.font as tkfont
from PIL import Image, ImageTk

class View(Tk):

    def __init__(self, controller, model):
        super().__init__()  # kõik info tkinterist
        self.controller = controller
        self.model = model
        self.userinput = StringVar()

        self.big_font_style = tkfont.Font(family="Courier", size=18, weight="bold")
        self.default_style_bold = tkfont.Font(family="Verdana", size=10, weight="bold")
        self.default_style = tkfont.Font(family="Verdana", size=10)

        # window properties
        self.geometry("515x200")
        self.title("Hangman")
        self.center(self)

        # Create two frames
        self.frame_top, self.frame_bottom, self.frame_image = self.create_two_frames()

        self.image = ImageTk.PhotoImage(Image.open(self.model.images_files[len(self.model.images_files) - 1]))
        self.lable_image = None

        # Create all Buttons, Labels and Entry
        self.btn_new, self.btn_cancle, self.btn_send = self.create_all_buttons()
        self.lbl_error, self.lbl_time, self.lbl_result = self.create_all_labels()
        self.char_input = self.create_input_entry()


    def main(self):
        self.mainloop()

    @staticmethod
    def center(win):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        Netist võetud plokk: https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter
        """
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    def create_two_frames(self):
        frame_top = Frame(self, bg="#0096FF", height=50)
        frame_bottom = Frame(self, bg="#EBEB00")

        frame_top.pack(fill="both")
        frame_bottom.pack(expand=True,fill="both")

        #hangman image frame
        frame_img = Frame(frame_top, bg="white", width=130, height=130)
        frame_img.grid(row=0, column=3, rowspan=4, padx=5, pady=5)

        return frame_top, frame_bottom, frame_img # method return two objects

    def create_all_buttons(self):
        # New Game
        btn_new = Button(self.frame_top, text="New Game", font=self.default_style)
        #Leaderboard and place once
        Button(self.frame_top, text="Leaderboard", font=self.default_style).grid(row=0, column=1, pady=5, padx=2,
                                                                                 sticky=EW)
        #Cancle and Send
        btn_cancel = Button(self.frame_top, text="Cancle", font=self.default_style, state="disabled")
        btn_send = Button(self.frame_top, text="Send", font=self.default_style, state="disabled")

        #Place three buttons and frames
        btn_new.grid(row=0, column=0, padx=5, pady=2, sticky=EW)
        btn_cancel.grid(row=0, column=2, padx=5, pady=2, sticky=EW)
        btn_send.grid(row=1, column=2, padx=5, pady=2, sticky=EW)

        return btn_new, btn_cancel, btn_send

    def create_all_labels(self):
        Label(self.frame_top, text="Input letter", font=self.default_style_bold).grid(row=1,column=0, padx=5, pady=2)
        lbl_error = Label(self.frame_top, text="Wrong 0 letter(s)", anchor="w", font=self.default_style_bold)
        lbl_time = Label(self.frame_top, text="0:00:00", font=self.default_style)
        lbl_result = Label(self.frame_bottom, text="Let\'s play". upper(), font=self.big_font_style)
        # Image label
        self.lable_image = Label(self.frame_image, image=self.image)
        # Eraldi rida kuna neid ridu saab muuta(näide 6 rida üleval pole vaja) ning vastasel juhul ei saa teha return
        self.lable_image.pack()
        lbl_error.grid(row=2, column=0, columnspan=3, sticky=EW, padx=5, pady=2)
        lbl_time.grid(row=3, column=0, columnspan=3, sticky=EW, padx=5, pady=2)
        lbl_result.pack(pady=2, padx=2)

        return lbl_result, lbl_time, lbl_error

    def create_input_entry(self):
        char_input = Entry(self.frame_top, textvariable=self.userinput, justify="center", font=self.default_style)
        char_input["state"] = "disabled"
        char_input.grid(row=1, column=1, padx=5, pady=2)

        return char_input
