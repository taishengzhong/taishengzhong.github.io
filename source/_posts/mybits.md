---
title: mybits第一天笔记
tags:
  - 总结
  - mybits总结
categories:
  - mybits
keywords: "hello，总结"
cover: https://p6.qhimg.com/bdr/__85/t01945d79566462c0fb.jpg
toc: True
abbrlink: 20220829
---
## 1、通过命名空间访问（了解）
1、创建动态web工程
2、导入相关的jar包（commons-logging-1.2.jar、log4j-1.2.17.jar、mybatis-3.4.2.jar、mysql-connector-java-5.1.21.jar）
3、在src下面创建mybatis的核心配置文件mybatis-config.xml(文档):
``` BASH
<configuration>
//配置连接数据库的四大基本参数（db.properties）
    <properties resource="db.properties"></properties>
    //环境配置
    <environments default="development">
        <environment id="development">
        //事务管理
            <transactionManager type="JDBC"/>
            //连接数据库（mybatis默认的连接池）
            <dataSource type="POOLED">
                <property name="driver" value="${jdbc.driverClassName}"/>
                <property name="url" value="${jdbc.url}"/>
                <property name="username" value="${jdbc.username}"/>
                <property name="password" value="${jdbc.password}"/>
            </dataSource>
        </environment>
<!--        <environment id="test">-->
<!--            <transactionManager type="JDBC"/>-->
<!--            <dataSource type="POOLED">-->
<!--                <property name="driver" value="${driver}"/>-->
<!--                <property name="url" value="${url}"/>-->
<!--                <property name="username" value="${username}"/>-->
<!--                <property name="password" value="${password}"/>-->
<!--            </dataSource>-->
<!--        </environment>-->
    </environments>
    //加载对应的mapper映射文件
    <mappers>
        <mapper resource="com\hqyj\gyq\entity\UserMapper.xml"/>
    </mappers>
</configuration>
```
### 1.db.properties部分
``` bash
jdbc.driverClassName=com.mysql.jdbc.Driver
    jdbc.url=jdbc:mysql://127.0.0.1:3306/j220701
    jdbc.username=root
    jdbc.password=123456
```

### 2.创建dao包以及对应的实现类的包：

### 3.在dao包中编写接口UserDao
### 4.编写对应的实现类
### 5.编写对应的映射文件（UserMapper.xml---->实体类+Mapper.xml）:
``` bash
<!--命名空间值，一般来说写对应接口的完全限定名-->
    <mapper namespace="com.hqyj.gyq.dao.UserDao">

        <!--当属性名和字段名不一致的时候需要配置，如果属性名和字段名保持一致则不需要配置resultMap-->
        <resultMap id="findUser" type="com.hqyj.gyq.entity.User">
            <id column="id" property="id"></id>
            <result column="user_name" property="userName"></result>
            <result column="user_age" property="userAge"></result>
            <result column="user_sex" property="userSex"></result>
            <result column="user_tel" property="userTel"></result>
            <result column="user_pwd" property="userPwd"></result>
        </resultMap>
        <!--id值唯一，用来做精确定位的（找到该命名空间下的哪一个sql语句）-->
        <select id="selectUserById" resultMap="findUser">
            select * from user where id = #{id}
        </select>
    </mapper>
```
## 2、编写测试类  通过接口方式访问（掌握）
1-3同上

### 1.创建mapper包，编写UserMapper接口
### 2.在对应映射文件里面编写sql语句，注意（id值一定与接口的方法名保持一致）
### 3.编写测试类，使用session.getMapper()获取对应的对象-----》原理：使用动态代理模式创建了对应mapper接口的实现类

