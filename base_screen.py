class BaseScreen:
    def __init__(self, root, db):
        self.root = root
        self.db = db

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
