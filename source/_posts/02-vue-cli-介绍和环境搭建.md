---
title: Vue cli 介绍
tags:
  - Vue cli 介绍
  - Vue cli
categories:
  - Vue
keywords: "Vue，cli"
cover: https://fastly.jsdelivr.net/gh/tzy13755126023/BLOG_SOURCE/gallery_f/ACG/20201230_15.jpg
toc: True
abbrlink: 20221018
---



#  **Vue cli 介绍**

**什么是vue-cli**

vue-cli是由vue官方发布的快速构建vue单页面的脚手架

**为什么要用vue-cli构建项目**

 用vue-cli可以实现webpack的快速打包

代码重用

兼容ES6 

兼容nodeJS 

#  Vue cli 环境搭建

1. 安装node.js

​         Node.js 官方网站下载：https://nodejs.org/en/               

 

2. 下载完毕后，可以安装node，建议不要安装在系统盘。

3. 设置nodejs prefix（全局）和cache（缓存）路径

   一、在nodejs安装路径下，新建node_global和node_cache两个文件夹

   ![image-20210824092715825](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20210824092715825.png)

   二、设置缓存文件夹

   ​        npm config set cache "D:\vueProject\nodejs\node_cache"

   三　设置全局模块存放路径

   ​      npm config set prefix "D:\vueProject\nodejs\node_global"


   4   基于 Node.js 安装cnpm（淘宝镜像）

​       npm install -g cnpm --registry=https://registry.npm.taobao.org

​    

   5   设置环境变量（非常重要）

   说明：设置环境变量可以使得住任意目录下都可以使用cnpm、vue等命令，而不需要输入全路径

   1、鼠标右键"此电脑"，选择“属性”菜单，在弹出的“系统”对话框中左侧选择“高级系统设置”，弹出“系统属性”对话框。

   2、修改系统变量PATH

   ![image-20210824092919303](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20210824092919303.png)

![image-20210824092929861](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20210824092929861.png)

新增系统变量NODE_PATH

![image-20210824093002833](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20210824093002833.png)



6   安装Vue

  cnpm install vue -g 或者   npm install vue -g

![image-20210824093035739](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20210824093035739.png)

7  安装vue命令行工具，即vue-cli 脚手架

cnpm install vue-cli -g 或者 npm install vue-cli -g

![image-20210824093104047](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20210824093104047.png)

8 搭建完毕

