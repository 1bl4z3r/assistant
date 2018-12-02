import wx
import wikipedia
import wolframalpha

app_id = "YOUR APP ID"
client = wolframalpha.Client(app_id)
language = "en"
wikipedia.set_lang(language)

class Assistant(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, pos=wx.DefaultPosition, size=wx.Size(450, 100), style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN, title="Assistant")
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel, label="How can I help you?")
        sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(sizer)
        self.Show()

    def OnEnter(self, event):
        query = self.txt.GetValue()
        query = query.lower()
	try:
        	res = wolframalpha.Client(app_id).query(query)
        	answer = next(res.results).text
        	print(answer)
    	except:
		try:
       			query = query.split(' ')
       			query = ' '.join(query[2:])
        		print(wikipedia.summary(query))
		except:
			print("Cannot find {}".format(query))


if __name__ == "__main__":
    app = wx.App(True)
    frame = Assistant()
    app.MainLoop()

