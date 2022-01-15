import DAL
from Window import Window
from MainFrame import MainFrame

def populate_hotkeys_map(hotkeys):
    hotkeysMap = {}

    for hotkey_i in hotkeys:
        hotkey = hotkey_i["hotkey"]
        text_to_copy = hotkey_i["text"]

        hotkeysMap[hotkey] = text_to_copy

    return hotkeysMap

if __name__ == "__main__":
    data = DAL.retrieve_db()
    
    hotkeysMap = populate_hotkeys_map(data["hotkeys"])

    window = Window(hotkeysMap)
    MainFrame(window, data, hotkeysMap)

    window.mainloop()


    ##TODO check empty db