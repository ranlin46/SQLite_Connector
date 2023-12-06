# SQLite 连接器

## 概述
该程序是一个简单的学生信息管理系统，使用 Python 的 Tkinter 库进行图形用户界面设计，并使用 SQLite 数据库进行数据存储。用户可以通过界面实现学生信息的添加、显示、更新、删除和搜索等功能。

## 功能
程序提供以下主要功能：

1. **添加新记录：** 用户可以输入学生的信息，包括学生ID、姓名、姓氏、地址、性别和手机号码，然后点击“Add New”按钮将信息添加到数据库中。

2. **显示记录：** 用户可以点击“Display”按钮查看数据库中的所有学生记录，以表格形式展示在界面上。

3. **更新记录：** 用户可以选中表格中的某一行记录，然后在界面上更新该学生的信息，然后点击“Update”按钮将更新后的信息保存到数据库中。

4. **删除记录：** 用户可以选中表格中的某一行记录，然后点击“Delete”按钮将该学生的记录从数据库中删除。

5. **搜索记录：** 用户可以输入学生ID，然后点击“Search”按钮来查找数据库中是否存在该学生的记录，如果存在则将学生信息显示在界面上。

6. **重置表单：** 用户可以点击“Reset”按钮清空输入框中的内容，以便添加新的学生信息。

7. **退出程序：** 用户可以点击“Exit”按钮退出程序，会弹出确认对话框以确保用户不会误操作退出。

## 数据存储
学生信息存储在一个 SQLite 数据库文件（`trainee.db`）中，包含一个名为 `train` 的表用于存储学生记录。

## 如何运行程序
1. 安装 Python（如果未安装）。
2. 打开终端或命令提示符。
3. 进入程序所在的目录。
4. 运行命令 `mian.py`。

## 注意事项
- 在运行程序之前，请确保已安装了 Tkinter 和 SQLite 相关的库。
- 如果首次运行程序，将创建一个名为 `trainee.db` 的数据库文件。确保有写入权限。
- 如果程序在运行时出现任何问题，请检查控制台或终端输出以获取更多信息。


## 版本历史
- 版本 1.0（日期）：初始版本。