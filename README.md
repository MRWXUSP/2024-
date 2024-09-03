# 日程待办大作业

**构建**
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
main.py         主程序
README.md
```