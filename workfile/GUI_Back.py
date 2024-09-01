# -*- coding: utf-8 -*-

'''
本文件为GUI界面的前端处理事件,与后端交换数据接口中间件,此文件需要添加之处会标明;
请不要在此文件添加后端函数代码实例,仅填充函数使用语句即可
'''
#import <你的后端文件名>
import wx
import time


from . import GUI_Head

#以下为数据类型定义,请不要修改
#在待办条目中会以:"Name\tTime"的形式体现
class DataType:
    Name = 'string' #代办名，中间件会进行检查，不允许出现除字母外的字符，不得超过八个字符
    Time = 'string' #截止时间，中间件会进行检查，不允许出现除数字、'-'外的字符，格式必须为"YY-MM-DD-HH-MM-SS"
    def __init__(self):
        self.Name = ''
        self.Time = ''
    
    def SetDataByNT(self, Name, Time):
        self.Name = Name
        self.Time = Time
    
    def SetDataByString(self, Data):
        TempData = Data.split('\t')
        self.Name = TempData[0]
        self.Time = TempData[1]


class GUI_Back( GUI_Head.MyFrame1 ):
    def __init__( self, parent ):
        GUI_Head.MyFrame1.__init__( self, parent )
    
    #此函数为输出日志的函数,参数为输出的日志string,前带有标准化输出的时间,注意日志自带换行
    def OutPutLog(self, log):
        TempTime = time.strftime('[%Y-%m-%d %H:%M:%S]: ',time.localtime(time.time()))
        self.m_textCtrl14.AppendText(TempTime+log+'\n')

    #此函数为待办列表按时间排序函数，在改动列表后自动调用，没有返回值，排序成功后会自动更新列表
    def ListSort(self):
        TempList = []
        for i in range(self.m_checkList2.GetCount()):
            TempData = DataType()
            TempData.SetDataByString(self.m_checkList2.GetString(i))
            TempList.append(TempData)
        TempList.sort(key=lambda x:x.Time)
        self.m_checkList2.Clear()
        for i in range(len(TempList)):
            self.m_checkList2.Append(TempList[i].Name+'\t'+TempList[i].Time)

    #此函数为串口打开按钮的事件处理函数
    def OpenSerialH( self, event ):
        self.OutPutLog("正在打开串口...")
        #以下四个参数分别为:串口号,波特率,数据位数,校验位数,停止位数,数据类型为string
        SerialPort = self.m_choice1.GetStringSelection()
        SerialBaud = self.m_choice2.GetStringSelection()
        Serial_Data = self.m_choice3.GetStringSelection()
        Serial_Check = self.m_choice4.GetStringSelection()
        Serial_Stop = self.m_choice5.GetStringSelection()
        '''此处添加串口打开函数,并且将返回值赋给SerialState,返回值为串口状态,成功为'OPEN',失败为'CLOSE' '''
        SerialState = 'OPEN'
        self.OutPutLog("串口号:"+SerialPort+" 波特率:"+SerialBaud+" 数据位:"+Serial_Data+" 校验位:"+Serial_Check+" 停止位:"+Serial_Stop)
        if SerialState == 'OPEN':
            self.OutPutLog("串口打开成功")
            self.m_button2.Enable(False)
            self.m_button3.Enable(True)
            self.m_button4.Enable(False)
            self.m_button5.Enable(False)
            self.m_button6.Enable(False)
            self.ReadDataH(event)
            self.m_button27.Enable(True)
            self.m_button9.Enable(True)
            self.m_button10.Enable(True)
            self.m_button91.Enable(True)
            self.m_button101.Enable(True)
            self.m_button11.Enable(True)
        else:
            self.OutPutLog("串口打开失败")
        event.Skip()
    
    #此函数为串口关闭按钮的事件处理函数
    def CloseSerialH( self, event ):
        self.OutPutLog("正在关闭串口...")
        '''此处添加串口关闭函数,并且将返回值赋给SerialState,返回值为串口状态,成功为'CLOSE',失败为'OPEN' '''
        SerialState = 'CLOSE'
        if SerialState == 'OPEN':
            self.OutPutLog("串口关闭失败")
        else:
            self.OutPutLog("串口关闭成功")
            self.m_button2.Enable(True)
            self.m_button3.Enable(False)
            self.m_button4.Enable(True)
            self.m_button5.Enable(True)
            self.m_button6.Enable(True)
            self.m_button27.Enable(False)
            self.m_button9.Enable(False)
            self.m_button10.Enable(False)
            self.m_button91.Enable(False)
            self.m_button101.Enable(False)
            self.m_button11.Enable(False)

        event.Skip()
    
    #此函数为添加串口按钮的事件处理函数
    def AddSerialH( self, event ):
        TempDialog = Dialog_Back(self)
        TempDialog.Title = "请输入串口号"
        TempDialog.m_textCtrl15.SetValue('')
        TempDialog.ShowModal()
        while TempDialog.IsShown() :
            pass
        if TempDialog.Title == "###增加串口号###":
            TempSerial = TempDialog.m_textCtrl15.GetValue()
            self.m_choice1.Insert(TempSerial,self.m_choice1.GetCount()-1)
        event.Skip()
    
    #此函数为删除串口按钮的事件处理函数
    def DelSerialH( self, event ):
        TempDialog = Dialog_Back(self)
        TempDialog.Title = "确定删除串口号?"
        TempDialog.m_textCtrl15.Show(False)
        TempDialog.ShowModal()
        while TempDialog.IsShown() :
            pass
        if TempDialog.Title == "###删除串口号###":
            self.m_choice1.Delete(self.m_choice1.GetSelection())
            self.m_choice1.SetSelection(-1)
        event.Skip()

    #此函数为退出程序按钮的事件处理函数
    def ExitH( self, event ):
        self.Destroy()
    
    #此函数为勾选待办条目后的事件处理函数
    def UpdateDisplayByCheckH( self, event ):
        TempData = DataType()
        TempData.SetDataByString(self.m_listBox1.GetString(self.m_listBox1.GetSelection()))
        self.m_staticText321.Label = TempData.Name
        self.m_staticText341.Label = TempData.Time[0:2]
        self.m_staticText361.Label = TempData.Time[3:5]
        self.m_staticText381.Label = TempData.Time[6:8]
        self.m_staticText401.Label = TempData.Time[9:11]
        self.m_staticText42.Label = TempData.Time[12:14]
        self.m_staticText44.Label = TempData.Time[15:17]
        event.Skip()

    #此函数协助"ReadDataH"判断数据是否合法 0-合法 1-时间或名称为空 2-名称有除字母外的字符 3-名称长度不合法 4-时间格式不合法
    def CheckData(self, DataType):
        if DataType.Name == '' or DataType.Time == '':
            return 1
        for i in range(len(DataType.Name)):
            if not DataType.Name[i].isalpha():
                return 2
        if len(DataType.Name) > 8:
            return 3
        if len(DataType.Time) != 17:
            return 4
        if DataType.Time[2] != '-' or DataType.Time[5] != '-' or DataType.Time[8] != '-' or DataType.Time[11] != '-' or DataType.Time[14] != '-':
            return 4
        if not DataType.Time[0:2].isdigit() or not DataType.Time[3:5].isdigit() or not DataType.Time[6:8].isdigit() or not DataType.Time[9:11].isdigit() or not DataType.Time[12:14].isdigit() or not DataType.Time[15:17].isdigit():
            return 4
        return 0

    #此函数为读取数据按钮的事件处理函数
    def ReadDataH( self, event ):
        self.OutPutLog("正在读取数据...")
        '''此处添加读取数据函数,并且将返回值赋给DataList,返回值为一个list或元组(尽量用元组以避免被更改),
        每个元素为一个DataType类的实例,其中首位元素为当前学习板的时间,名称设置为"NowTime"若返回值为一个空元组,
        则说明数据读取失败,中间件会检查每一个元素的数据类型是否正确,不正确则会报告到日志并忽略该待办事项'''
        DataList = ()
        if len(DataList) == 0:
            self.OutPutLog("数据读取失败")
            event.Skip()
            return
        self.m_checkList2.Clear()
        for i in range(len(DataList)):
            if i == 0:
                if DataList[i].Name != 'NowTime':
                    self.OutPutLog("当前时间数据错误")
                else:
                    self.m_textCtrl2.SetValue(DataList[i].Time[0:2])
                    self.m_textCtrl3.SetValue(DataList[i].Time[3:5])
                    self.m_textCtrl4.SetValue(DataList[i].Time[6:8])
                    self.m_textCtrl8.SetValue(DataList[i].Time[9:11])
                    self.m_textCtrl9.SetValue(DataList[i].Time[12:14])
                    self.m_textCtrl10.SetValue(DataList[i].Time[15:17])
                continue
            if self.CheckData(DataList[i]) == 0:
                self.m_checkList2.Append(DataList[i].Name+'\t'+DataList[i].Time)
            elif self.CheckData(DataList[i]) == 1:
                self.OutPutLog("第"+str(i+1)+"个数据有时间或名称为空,已忽略.名称:"+DataList[i].Name+" 时间:"+DataList[i].Time)
            elif self.CheckData(DataList[i]) == 2:
                self.OutPutLog("第"+str(i+1)+"个数据有名称有除字母外的字符,已忽略.名称:"+DataList[i].Name+" 时间:"+DataList[i].Time)
            elif self.CheckData(DataList[i]) == 3:
                self.OutPutLog("第"+str(i+1)+"个数据有名称长度不合法,已忽略.名称:"+DataList[i].Name+" 时间:"+DataList[i].Time)
            elif self.CheckData(DataList[i]) == 4:
                self.OutPutLog("第"+str(i+1)+"个数据有时间格式不合法,已忽略.名称:"+DataList[i].Name+" 时间:"+DataList[i].Time)
        self.ListSort()
        self.m_checkList2.Enable(True)
        self.OutPutLog("数据读取完毕")
        event.Skip()
    
    #此函数为更改学习板时间按钮的事件处理函数
    def ChangeTimeH( self, event ):
        TempData = DataType()
        TempData.Name = 'ChangeTime'
        TempData.Time = self.m_textCtrl2.GetValue()+'-'+self.m_textCtrl3.GetValue()+'-'+self.m_textCtrl4.GetValue()+'-'+self.m_textCtrl8.GetValue()+'-'+self.m_textCtrl9.GetValue()+'-'+self.m_textCtrl10.GetValue()
        if self.CheckData(TempData) != 0:
            TempDiaLog = Dialog_Back(self)
            TempDiaLog.Title = "要修改的时间不合法!"
            TempDiaLog.m_textCtrl15.Show(False)
            TempDiaLog.ShowModal()
            event.Skip()
            return
        TempDialog = Dialog_Back(self)
        TempDialog.Title = "确定更改时间?"
        TempDialog.m_textCtrl15.Show(False)
        TempDialog.ShowModal()
        while TempDialog.IsShown() :
            pass
        if not TempDialog.Title == "###确定更改时间###":
            event.Skip()
            return
        self.OutPutLog("正在更改时间...")
        #以下为更改时间的数据，是传入你函数的参数
        TempTime = self.m_textCtrl2.GetValue()+'-'+self.m_textCtrl3.GetValue()+'-'+self.m_textCtrl4.GetValue()+'-'+self.m_textCtrl8.GetValue()+'-'+self.m_textCtrl9.GetValue()+'-'+self.m_textCtrl10.GetValue()
        '''此处添加更改时间函数,参数为string型TempTime,并且将返回值赋给TimeState,返回值为时间状态,成功为'TRUE',失败为'FALSE' '''
        TimeState = 'TRUE'
        if TimeState == 'TRUE':
            self.OutPutLog("时间更改成功")
        else:
            self.OutPutLog("时间更改失败")
        event.Skip()
    
    #此函数为清空学习板时间按钮的事件处理函数
    def ClearTimeH( self, event ):
        TempDialog = Dialog_Back(self)
        TempDialog.Title = "确定清空时间?"
        TempDialog.m_textCtrl15.Show(False)
        TempDialog.ShowModal()
        while TempDialog.IsShown() :
            pass
        if not TempDialog.Title == "###确定清空时间###":
            event.Skip()
            return
        self.OutPutLog("正在清空时间...")
        '''此处添加清空时间函数,没有参数,并且将返回值赋给TimeState,返回值为时间状态,成功为'TRUE',失败为'FALSE' '''
        TimeState = 'TRUE'
        if TimeState == 'TRUE':
            self.OutPutLog("时间清空成功")
        else:
            self.OutPutLog("时间清空失败")
        event.Skip()
    
    #此函数为添加待办事项按钮的事件处理函数
    def AddTodoH( self, event ):
        TempData = DataType()
        TempData.Name = self.m_textCtrl7.GetValue()
        TempData.Time = self.m_textCtrl81.GetValue()+'-'+self.m_textCtrl91.GetValue()+'-'+self.m_textCtrl101.GetValue()+'-'+self.m_textCtrl11.GetValue()+'-'+self.m_textCtrl12.GetValue()+'-'+self.m_textCtrl13.GetValue()
        if self.CheckData(TempData) != 0:
            TempDiaLog = Dialog_Back(self)
            TempDiaLog.Title = "要添加的时间不合法!"
            TempDiaLog.m_textCtrl15.Show(False)
            TempDiaLog.ShowModal()
            while TempDiaLog.IsShown() :
                pass
            event.Skip()
            return
        self.OutPutLog("正在添加待办事项...")
        #TempData是传入你函数的参数
        '''此处添加添加待办事项函数,参数为类Datatype型,并且将返回值赋给AddState,返回值为添加状态,成功为'TRUE',失败为'FALSE' '''
        AddState = 'TRUE'
        if AddState == 'TRUE':
            self.OutPutLog("待办事项添加成功")
            self.m_checkList2.Append(TempData.Name+'\t'+TempData.Time)
            self.ListSort()
        else:
            self.OutPutLog("待办事项添加失败")
        event.Skip()

            
    #此函数为删除待办事项按钮的事件处理函数
    def DelTodoH( self, event ):
        if self.m_checkList2.GetSelection() == -1:
            TempDiaLog = Dialog_Back(self)
            TempDiaLog.Title = "请选择待办事项!"
            TempDiaLog.m_textCtrl15.Show(False)
            TempDiaLog.ShowModal()
            while TempDiaLog.IsShown() :
                pass
            event.Skip()
            return
        #这是传入你函数的参数
        TempData = DataType()
        TempData.SetDataByString(self.m_checkList2.GetString(self.m_checkList2.GetSelection()))
        self.OutPutLog("正在删除待办事项...")
        '''此处添加删除待办事项函数,并且将返回值赋给DelState,返回值为删除状态,成功为'TRUE',失败为'FALSE' '''
        DelState = 'TRUE'
        if DelState == 'TRUE':
            self.OutPutLog("待办事项删除成功")
            self.m_checkList2.Delete(self.m_checkList2.GetSelection())
        else:
            self.OutPutLog("待办事项删除失败")
        self.ListSort()
        event.Skip()
    
    #此函数为更改待办事项按钮的事件处理函数
    def ChangeTodoH( self, event ):
        if self.m_checkList2.GetSelection() == -1:
            TempDiaLog = Dialog_Back(self)
            TempDiaLog.Title = "请选择待办事项!"
            TempDiaLog.m_textCtrl15.Show(False)
            TempDiaLog.ShowModal()
            while TempDiaLog.IsShown() :
                pass
            event.Skip()
            return
        TempData = DataType()
        TempData.Name = self.m_textCtrl7.GetValue()
        TempData.Time = self.m_textCtrl81.GetValue()+'-'+self.m_textCtrl91.GetValue()+'-'+self.m_textCtrl101.GetValue()+'-'+self.m_textCtrl11.GetValue()+'-'+self.m_textCtrl12.GetValue()+'-'+self.m_textCtrl13.GetValue()
        if self.CheckData(TempData) != 0:
            TempDiaLog = Dialog_Back(self)
            TempDiaLog.Title = "要修改的时间不合法!"
            TempDiaLog.m_textCtrl15.Show(False)
            TempDiaLog.ShowModal()
            while TempDiaLog.IsShown() :
                pass
            event.Skip()
            return
        self.OutPutLog("正在更改待办事项...")
        #TempData是传入你函数的参数
        '''此处添加更改待办事项函数,参数为类Datatype型,并且将返回值赋给ChangeState,返回值为更改状态,成功为'TRUE',失败为'FALSE' '''
        ChangeState = 'TRUE'
        if ChangeState == 'TRUE':
            self.OutPutLog("待办事项更改成功")
            TempData = DataType()
            TempData.Name = self.m_textCtrl7.GetValue()
            TempData.Time = self.m_textCtrl81.GetValue()+'-'+self.m_textCtrl91.GetValue()+'-'+self.m_textCtrl101.GetValue()+'-'+self.m_textCtrl11.GetValue()+'-'+self.m_textCtrl12.GetValue()+'-'+self.m_textCtrl13.GetValue()
            self.m_checkList2.SetString(self.m_checkList2.GetSelection(),TempData.Name+'\t'+TempData.Time)
            self.ListSort()
        else:
            self.OutPutLog("待办事项更改失败")
        event.Skip()

class Dialog_Back( GUI_Head.MyDialog2 ):
    def __init__( self, parent ):
        GUI_Head.MyDialog2.__init__( self, parent )
    
    def EasyDialogH( self, event ):
        if self.Title == "请输入串口号":
            if self.m_textCtrl15.GetValue() == '串口号不能为空':
                self.m_textCtrl15.SetValue('')
            elif self.m_textCtrl15.GetValue() == '':
                self.m_textCtrl15.SetValue("串口号不能为空")
            else:
                self.Show(False)
                self.Title = "###增加串口号###"
        elif self.Title == "确定删除串口号?":
            self.Show(False)
            self.Title = "###删除串口号###"
        elif self.Title == "要修改的时间不合法!":
            self.Show(False)
            self.Title = "###要修改的时间不合法###"
        elif self.Title == "确定更改时间?":
            self.Show(False)
            self.Title = "###确定更改时间###"
        elif self.Title == "确定清空时间?":
            self.Show(False)
            self.Title = "###确定清空时间###"
        elif self.Title == "要添加的时间不合法!":
            self.Show(False)
            self.Title = "###要添加的时间不合法###"
        elif self.Title == "请选择待办事项!":
            self.Show(False)
            self.Title = "###请选择待办事项###"
        event.Skip()
    




