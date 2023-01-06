from tkinter import simpledialog

from GameTime import GameTime
from Model import Model
from View import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self, self.model)
        self.gametime = GameTime(self.view.lbl_time)  # Crate gametime object

    def main(self):
        self.view.main()

    def click_btn_new(self):
        self.view.btn_new["state"] = "disable"
        self.view.btn_cancle["state"] = "normal"
        self.view.btn_send["state"] = "normal"
        self.view.char_input["state"] = "normal"
        self.view.change_image(0)  # Image change with index
        self.model.start_new_game()  # starting new game
        self.view.lbl_result.configure(text=self.model.user_word)
        self.view.lbl_error.configure(text="Wrong 0 letter(s)", fg="black")
        self.view.char_input.focus()  # Active input field
        self.gametime.reset()
        self.gametime.start()

    def click_btn_cancel(self):
        self.gametime.stop()
        self.view.btn_new["state"] = "normal"
        self.view.btn_cancle["state"] = "disable"
        self.view.btn_send["state"] = "disable"
        self.view.char_input["state"] = "disable"
        self.view.char_input.delete(0, "end")
        self.view.change_image(len(self.model.images_files) - 1)

    def click_btn_send(self):
        self.model.get_user_input(self.view.userinput.get().strip())  # strip võtab vaid tähed
        self.view.lbl_result.configure(text=self.model.user_word)
        self.view.lbl_error.configure(text=f"Wrong {self.model.counter} letter(s). {self.model.get_all_user_chars()}")
        self.view.char_input.delete(0, "end")
        if self.model.counter > 0:
            self.view.lbl_error.configure(fg="red")  # Font color
            self.view.change_image(self.model.counter)  # error image change
        self.is_game_over()

    def is_game_over(self):
        if self.model.counter >= 11 or "_" not in self.model.user_word \
                or self.model.counter >= (len(self.model.images_files) - 1):
            self.gametime.stop()
            self.view.btn_new["state"] = "normal"
            self.view.btn_cancle["state"] = "disable"
            self.view.btn_send["state"] = "disable"
            self.view.char_input["state"] = "disable"
            player_name = simpledialog.askstring("Game over", "Add player name", parent=self.view)
            self.model.set_player_name(player_name, self.gametime.counter)
            self.view.change_image(len(self.model.images_files) - 1)

    def click_btn_leaderboard(self):
        popup_window = self.view.create_popup_window()
        data = self.model.read_leaderboard_file_contents()
        self.view.generate_leaderboard(popup_window, data)
