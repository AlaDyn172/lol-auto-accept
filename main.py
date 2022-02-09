import pyautogui
import locate

class Main:
    def __init__(self):
        # Gamemodes: blind, draft, solo, flex
        # ARAM | TFT | other gamemodes not supported.
        self.gamemode = "flex"
        # Roles: top, jg, mid, bot, supp, fill
        self.main_role = "jg"
        self.secondary_role = "top"
    def main(self):
        self.check_fmatch_or_play_btn()
    def check_fmatch_or_play_btn(self):
        play_btn = locate.get("play")
        if(play_btn is None):
            find_match = locate.get("find_match")
            if(find_match is not None):
                if(self.gamemode == "solo" or self.gamemode == "flex"):
                    self.pick_roles()
                    self.click_find_match()
                    self.click_accept()
                else:
                    self.click_find_match()
                    self.click_accept()
        else:
            self.click_play()
            self.click_gamemode()
            self.click_confirm()
            if(self.gamemode == "solo" or self.gamemode == "flex"):
                self.pick_roles()
                self.click_find_match()
                self.click_accept()
            else:
                self.click_find_match()
                self.click_accept()
    def click_play(self):
        btn = locate.get("play")
        pyautogui.click(btn)
    def click_find_match(self):
        btn = locate.get("find_match")
        pyautogui.click(btn)
    def click_gamemode(self):
        btn = locate.get("gamemodes/"+self.gamemode)
        pyautogui.click(btn)
    def click_confirm(self):
        btn = locate.get("confirm")
        pyautogui.click(btn)
    def click_accept(self):
        btn = locate.get("accept")
        pyautogui.click(btn)
    def pick_roles(self):
        pick_role = locate.get("pick_1st_role")
        pyautogui.click(pick_role)
        main_role = locate.get("roles/" + self.main_role)
        pyautogui.click(main_role)
        pick_role = locate.get("pick_role")
        pyautogui.click(pick_role)
        secondary_role = locate.get("roles/" + self.secondary_role)
        pyautogui.click(secondary_role)

Object = Main()

if __name__ == '__main__':
    Object.main()
