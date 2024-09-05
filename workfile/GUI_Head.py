# -*- coding: utf-8 -*-

#--------------------------------------------------------------------------
# Python code generated with wxFormBuilder (version 3.9.0 Jun 14 2020)
# http://www.wxformbuilder.org/
#
# PLEASE DO *NOT* EDIT THIS FILE!
#--------------------------------------------------------------------------

import wx
import wx.xrc

import gettext
_ = gettext.gettext

#--------------------------------------------------------------------------
#  Class MyFrame1
#---------------------------------------------------------------------------

class MyFrame1 ( wx.Frame ):

	def __init__(self, parent):
		wx.Frame.__init__ (self, parent, id = wx.ID_ANY, title = _(u"控制台（仅运行在windows!!!）"), pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
		self.SetBackgroundColour(wx.Colour( 239, 235, 235 ))

		gbSizer6 = wx.GridBagSizer(0, 0)
		gbSizer6.SetFlexibleDirection(wx.BOTH)
		gbSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _(u"串口设置")), wx.VERTICAL)

		self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, _(u"串口"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText3.Wrap(-1)

		sbSizer3.Add(self.m_staticText3, 0, wx.ALL, 5)

		m_choice1Choices = [ _(u"COM1"), _(u"COM2"), _(u"COM3"), _(u"COM4"), _(u"COM5"), _(u"COM6"), _(u"COM7"), _(u"COM8"), _(u"COM9"), _(u"COM10"), _(u"COM11"), _(u"COM12"), _(u"COM13"), _(u"COM14"), _(u"COM15"), _(u"COM16"), _(u"COM17"), _(u"COM18"), _(u"COM19"), _(u"COM20"), _(u"COM21"), _(u"COM22"), _(u"COM23"), _(u"COM24"), _(u"COM25"), wx.EmptyString ]
		self.m_choice1 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), m_choice1Choices, 0)
		self.m_choice1.SetSelection(0)
		sbSizer3.Add(self.m_choice1, 0, wx.ALL, 5)

		self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, _(u"波特率"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText4.Wrap(-1)

		sbSizer3.Add(self.m_staticText4, 0, wx.ALL, 5)

		m_choice2Choices = [ _(u"600"), _(u"1200"), _(u"1800"), _(u"2400"), _(u"4800"), _(u"9600") ]
		self.m_choice2 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), m_choice2Choices, 0)
		self.m_choice2.SetSelection(5)
		sbSizer3.Add(self.m_choice2, 0, wx.ALL, 5)

		self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, _(u"数据位"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText5.Wrap(-1)

		sbSizer3.Add(self.m_staticText5, 0, wx.ALL, 5)

		m_choice3Choices = [ _(u"5"), _(u"6"), _(u"7"), _(u"8") ]
		self.m_choice3 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), m_choice3Choices, 0)
		self.m_choice3.SetSelection(3)
		sbSizer3.Add(self.m_choice3, 0, wx.ALL, 5)

		self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, _(u"校验位"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText6.Wrap(-1)

		sbSizer3.Add(self.m_staticText6, 0, wx.ALL, 5)

		m_choice4Choices = [ _(u"无"), _(u"奇"), _(u"偶") ]
		self.m_choice4 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), m_choice4Choices, 0)
		self.m_choice4.SetSelection(0)
		sbSizer3.Add(self.m_choice4, 0, wx.ALL, 5)

		self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, _(u"停止位"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText7.Wrap(-1)

		sbSizer3.Add(self.m_staticText7, 0, wx.ALL, 5)

		m_choice5Choices = [ _(u"1"), _(u"1.5"), _(u"2") ]
		self.m_choice5 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), m_choice5Choices, 0)
		self.m_choice5.SetSelection(0)
		sbSizer3.Add(self.m_choice5, 0, wx.ALL, 5)


		gbSizer6.Add(sbSizer3, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.EXPAND|wx.ALL, 5)

		gbSizer8 = wx.GridBagSizer(0, 0)
		gbSizer8.SetFlexibleDirection(wx.BOTH)
		gbSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_ALL)

		sbSizer6 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _(u"串口操作")), wx.HORIZONTAL)

		self.m_button2 = wx.Button(self, wx.ID_ANY, _(u"打开串口"), wx.DefaultPosition, wx.Size( -1,-1 ), 0)
		sbSizer6.Add(self.m_button2, 1, wx.ALL, 5)

		self.m_button3 = wx.Button(self, wx.ID_ANY, _(u"关闭串口"), wx.DefaultPosition, wx.Size( -1,-1 ), 0)
		self.m_button3.Enable(False)

		sbSizer6.Add(self.m_button3, 1, wx.ALL, 5)

		self.m_button4 = wx.Button(self, wx.ID_ANY, _(u"添加串口"), wx.DefaultPosition, wx.Size( -1,-1 ), 0)
		sbSizer6.Add(self.m_button4, 1, wx.ALL, 5)

		self.m_button5 = wx.Button(self, wx.ID_ANY, _(u"删除串口"), wx.DefaultPosition, wx.Size( -1,-1 ), 0)
		sbSizer6.Add(self.m_button5, 1, wx.ALL, 5)

		self.m_button6 = wx.Button(self, wx.ID_ANY, _(u"退出程序"), wx.DefaultPosition, wx.Size( -1,-1 ), 0)
		sbSizer6.Add(self.m_button6, 1, wx.ALL, 5)


		gbSizer8.Add(sbSizer6, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.EXPAND|wx.ALL, 5)

		sbSizer41 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _(u"数据显示与选取")), wx.VERTICAL)

		gbSizer10 = wx.GridBagSizer(0, 0)
		gbSizer10.SetFlexibleDirection(wx.BOTH)
		gbSizer10.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		sbSizer43 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _(u"待办列表")), wx.VERTICAL)

		m_checkList2Choices = [_(u"暂无任何待办项")]
		self.m_checkList2 = wx.CheckListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList2Choices, wx.LB_HSCROLL|wx.LB_NEEDED_SB|wx.LB_SINGLE)
		self.m_checkList2.Enable(False)

		sbSizer43.Add(self.m_checkList2, 0, wx.ALL|wx.EXPAND, 5)

		self.m_staticText29 = wx.StaticText(self, wx.ID_ANY, _(u"刷新列表请在“基本操作”中处理"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText29.Wrap(-1)

		sbSizer43.Add(self.m_staticText29, 0, wx.ALL, 5)


		gbSizer10.Add(sbSizer43, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.EXPAND|wx.ALL, 5)

		sbSizer44 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _(u"时间")), wx.VERTICAL)

		bSizer18 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_staticText30 = wx.StaticText(self, wx.ID_ANY, _(u"NaN"), wx.DefaultPosition, wx.DefaultSize, wx.ST_NO_AUTORESIZE|wx.BORDER_SUNKEN)
		self.m_staticText30.Wrap(-1)

		bSizer18.Add(self.m_staticText30, 2, wx.ALL, 5)

		self.m_staticText31 = wx.StaticText(self, wx.ID_ANY, _(u"年"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText31.Wrap(-1)

		bSizer18.Add(self.m_staticText31, 1, wx.ALL, 5)

		self.m_staticText32 = wx.StaticText(self, wx.ID_ANY, _(u"NaN"), wx.DefaultPosition, wx.DefaultSize, wx.ST_NO_AUTORESIZE|wx.BORDER_SUNKEN)
		self.m_staticText32.Wrap(-1)

		bSizer18.Add(self.m_staticText32, 2, wx.ALL, 5)

		self.m_staticText33 = wx.StaticText(self, wx.ID_ANY, _(u"月"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText33.Wrap(-1)

		bSizer18.Add(self.m_staticText33, 1, wx.ALL, 5)

		self.m_staticText34 = wx.StaticText(self, wx.ID_ANY, _(u"NaN"), wx.DefaultPosition, wx.DefaultSize, wx.ST_NO_AUTORESIZE|wx.BORDER_SUNKEN)
		self.m_staticText34.Wrap(-1)

		bSizer18.Add(self.m_staticText34, 2, wx.ALL, 5)

		self.m_staticText35 = wx.StaticText(self, wx.ID_ANY, _(u"日"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText35.Wrap(-1)

		bSizer18.Add(self.m_staticText35, 1, wx.ALL, 5)


		sbSizer44.Add(bSizer18, 1, wx.EXPAND|wx.ALL, 5)

		bSizer19 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_staticText36 = wx.StaticText(self, wx.ID_ANY, _(u"NaN"), wx.DefaultPosition, wx.DefaultSize, wx.ST_NO_AUTORESIZE|wx.BORDER_SUNKEN)
		self.m_staticText36.Wrap(-1)

		bSizer19.Add(self.m_staticText36, 2, wx.ALL, 5)

		self.m_staticText37 = wx.StaticText(self, wx.ID_ANY, _(u"时"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText37.Wrap(-1)

		bSizer19.Add(self.m_staticText37, 1, wx.ALL, 5)

		self.m_staticText38 = wx.StaticText(self, wx.ID_ANY, _(u"NaN"), wx.DefaultPosition, wx.DefaultSize, wx.ST_NO_AUTORESIZE|wx.BORDER_SUNKEN)
		self.m_staticText38.Wrap(-1)

		bSizer19.Add(self.m_staticText38, 2, wx.ALL, 5)

		self.m_staticText39 = wx.StaticText(self, wx.ID_ANY, _(u"分"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText39.Wrap(-1)

		bSizer19.Add(self.m_staticText39, 1, wx.ALL, 5)

		self.m_staticText40 = wx.StaticText(self, wx.ID_ANY, _(u"NaN"), wx.DefaultPosition, wx.DefaultSize, wx.ST_NO_AUTORESIZE|wx.BORDER_SUNKEN)
		self.m_staticText40.Wrap(-1)

		bSizer19.Add(self.m_staticText40, 2, wx.ALL, 5)

		self.m_staticText41 = wx.StaticText(self, wx.ID_ANY, _(u"秒"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText41.Wrap(-1)

		bSizer19.Add(self.m_staticText41, 1, wx.ALL, 5)


		sbSizer44.Add(bSizer19, 1, wx.EXPAND|wx.ALL, 5)


		gbSizer10.Add(sbSizer44, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.EXPAND|wx.ALL, 5)


		gbSizer10.AddGrowableCol(0)
		gbSizer10.AddGrowableCol(1)
		gbSizer10.AddGrowableRow(0)

		sbSizer41.Add(gbSizer10, 1, wx.EXPAND|wx.ALL, 5)


		gbSizer8.Add(sbSizer41, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.EXPAND|wx.ALL, 5)

		sbSizer8 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _(u"基本操作")), wx.VERTICAL)

		bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_STATIC)
		self.m_textCtrl2.SetMaxLength(2)
		bSizer3.Add(self.m_textCtrl2, 3, wx.ALL, 5)

		self.m_staticText20 = wx.StaticText(self, wx.ID_ANY, _(u"年"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText20.Wrap(-1)

		bSizer3.Add(self.m_staticText20, 0, wx.ALL, 5)

		self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_STATIC)
		self.m_textCtrl3.SetMaxLength(2)
		bSizer3.Add(self.m_textCtrl3, 3, wx.ALL, 5)

		self.m_staticText21 = wx.StaticText(self, wx.ID_ANY, _(u"月"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText21.Wrap(-1)

		bSizer3.Add(self.m_staticText21, 0, wx.ALL, 5)

		self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_STATIC)
		self.m_textCtrl4.SetMaxLength(2)
		bSizer3.Add(self.m_textCtrl4, 3, wx.ALL, 5)

		self.m_staticText22 = wx.StaticText(self, wx.ID_ANY, _(u"日"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText22.Wrap(-1)

		bSizer3.Add(self.m_staticText22, 0, wx.ALL, 5)

		self.m_textCtrl8 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_STATIC)
		self.m_textCtrl8.SetMaxLength(2)
		bSizer3.Add(self.m_textCtrl8, 3, wx.ALL, 5)

		self.m_staticText26 = wx.StaticText(self, wx.ID_ANY, _(u"时"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText26.Wrap(-1)

		bSizer3.Add(self.m_staticText26, 0, wx.ALL, 5)

		self.m_textCtrl9 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_STATIC)
		self.m_textCtrl9.SetMaxLength(2)
		bSizer3.Add(self.m_textCtrl9, 3, wx.ALL, 5)

		self.m_staticText27 = wx.StaticText(self, wx.ID_ANY, _(u"分"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText27.Wrap(-1)

		bSizer3.Add(self.m_staticText27, 0, wx.ALL, 5)

		self.m_textCtrl10 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_STATIC)
		self.m_textCtrl10.SetMaxLength(2)
		bSizer3.Add(self.m_textCtrl10, 3, wx.ALL, 5)

		self.m_staticText28 = wx.StaticText(self, wx.ID_ANY, _(u"秒"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText28.Wrap(-1)

		bSizer3.Add(self.m_staticText28, 0, wx.ALL, 5)


		sbSizer8.Add(bSizer3, 1, wx.EXPAND, 5)

		bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_button27 = wx.Button(self, wx.ID_ANY, _(u"读取/刷新数据"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_button27.Enable(False)

		bSizer5.Add(self.m_button27, 1, wx.ALL, 5)

		self.m_button9 = wx.Button(self, wx.ID_ANY, _(u"修改学习板时间"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_button9.Enable(False)

		bSizer5.Add(self.m_button9, 1, wx.ALL, 5)

		self.m_button10 = wx.Button(self, wx.ID_ANY, _(u"重置学习板时间"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_button10.Enable(False)

		bSizer5.Add(self.m_button10, 1, wx.ALL, 5)


		sbSizer8.Add(bSizer5, 1, wx.EXPAND, 5)


		gbSizer8.Add(sbSizer8, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.EXPAND|wx.ALL, 5)

		sbSizer9 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _(u"数据操作（先在上方选择要修改的待办）")), wx.VERTICAL)

		bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_staticText321 = wx.StaticText(self, wx.ID_ANY, _(u"NaN"), wx.DefaultPosition, wx.DefaultSize, wx.ST_NO_AUTORESIZE|wx.BORDER_SUNKEN)
		self.m_staticText321.Wrap(-1)

		bSizer7.Add(self.m_staticText321, 2, wx.ALL, 5)

		self.m_staticText331 = wx.StaticText(self, wx.ID_ANY, _(u"名称"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText331.Wrap(-1)

		bSizer7.Add(self.m_staticText331, 0, wx.ALL, 5)

		self.m_staticText341 = wx.StaticText(self, wx.ID_ANY, _(u"NaN"), wx.DefaultPosition, wx.DefaultSize, wx.ST_NO_AUTORESIZE|wx.BORDER_SUNKEN)
		self.m_staticText341.Wrap(-1)

		bSizer7.Add(self.m_staticText341, 1, wx.ALL, 5)

		self.m_staticText351 = wx.StaticText(self, wx.ID_ANY, _(u"年"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText351.Wrap(-1)

		bSizer7.Add(self.m_staticText351, 0, wx.ALL, 5)

		self.m_staticText361 = wx.StaticText(self, wx.ID_ANY, _(u"NaN"), wx.DefaultPosition, wx.DefaultSize, wx.ST_NO_AUTORESIZE|wx.BORDER_SUNKEN)
		self.m_staticText361.Wrap(-1)

		bSizer7.Add(self.m_staticText361, 1, wx.ALL, 5)

		self.m_staticText371 = wx.StaticText(self, wx.ID_ANY, _(u"月"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText371.Wrap(-1)

		bSizer7.Add(self.m_staticText371, 0, wx.ALL, 5)

		self.m_staticText381 = wx.StaticText(self, wx.ID_ANY, _(u"NaN"), wx.DefaultPosition, wx.DefaultSize, wx.ST_NO_AUTORESIZE|wx.BORDER_SUNKEN)
		self.m_staticText381.Wrap(-1)

		bSizer7.Add(self.m_staticText381, 1, wx.ALL, 5)

		self.m_staticText391 = wx.StaticText(self, wx.ID_ANY, _(u"日"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText391.Wrap(-1)

		bSizer7.Add(self.m_staticText391, 0, wx.ALL, 5)

		self.m_staticText401 = wx.StaticText(self, wx.ID_ANY, _(u"NaN"), wx.DefaultPosition, wx.DefaultSize, wx.ST_NO_AUTORESIZE|wx.BORDER_SUNKEN)
		self.m_staticText401.Wrap(-1)

		bSizer7.Add(self.m_staticText401, 1, wx.ALL, 5)

		self.m_staticText411 = wx.StaticText(self, wx.ID_ANY, _(u"时"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText411.Wrap(-1)

		bSizer7.Add(self.m_staticText411, 0, wx.ALL, 5)

		self.m_staticText42 = wx.StaticText(self, wx.ID_ANY, _(u"NaN"), wx.DefaultPosition, wx.DefaultSize, wx.ST_NO_AUTORESIZE|wx.BORDER_SUNKEN)
		self.m_staticText42.Wrap(-1)

		bSizer7.Add(self.m_staticText42, 1, wx.ALL, 5)

		self.m_staticText43 = wx.StaticText(self, wx.ID_ANY, _(u"分"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText43.Wrap(-1)

		bSizer7.Add(self.m_staticText43, 0, wx.ALL, 5)

		self.m_staticText44 = wx.StaticText(self, wx.ID_ANY, _(u"NaN"), wx.DefaultPosition, wx.DefaultSize, wx.ST_NO_AUTORESIZE|wx.BORDER_SUNKEN)
		self.m_staticText44.Wrap(-1)

		bSizer7.Add(self.m_staticText44, 1, wx.ALL, 5)

		self.m_staticText45 = wx.StaticText(self, wx.ID_ANY, _(u"秒"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText45.Wrap(-1)

		bSizer7.Add(self.m_staticText45, 0, wx.ALL, 5)


		sbSizer9.Add(bSizer7, 1, wx.EXPAND, 5)

		bSizer51 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_textCtrl7 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_STATIC)
		self.m_textCtrl7.SetMaxLength(8)
		bSizer51.Add(self.m_textCtrl7, 2, wx.ALL, 5)

		self.m_staticText25 = wx.StaticText(self, wx.ID_ANY, _(u"名称"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText25.Wrap(-1)

		bSizer51.Add(self.m_staticText25, 0, wx.ALL, 5)

		self.m_textCtrl81 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_STATIC)
		self.m_textCtrl81.SetMaxLength(2)
		bSizer51.Add(self.m_textCtrl81, 1, wx.ALL, 5)

		self.m_staticText261 = wx.StaticText(self, wx.ID_ANY, _(u"年"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText261.Wrap(-1)

		bSizer51.Add(self.m_staticText261, 0, wx.ALL, 5)

		self.m_textCtrl91 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_STATIC)
		self.m_textCtrl91.SetMaxLength(2)
		bSizer51.Add(self.m_textCtrl91, 1, wx.ALL, 5)

		self.m_staticText271 = wx.StaticText(self, wx.ID_ANY, _(u"月"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText271.Wrap(-1)

		bSizer51.Add(self.m_staticText271, 0, wx.ALL, 5)

		self.m_textCtrl101 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_STATIC)
		self.m_textCtrl101.SetMaxLength(2)
		bSizer51.Add(self.m_textCtrl101, 1, wx.ALL, 5)

		self.m_staticText281 = wx.StaticText(self, wx.ID_ANY, _(u"日"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText281.Wrap(-1)

		bSizer51.Add(self.m_staticText281, 0, wx.ALL, 5)

		self.m_textCtrl11 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_STATIC)
		self.m_textCtrl11.SetMaxLength(2)
		bSizer51.Add(self.m_textCtrl11, 1, wx.ALL, 5)

		self.m_staticText291 = wx.StaticText(self, wx.ID_ANY, _(u"时"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText291.Wrap(-1)

		bSizer51.Add(self.m_staticText291, 0, wx.ALL, 5)

		self.m_textCtrl12 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_STATIC)
		self.m_textCtrl12.SetMaxLength(2)
		bSizer51.Add(self.m_textCtrl12, 1, wx.ALL, 5)

		self.m_staticText301 = wx.StaticText(self, wx.ID_ANY, _(u"分"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText301.Wrap(-1)

		bSizer51.Add(self.m_staticText301, 0, wx.ALL, 5)

		self.m_textCtrl13 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_STATIC)
		self.m_textCtrl13.SetMaxLength(2)
		bSizer51.Add(self.m_textCtrl13, 1, wx.ALL, 5)

		self.m_staticText311 = wx.StaticText(self, wx.ID_ANY, _(u"秒"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText311.Wrap(-1)

		bSizer51.Add(self.m_staticText311, 0, wx.ALL, 5)


		sbSizer9.Add(bSizer51, 1, wx.EXPAND, 5)

		bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_button91 = wx.Button(self, wx.ID_ANY, _(u"增加待办"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_button91.Enable(False)

		bSizer6.Add(self.m_button91, 1, wx.ALL, 5)

		self.m_button101 = wx.Button(self, wx.ID_ANY, _(u"删除待办"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_button101.Enable(False)

		bSizer6.Add(self.m_button101, 1, wx.ALL, 5)

		self.m_button11 = wx.Button(self, wx.ID_ANY, _(u"更改待办"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_button11.Enable(False)

		bSizer6.Add(self.m_button11, 1, wx.ALL, 5)


		sbSizer9.Add(bSizer6, 1, wx.EXPAND, 5)


		gbSizer8.Add(sbSizer9, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.EXPAND|wx.ALL, 5)

		sbSizer45 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _(u"报告")), wx.VERTICAL)

		sbSizer45.SetMinSize(wx.Size( -1,300 ))
		self.m_textCtrl14 = wx.TextCtrl(self, wx.ID_ANY, _(u"欢迎使用日程待办控制台\n"), wx.DefaultPosition, wx.DefaultSize, wx.TE_BESTWRAP|wx.TE_LEFT|wx.TE_MULTILINE|wx.TE_READONLY|wx.BORDER_STATIC|wx.VSCROLL)
		sbSizer45.Add(self.m_textCtrl14, 1, wx.ALL|wx.EXPAND, 5)


		gbSizer8.Add(sbSizer45, wx.GBPosition(4, 0), wx.GBSpan(1, 1), wx.EXPAND, 5)


		gbSizer8.AddGrowableCol(0)

		gbSizer6.Add(gbSizer8, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL|wx.EXPAND, 5)


		gbSizer6.AddGrowableCol(1)
		gbSizer6.AddGrowableRow(0)

		self.SetSizer( gbSizer6 )
		self.Layout()
		gbSizer6.Fit( self )

		self.Centre(wx.BOTH)

		# Connect Events
		self.m_button2.Bind(wx.EVT_BUTTON, self.OpenSerialH)
		self.m_button3.Bind(wx.EVT_BUTTON, self.CloseSerialH)
		self.m_button4.Bind(wx.EVT_BUTTON, self.AddSerialH)
		self.m_button5.Bind(wx.EVT_BUTTON, self.DelSerialH)
		self.m_button6.Bind(wx.EVT_BUTTON, self.ExitH)
		self.m_checkList2.Bind(wx.EVT_LISTBOX, self.UpdateDisplayByCheckH)
		self.m_button27.Bind(wx.EVT_BUTTON, self.ReadDataH)
		self.m_button9.Bind(wx.EVT_BUTTON, self.ChangeTimeH)
		self.m_button10.Bind(wx.EVT_BUTTON, self.ClearTimeH)
		self.m_button91.Bind(wx.EVT_BUTTON, self.AddTodoH)
		self.m_button101.Bind(wx.EVT_BUTTON, self.DelTodoH)
		self.m_button11.Bind(wx.EVT_BUTTON, self.ChangeTodoH)

	def __del__( self ):
		# Disconnect Events
		self.m_button2.Unbind(wx.EVT_BUTTON, None)
		self.m_button3.Unbind(wx.EVT_BUTTON, None)
		self.m_button4.Unbind(wx.EVT_BUTTON, None)
		self.m_button5.Unbind(wx.EVT_BUTTON, None)
		self.m_button6.Unbind(wx.EVT_BUTTON, None)
		self.m_checkList2.Unbind(wx.EVT_LISTBOX, None)
		self.m_button27.Unbind(wx.EVT_BUTTON, None)
		self.m_button9.Unbind(wx.EVT_BUTTON, None)
		self.m_button10.Unbind(wx.EVT_BUTTON, None)
		self.m_button91.Unbind(wx.EVT_BUTTON, None)
		self.m_button101.Unbind(wx.EVT_BUTTON, None)
		self.m_button11.Unbind(wx.EVT_BUTTON, None)


	# Virtual event handlers, overide them in your derived class
	def OpenSerialH( self, event ):
		event.Skip()

	def CloseSerialH( self, event ):
		event.Skip()

	def AddSerialH( self, event ):
		event.Skip()

	def DelSerialH( self, event ):
		event.Skip()

	def ExitH( self, event ):
		event.Skip()

	def UpdateDisplayByCheckH( self, event ):
		event.Skip()

	def ReadDataH( self, event ):
		event.Skip()

	def ChangeTimeH( self, event ):
		event.Skip()

	def ClearTimeH( self, event ):
		event.Skip()

	def AddTodoH( self, event ):
		event.Skip()

	def DelTodoH( self, event ):
		event.Skip()

	def ChangeTodoH( self, event ):
		event.Skip()


#--------------------------------------------------------------------------
#  Class MyDialog2
#---------------------------------------------------------------------------

class MyDialog2 ( wx.Dialog ):

	def __init__(self, parent):
		wx.Dialog.__init__ (self, parent, id = wx.ID_ANY, title = _(u"自定义标题"), pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

		bSizer8 = wx.BoxSizer(wx.VERTICAL)

		self.m_textCtrl15 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_STATIC)
		self.m_textCtrl15.SetMinSize(wx.Size( 200,-1 ))

		bSizer8.Add(self.m_textCtrl15, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_button12 = wx.Button(self, wx.ID_ANY, _(u"OK"), wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer8.Add(self.m_button12, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)


		self.SetSizer( bSizer8 )
		self.Layout()
		bSizer8.Fit( self )

		self.Centre(wx.BOTH)

		# Connect Events
		self.m_button12.Bind(wx.EVT_BUTTON, self.EasyDialogH)

	def __del__( self ):
		# Disconnect Events
		self.m_button12.Unbind(wx.EVT_BUTTON, None)


	# Virtual event handlers, overide them in your derived class
	def EasyDialogH( self, event ):
		event.Skip()


