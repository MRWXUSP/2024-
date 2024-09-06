# 日程待办大作业

**构建**
学习板代码文件存在于```/output```中，第一次启动需要在main()函数添加
```
M24C02_Write(0x00,0x00)
WriteDelay();
M24C02_Write(0x01,0x00)
WriteDelay();
M24C02_Write(0x02,0x00)
WriteDelay();
```
以初始化非易失性存储单元

若要运行GUI，需要系统有**python3环境**与**wxpyhton**软件包
>```获取wxpython```
>```pip install -U wxpython```

>```运行GUI（仅在windows可运行）```
>```/works/main.py```

**生成**
生成exe可运行程序需要**pyinstaller**软件包
>```获取pyinstaller```
>```pip install pyinstaller```

>```打包```
>```pyinstaller -F main.py```
>```pyinstaller -w -F main.py  (去掉控制台窗口的版本)```

**文件**
```
workfile
|-__pychane__   python运行时文件夹
|-DataDown.py   数据处理函数库
|-GUI_Back.py   GUI中间件-后端连接器
|-GUI_Head.py   GUI前端
output
|-BSP_DEMO.hex  STC-B板程序
main.py         主程序
README.md       帮助文档
```