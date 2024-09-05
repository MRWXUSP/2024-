# -*- coding: utf-8 -*-
'''
在此文件运行并调试程序,仅可在windows下运行
'''

import wx

from workfile.GUI_Back import GUI_Back


app = wx.App(False)
frame = GUI_Back(None)
frame.Show(True)
app.MainLoop()