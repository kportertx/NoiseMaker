#!/usr/bin/python
import wx
import audiere

class BabyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, size=wx.DisplaySize())

        self.device = audiere.open_device()
        self._soundgen = self.device.create_tone
        self.tone = self.device.create_tone(250)
        self._pan = 0
        self.tone.pan = self._pan
        self._gen_toggle = False
        panel = wx.Panel(self,-1)
        panel.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        panel.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
        panel.SetFocus()
        self.Centre()
        self.Show(True)

    def OnKeyDown(self, event):
        keycode = event.GetKeyCode()
        print keycode
        if keycode == 311:
            self._gen_toggle = not self._gen_toggle
            if self._gen_toggle:
                self._soundgen = self.device.create_square
            else:
                self._soundgen = self.device.create_tone
        
        self.tone = self._soundgen(keycode*20)
        self.tone.play()

    def OnKeyUp(self, event):
        """ Stop the tone """
        self.tone.stop()


class BabyApp(wx.App):
    def OnInit(self):
        frame = BabyFrame(None, -1, 'Baby Music')
        frame.Show(True)
        return True

def main():
    app = BabyApp(0)
    app.MainLoop()

if __name__ == "__main__":
    main()
