---
title: mybits第二天笔记
tags:
  - 总结
  - mybits总结
categories:
  - mybits
keywords: "多表查询，总结"
cover: https://p7.qhimg.com/bdr/__85/t0127f0c82a2f151104.jpg
toc: True
abbrlink: 20220830
---
在之前所进行的查询之中可以发现 FROM 子句之中只会存在有一张数据表，所以之前都只是针对于单表查询操作， 而所谓的多表查询指的是同时从多张数据表之中取出数据实现的查询，重点修改的是 FROM 子句
## 一对一
``` bash
<!--当属性名和字段名不一致的时候需要配置，如果属性名和字段名保持一致则不需要配置resultMap-->
    <resultMap id="findUser" type="User">
        <id column="id" property="id"></id>
        <result column="user_name" property="userName"></result>
        <result column="user_age" property="userAge"></result>
        <result column="user_sex" property="userSex"></result>
        <result column="user_tel" property="userTel"></result>
        <result column="user_pwd" property="userPwd"></result>
        <!--配置一对一的级联操作-->
        <!--property:次类属性，javaType：该属性所对应的类型-->
        <association property="idCard" javaType="IdCard">
            <id column="id" property="id"></id>
            <result column="card_name" property="cardName"></result>
            <result column="card_address" property="cardAddress"></result>
            <result column="card_num" property="cardNum"></result>
        </association>
    </resultMap>
```
## 一对多
``` code
 <resultMap id="findUser2" type="User">
        <id column="user_id" property="id"></id>
        <result column="user_name" property="userName"></result>
        <result column="user_age" property="userAge"></result>
        <result column="user_sex" property="userSex"></result>
        <result column="user_tel" property="userTel"></result>
        <result column="user_pwd" property="userPwd"></result>
        <!--配置一对多的级联操作-->
        <!--property:次类属性，ofType：该属性所对应的类型-->
        <collection property="orders" ofType="Order">
            <!--column：sql语句执行完成后的字段名-->
            <id column="order_id" property="id"></id>
            <result column="order_name" property="orderName"></result>
            <result column="order_price" property="orderPrice"></result>
            <result column="order_time" property="orderTime"></result>
        </collection>
    </resultMap>
```
## 多对多
``` code
 <resultMap id="findUser1" type="User">
        <result column="user_name" property="userName"></result>
    </resultMap>
    <!--User queryUserById(Integer id);-->
    <!--接口方式访问，id值为对应接口中的方法名-->
    <!--resultType="com.hqyj.gyq.entity.User" 当表中的字段名和实体类的属性名相同则可以自动映射上，如果不同就不适用，使用resultMap-->
    <select id="selectUserById"  resultMap="findUser">
        select * from user where user_id = #{id}
    </select>

    <select id="selectUserById1"  resultMap="findUser">
        select * from user u,idCard i where u.user_id = #{id} and i.id = u.card_id
    </select>

    <!--如果是多表联查，注意：表中的字段名相同了，最好建表时候进行区分，或者在sql语句中取别名区分-->
    <select id="selectUserById2"   resultMap="findUser2">
            SELECT*,o.id order_id FROM user u,t_order o  where u.user_id = #{id} and u.user_id=o.user_id
    </select>

```

## 总结
多表查询首先要分清楚主次关系。我们首先要查询什么然后在次查询里编写我们的sql语句进行联表查询。
