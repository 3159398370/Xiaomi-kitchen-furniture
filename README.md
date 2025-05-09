# Xiaomi-kitchen-furniture
小米厨房家具django作业项目

项目是基于 Django 框架开发的“小米智能厨房家具”管理与展示平台，主要功能和结构如下：

## 1. 项目结构说明

djangoProject/
├── manage.py
├── db.sqlite3
├── static/
├── xiaomi/           # 主项目配置
├── xiaomijiaju/      # 主要业务应用
├── furniture/        # 其他业务应用

xiaomi/ Django 主项目目录，包含全局配置（如 settings.py、urls.py、wsgi.py、asgi.py）。

xiaomijiaju/ 这是一个 Django 应用，核心功能模块。

models.py ：定义了两个主要数据模型： Product （产品）和 InstallationRequest （安装预约）。

Product 用于存储厨房家具产品的信息（如名称、描述、价格、图片、分类等）。

InstallationRequest 用于存储用户的安装预约请求（如姓名、电话、地址、预约产品、时间、备注）。

views.py ：实现了产品列表、分类导航、厨房家具展示、安装预约、关于页面、用户登录注册等视图逻辑。

templates/ ：存放前端页面模板，包括产品列表、分类导航、安装预约、登录注册等页面，风格现代，支持 Bootstrap。

migrations/ ：数据库迁移文件，自动生成的数据表结构变更记录。

furniture/ 另一个 Django 应用，用于后续扩展或测试。

static/ 静态资源目录，包含 CSS 样式和图片（如产品图片、logo 等），供前端页面引用。

db.sqlite3 SQLite 数据库文件，存储所有数据（如用户、产品、预约等）。

manage.py Django 项目的管理脚本，用于运行开发服务器、数据库迁移等操作。

### 2. 主要功能模块

产品展示与分类 用户可以浏览厨房家具产品列表，支持分类导航（如厨房储物、桌台、电器等），每个产品有图片、价格、描述等信息。

安装预约 用户可在线填写表单，预约家具安装服务，后台会保存用户的预约信息。

用户系统 支持用户注册、登录、退出、账号删除等功能，部分页面需要用户登录后才能访问。

关于页面 展示小米公司及智能厨房家具系列的品牌介绍、企业愿景等内容。

美观的前端页面 使用 Bootstrap 进行页面布局和美化，响应式设计，适合多种设备访问。

### 3. 技术栈

后端 ：Python 3 + Django 框架

数据库 ：SQLite（开发环境默认）

前端 ：HTML + CSS+ Django 模板

静态资源管理 ：Django 静态文件机制



本项目注册用户信息的存储和输入校验机制如下：

### 1. 用户信息的存储方式

​	本项目采用 Django 框架自带的用户系统（django.contrib.auth），用户信息（如用户名、密码等）存储在数据库（默认是 db.sqlite3）中的 auth_user 表。

​	在 xiaomijiaju/views.py 的 register 视图函数中，调用了 User.objects.create_user(username=username, password=password) ，即使用 Django 的 User 模型创建新用户，自动将用户信息写入数据库。

用户密码会自动加密存储，保证安全性。

### 2. 用户输入信息的校验方式 前端校验

在 xiaomijiaju/templates/register.html 中，表单字段（如用户名、手机号、密码）都设置了 HTML5 校验规则并配合 JavaScript 实现了实时校验和提交前校验。

例如：
- 用户名： pattern="[A-Za-z0-9_]{3,20}" ，要求3-20位字母、数字或下划线。
- 手机号： pattern="^1[3-9]\d{9}$" ，要求11位中国大陆手机号。
- 密码： minlength="6" ，要求至少6位。

- JS 脚本会在表单提交时检查两次密码是否一致、用户名和手机号格式是否正确，不符合则阻止提交并显示错误提示。 后端校验

- 在 xiaomijiaju/views.py 的 register 视图函数中，后端再次对所有关键字段进行严格校验，包括：
  - 两次密码是否一致
  - 用户名格式是否正确
  - 手机号格式是否正确
  - 密码长度是否足够
  - 用户名是否已存在

  校验失败时，使用 messages.error 返回错误信息，并重新渲染注册页面，防止恶意绕过前端校验。

### 3. 典型流程总结

1. 用户在注册页面填写信息，前端实时校验格式。
2. 提交表单后，后端再次校验所有输入。
3. 校验通过则调用 User.objects.create_user 存储用户信息到数据库。
4. 校验不通过则返回错误提示，用户需修改后重新提交。

用户信息获取和写入数据库的流程。

1. 前端表单收集信息 以 register.html 或 login.html 为例，页面中有 <form> 表单，用户在表单中填写用户名、密码等信息。 表单通常会有 method="post" ，并指定 action

2. 用户填写后点击提交，浏览器会将这些数据通过 POST 请求发送到后端。

   后端视图处理请求 Django 的视图（views.py）会有对应的处理函数或类视图

   - request.POST.get("字段名") 就是获取用户填入的信息。
     然后通过 Django 的 ORM（如 User.objects.create(...) ）将数据写入数据库。

模型（models.py）定义数据结构

用户在前端页面填写表单，提交后数据通过 POST 发送到后端。

后端用 request.POST.get() 获取数据。

用 ORM（如 User.objects.create ）写入数据库。

1. **Django框架核心表**
   
   auth_group → 权限组表
   
   auth_group_permissions → 权限组权限关联表
   
   auth_permission → 权限明细表
   
   auth_user → 用户认证表
   
   auth_user_groups → 用户组关联表
   
   auth_user_user_permissions → 用户权限关联表
   
   django_admin_log → 后台操作日志表
   
   django_content_type → 内容类型表
   
   django_migrations → 数据迁移记录表
   
   django_session → 会话状态表
2. **业务自定义表**
   
   xiaomijiaju_installationrequest → 小米家具_安装申请工单表（
   
   xiaomijiaju_product → 小米家具_产品信息表



代富强：组长，负责协调各个组员的配合，设计出了前期流程框架，做什么，怎么做的大纲，完成登录，注册，删除页面的html,css,js实现，并设计基础数据库表，解决数据库问题，并实现与数据库联动

贾培坤：安装预约，关于小米两个页面实现，并设计用户表单写入数据库程序，与刘春博二人完成其前端转成django的项目结构

刘春博：分类导航，厨房家具两个页面实现，设计尾页导航栏跳转，并提供所有页面使用的素材，设计商品价格，维护数据库，并与代富强贾培坤三人完成主页设计
