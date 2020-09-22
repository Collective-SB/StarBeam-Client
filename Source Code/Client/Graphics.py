import wx
import settings

class GUI(wx.Frame):
    # I hate making GUIs and I always will, unless it's WinForms. Seriously, can't someone copy WinForms?
    coordinateListOnline = None
    coordinateList = None

    def __init__(self):
        super().__init__(parent=None, title='StarBeam', size=(460, 410))
        panel = wx.Panel(self)

        # Set icon
        self.icon = wx.EmptyIcon()
        self.icon.CopyFromBitmap(wx.Bitmap("Starbeam.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(self.icon)

        sizer = wx.BoxSizer(wx.VERTICAL)

        # self.text_ctrl = wx.TextCtrl(panel)
        # sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        # my_btn = wx.Button(panel, label='Press Me')
        # sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)

        # Title
        font = wx.Font(20, family=wx.FONTFAMILY_MODERN, style=0, weight=100, underline=False, faceName="",
                       encoding=wx.FONTENCODING_DEFAULT)
        GUI.Title0 = wx.StaticText(panel, label="Latest Local Coordinates:")
        GUI.Title0.SetFont(font)
        GUI.Title0.SetForegroundColour("Red")
        sizer.Add(GUI.Title0)

        # COORDINATE_LIST
        font = wx.Font(20, family=wx.FONTFAMILY_MODERN, style=0, weight=100, underline=False, faceName="",
                       encoding=wx.FONTENCODING_DEFAULT)
        GUI.coordinateList = wx.StaticText(panel, label="X:\nY:\nZ:")
        GUI.coordinateList.SetFont(font)
        GUI.coordinateList.SetForegroundColour("Red")
        sizer.Add(GUI.coordinateList)

        # whitespace
        sizer.Add(0, 10, 0)

        # Title
        font = wx.Font(20, family=wx.FONTFAMILY_MODERN, style=0, weight=100, underline=False, faceName="",
                       encoding=wx.FONTENCODING_DEFAULT)
        GUI.Title1 = wx.StaticText(panel, label="Latest Online Coordinates:")
        GUI.Title1.SetFont(font)
        GUI.Title1.SetForegroundColour("Red")
        sizer.Add(GUI.Title1)

        # ONLINE_COORDINATE_LIST
        font = wx.Font(20, family=wx.FONTFAMILY_MODERN, style=0, weight=100, underline=False, faceName="",
                       encoding=wx.FONTENCODING_DEFAULT)
        GUI.coordinateListOnline = wx.StaticText(panel, label="X:\nY:\nZ:")
        GUI.coordinateListOnline.SetFont(font)
        GUI.coordinateListOnline.SetForegroundColour("Red")
        sizer.Add(GUI.coordinateListOnline)

        # Standard Frozenbyte Disclaimer: "Starbase" and its characters, names and other material © Frozenbyte Oy,
        # used with permission but without endorsement.
        GUI.disclaimer = wx.StaticText(panel,
                                       label='"Starbase" and its characters, names \n and other material © Frozenbyte '
                                             'Oy,\n used with permission but without endorsement.')
        sizer.Add(GUI.disclaimer)

        # Made by Collective marker
        GUI.disclaimer = wx.StaticText(panel, label=" Developed by IHaveNoLife, StrikeEagleChase, and BenCo for Collective")
        GUI.disclaimer.SetForegroundColour("Red")
        sizer.Add(GUI.disclaimer)

        # Version
        GUI.disclaimer = wx.StaticText(panel, label=" Closed Testing")
        GUI.disclaimer.SetForegroundColour("Red")
        sizer.Add(GUI.disclaimer)

        panel.SetSizer(sizer)
        self.Show()

    @staticmethod
    def set_coordinates(data):
        GUI.coordinateList.SetLabel(data)

    @staticmethod
    def set_online_coordinates(data):
        GUI.coordinateListOnline.SetLabel(data)

    def apply(self, event):
        """
        if self.shareTypeRadio0.GetValue() == True:
            #for now, 0 means private and 1 means public. Not sure about the actual ones
            main.WriteToConfig("shareLayer", "0")
            settings.variables.shareLayer = "0"

        else:
            main.WriteToConfig("shareLayer", "1")
            settings.variables.shareLayer = "1"

        settings.variables.displayName = self.displayName.GetValue()
        main.WriteToConfig("displayName", self.displayName.GetValue())
        """

        # this will do stuff in the future


def start_gui():
    app = wx.App()
    GUI()
    app.MainLoop()
