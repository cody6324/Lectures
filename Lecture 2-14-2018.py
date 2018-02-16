"Chapter 8: Graphical User Interface   GUI"

from breezypythongui import EasyFrame


class LabelDemo(EasyFrame):
    """
    Displays a greeting in a window
    """

    def __init__(self):
        """
        Set up the window and the label
        """
        EasyFrame.__init__(self)
        self.addLabel(text="Hello World!", row=0, column=0)

def main() -> None:
    """
    Starts and pops up the window
    :return: None
    """
    LabelDemo().mainloop()