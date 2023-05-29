---
title: springboot整合日志
tags:
  - 日志、整合
  - springboot整合日志
categories:
  - springbootboot
keywords: "springboot，整合，日志"
cover: https://p8.qhimg.com/bdr/__85/t012b51fd84316f0502.jpg
toc: True
abbrlink: 20220829
---

# springboot整合日志

## 1.日志框架的选择

市面上常见的日志框架有很多，它们可以被分为两类：日志门面（日志抽象层）和日志实现，如下表。

| 日志分类        | 描述                                       | 举例                                       |
| ----------- | ---------------------------------------- | ---------------------------------------- |
| 日志门面（日志抽象层） | 为 Java 日志访问提供一套标准和规范的 API 框架，其主要意义在于提供接口。 | JCL（Jakarta Commons Logging）、SLF4j（Simple Logging Facade for Java）、jboss-logging |
| 日志实现        | 日志门面的具体的实现                               | Log4j、JUL（java.util.logging）、Log4j2、Logback |

​     通常情况下，日志由一个日志门面与一个日志实现组合搭建而成，Spring Boot 选用 SLF4J + Logback 的组合来搭建日志系统。

​     SLF4J 是目前市面上最流行的日志门面，使用 Slf4j 可以很灵活的使用占位符进行参数占位，简化代码，拥有更好的可读性。

​     Logback 是 Slf4j 的原生实现框架，它与 Log4j 出自一个人之手，但拥有比 log4j 更多的优点、特性和更做强的性能，现在基本都用来代替 log4j 成为主流

## 2.logback日志配置

### 2.1 springboot配置

在application-*.yml文件中配置：

```yaml
logging:
  file:
    path: D:/logs/springboot
  config: classpath:config/logback-spring.xml
  level:
    root: info
```

logging.file.path：日志存放路径

logging.config：读取logback日志文件配置，logback-spring.xml文件名尽量固定

logging.level：日志级别

### 2.2 logback-spring.xml配置

在项目的resources目录下创建config文件夹，在该文件夹下创建logback-spring.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- 日志级别从低到高分为TRACE < DEBUG < INFO < WARN < ERROR < FATAL，如果设置为WARN，则低于WARN的信息都不会输出 -->
<configuration>

    <!-- 读取logging.path中的路径来生成日志文件，logging.file.path从appliaction-*.yml中获取 -->
    <springProperty scope="context" name="logPath" source="logging.file.path"
                    defaultValue="/logs/springboot"/>
    <!-- 日志输出格式 -->
    <property name="log.pattern"
              value="%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{50} - %msg%n"/>
    <!-- 日志文件路径 -->
    <property name="log.path" value="${logPath}"/>

    <!-- 彩色日志 -->
    <!-- 彩色日志依赖的渲染类 -->
    <conversionRule conversionWord="clr"
                    converterClass="org.springframework.boot.logging.logback.ColorConverter"/>
    <conversionRule conversionWord="wex"
                    converterClass="org.springframework.boot.logging.logback.WhitespaceThrowableProxyConverter"/>
    <conversionRule conversionWord="wEx"
                    converterClass="org.springframework.boot.logging.logback.ExtendedWhitespaceThrowableProxyConverter"/>
    <!-- 彩色日志格式 -->
  	<!-- 变量引用格式：${变量名:-默认值} -->
    <property name="CONSOLE_LOG_PATTERN"
              value="${CONSOLE_LOG_PATTERN:-%clr(%d{yyyy-MM-dd HH:mm:ss.SSS}){faint} %clr(${LOG_LEVEL_PATTERN:-%5p}) %clr(${PID:- }){magenta} %clr(---){faint} %clr([%15.15t]){faint} %clr(%-40.40logger{39}){cyan} %clr(:){faint} %m%n${LOG_EXCEPTION_CONVERSION_WORD:-%wEx}}"/>

    <!--输出到控制台-->
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <!--此日志appender是为开发使用，只配置最底级别，控制台输出的日志级别是大于或等于此级别的日志信息-->
        <filter class="ch.qos.logback.classic.filter.ThresholdFilter">
            <level>debug</level>
        </filter>
        <encoder>
            <Pattern>${CONSOLE_LOG_PATTERN}</Pattern>
            <!-- 设置字符集 -->
            <charset>UTF-8</charset>
        </encoder>
    </appender>

    <!--输出到文件-->
    <!-- 时间滚动输出 level为 DEBUG 日志 -->
    <appender name="DEBUG_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <!-- 正在记录的日志文件的路径及文件名 -->
        <file>${log.path}/log_debug.log</file>
        <!--日志文件输出格式-->
        <encoder>
            <pattern>${log.pattern}</pattern>
            <charset>UTF-8</charset> <!-- 设置字符集 -->
        </encoder>
        <!-- 日志记录器的滚动策略，按日期，按大小记录 -->
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <!-- 日志归档 -->
            <fileNamePattern>${log.path}/debug/log-debug-%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            <timeBasedFileNamingAndTriggeringPolicy
                    class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
                <maxFileSize>100MB</maxFileSize>
            </timeBasedFileNamingAndTriggeringPolicy>
            <!--日志文件保留天数-->
            <maxHistory>30</maxHistory>
        </rollingPolicy>
        <!-- 此日志文件只记录debug级别的 -->
        <filter class="ch.qos.logback.classic.filter.LevelFilter">
            <level>debug</level>
            <onMatch>ACCEPT</onMatch>
            <onMismatch>DENY</onMismatch>
        </filter>
    </appender>

    <!-- 时间滚动输出 level为 INFO 日志 -->
    <appender name="INFO_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <!-- 正在记录的日志文件的路径及文件名 -->
        <file>${log.path}/log_info.log</file>
        <!--日志文件输出格式-->
        <encoder>
            <pattern>${log.pattern}</pattern>
            <charset>UTF-8</charset>
        </encoder>
        <!-- 日志记录器的滚动策略，按日期，按大小记录 -->
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <!-- 每天日志归档路径以及格式 -->
            <fileNamePattern>${log.path}/info/log-info-%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            <timeBasedFileNamingAndTriggeringPolicy
                    class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
                <maxFileSize>100MB</maxFileSize>
            </timeBasedFileNamingAndTriggeringPolicy>
            <!--日志文件保留天数-->
            <maxHistory>30</maxHistory>
        </rollingPolicy>
        <!-- 此日志文件只记录info级别的 -->
        <filter class="ch.qos.logback.classic.filter.LevelFilter">
            <level>info</level>
            <onMatch>ACCEPT</onMatch>
            <onMismatch>DENY</onMismatch>
        </filter>
    </appender>

    <!-- 时间滚动输出 level为 WARN 日志 -->
    <appender name="WARN_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <!-- 正在记录的日志文件的路径及文件名 -->
        <file>${log.path}/log_warn.log</file>
        <!--日志文件输出格式-->
        <encoder>
            <pattern>${log.pattern}</pattern>
            <charset>UTF-8</charset> <!-- 此处设置字符集 -->
        </encoder>
        <!-- 日志记录器的滚动策略，按日期，按大小记录 -->
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>${log.path}/warn/log-warn-%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            <timeBasedFileNamingAndTriggeringPolicy
                    class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
                <maxFileSize>100MB</maxFileSize>
            </timeBasedFileNamingAndTriggeringPolicy>
            <!--日志文件保留天数-->
            <maxHistory>30</maxHistory>
        </rollingPolicy>
        <!-- 此日志文件只记录warn级别的 -->
        <filter class="ch.qos.logback.classic.filter.LevelFilter">
            <level>warn</level>
            <onMatch>ACCEPT</onMatch>
            <onMismatch>DENY</onMismatch>
        </filter>
    </appender>


    <!-- 时间滚动输出 level为 ERROR 日志 -->
    <appender name="ERROR_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <!-- 正在记录的日志文件的路径及文件名 -->
        <file>${log.path}/log_error.log</file>
        <!--日志文件输出格式-->
        <encoder>
            <pattern>${log.pattern}</pattern>
            <charset>UTF-8</charset> <!-- 此处设置字符集 -->
        </encoder>
        <!-- 日志记录器的滚动策略，按日期，按大小记录 -->
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>${log.path}/error/log-error-%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            <timeBasedFileNamingAndTriggeringPolicy
                    class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
                <maxFileSize>100MB</maxFileSize>
            </timeBasedFileNamingAndTriggeringPolicy>
            <!--日志文件保留天数-->
            <maxHistory>30</maxHistory>
        </rollingPolicy>
        <!-- 此日志文件只记录ERROR级别的 -->
        <filter class="ch.qos.logback.classic.filter.LevelFilter">
            <level>ERROR</level>
            <onMatch>ACCEPT</onMatch>
            <onMismatch>DENY</onMismatch>
        </filter>
    </appender>

    <!--
        <logger>用来设置某一个包或者具体的某一个类的日志打印级别、以及指定<appender>。<logger>仅有一个name属性，一个可选的level和一个可选的addtivity属性。
        name:用来指定受此logger约束的某一个包或者具体的某一个类。
        level:用来设置打印级别，大小写无关：TRACE, DEBUG, INFO, WARN, ERROR, ALL 和 OFF，还有一个特俗值INHERITED或者同义词NULL，代表强制执行上级的级别。如果未设置此属性，那么当前logger将会继承上级的级别。
        addtivity:是否向上级logger传递打印信息。默认是true。
    -->
    <!--
         1、使用mybatis的时候，sql语句是debug下才会打印，而这里我们只配置了info，所以想要查看sql语句的话，有以下两种操作：
         2、第一种把<root level="info">改成<root level="DEBUG">这样就会打印sql，不过这样日志那边会出现很多其他消息
         3、第二种就是单独给dao下目录配置debug模式，这样配置sql语句会打印，其他还是正常info级别：
     -->

    <!--
        root节点是必选节点，用来指定最基础的日志输出级别，只有一个level属性
        level:用来设置打印级别，大小写无关：TRACE, DEBUG, INFO, WARN, ERROR, ALL 和 OFF，不能设置为INHERITED或者同义词NULL。默认是DEBUG可以包含零个或多个元素，标识这个appender将会添加到这个logger。
    -->

    <!--开发环境:打印控制台-->
    <springProfile name="dev">
        <root level="info">
            <appender-ref ref="CONSOLE"/>
            <appender-ref ref="INFO_FILE"/>
            <appender-ref ref="ERROR_FILE"/>
            <appender-ref ref="WARN_FILE"/>
        </root>
        <logger name="com.hqyj" level="debug" additivity="false">
            <appender-ref ref="CONSOLE"/>
        </logger>
    </springProfile>

    <!--生产环境:输出到文件-->
    <springProfile name="prod">
        <root level="info">
            <appender-ref ref="CONSOLE"/>
            <appender-ref ref="INFO_FILE"/>
            <appender-ref ref="ERROR_FILE"/>
            <appender-ref ref="WARN_FILE"/>
        </root>
        <logger name="com.hqyj" level="DEBUG" additivity="false">
            <appender-ref ref="DEBUG_FILE"/>
        </logger>
    </springProfile>

</configuration>
```

**根节点 `<configuration>` 的子节点**



#### 2.2.1 logger

用来设置某一个包或者具体的某一个类的日志打印级别、以及指定 `<appender>`。`<logger>` 仅有一个name属性，一个可选的level和一个可选的addtivity属性。

- `name` 用来指定受此 `loger` 约束的某一个包或者具体的某一个类
- `level` 用来设置打印级别，大小写无关：TRACE, DEBUG, INFO, WARN, ERROR, ALL 和 OFF，还有一个特殊值 **INHERITED** 或者同义词 **NULL** ，代表强制执行上级的级别。如果未设置此属性，那么当前 `logger` 将会继承上级的日志级别。
- `addtivity` 是否向上级 `logger` 传递打印信息。默认是true。
- appender-ref用来指定appender。

```html
<logger name="com.hqyj" level="debug" additivity="false">
    <appender-ref ref="CONSOLE"/>
</logger>
```

#### 2.2.2 appender

是 `<configuration>` 的子节点，是负责写日志的组件。该标签负责以适当的格式将日志记录事件输出到适当的输出设备。

- `name` 指定appender名称
- `class` 指定appender的全限定名

```html
<!--输出到控制台-->
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <!--此日志appender是为开发使用，只配置最底级别，控制台输出的日志级别是大于或等于此级别的日志信息-->
        <filter class="ch.qos.logback.classic.filter.ThresholdFilter">
            <level>debug</level>
        </filter>
        <encoder>
            <Pattern>${CONSOLE_LOG_PATTERN}</Pattern>
            <!-- 设置字符集 -->
            <charset>UTF-8</charset>
        </encoder>
    </appender>
```

常用的appender类型：ConsoleAppender、RollingFileAppender

ConsoleAppender：用于把日志输出到控制台。

RollingFileAppender：滚动记录文件，先将日志记录到指定文件，当符合某个条件时，将日志记录到其他文件。

**appender的子标签：**

- `encoder` 对日志进行格式化

- `rollingPolicy` 当发生滚动时，决定**RollingFileAppender** 的行为，涉及文件移动和重命名(设置滚动策略)

  `class` ：为 `rollingPolicy` 的属性，设置 日志的滚动策略，最常用的滚动策略为**TimeBasedRollingPolicy** ：它根据时间来制定滚动策略，既负责滚动也负责出发滚动。

  `rollingPolicy` 的 子节点：

  <fileNamePattern> : 为一个必要的子节点，设置日志文件的名称 。一般包含文件名及“%d”转换符，“%d”可以包含一个java.text.SimpleDateFormat指定的时间格式，如：%d{yyyy-MM}。如果直接使用 %d，默认格式是 yyyy-MM-dd。

  `<maxHistory>` : 可选节点，控制保留的归档文件的最大数量，超出数量就删除旧文件。

  `filter` :为日志过滤器。执行一个过滤器会有返回一个枚举值，即 **DENY**，**NEUTRAL**，**ACCEPT** 其中之一。

  `class` ：为 `filter` 设置指定的过滤器 ，下面列举几个常见的 过滤器

  **LevelFilter** ：级别过滤器，根据日志级别进行过滤。如果日志级别等于配置级别，过滤器会根据onMath 和 onMismatch接收或拒绝日志。

  onMatch="ACCEPT" 表示匹配该级别及以上

  onMatch="DENY" 表示不匹配该级别及以上

  onMatch="NEUTRAL" 表示该级别及以上的，由下一个filter处理，如果当前是最后一个，则表示匹配该级别及以上

  onMismatch="ACCEPT" 表示匹配该级别以下

  onMismatch="DENY" 表示不匹配该级别以下的

  onMismatch="NEUTRAL" 表示该级别及以下的，由下一个filter处理，如果当前是最后一个，则不匹配该级别以下的

#### 2.2.3 root

`root` 为根元素，只有一个level属性。`<root>` 可以包含零个或多个 `<appender-ref>` 元素。

- `level` 设置日志级别。

```xml
<root level="info">
    <appender-ref ref="CONSOLE"/>
    <appender-ref ref="INFO_FILE"/>
    <appender-ref ref="ERROR_FILE"/>
    <appender-ref ref="WARN_FILE"/>
</root>
```

#### 2.2.4 log的pattern转换符

log.pattern中转换符说明：

**c** {*length* }
**lo** {*length* }
**logger** {*length* }

输出日志的logger名，可有一个整形参数，功能是缩短logger名，设置为0表示只输入logger最右边点符号之后的字符串。

| Conversion specifier | Logger name                | Result                     |
| -------------------- | -------------------------- | -------------------------- |
| %logger              | mainPackage.sub.sample.Bar | mainPackage.sub.sample.Bar |
| %logger{0}           | mainPackage.sub.sample.Bar | Bar                        |
| %logger{5}           | mainPackage.sub.sample.Bar | m.s.s.Bar                  |
| %logger{10}          | mainPackage.sub.sample.Bar | m.s.s.Bar                  |
| %logger{15}          | mainPackage.sub.sample.Bar | m.s.sample.Bar             |
| %logger{16}          | mainPackage.sub.sample.Bar | m.sub.sample.Bar           |
| %logger{26}          | mainPackage.sub.sample.Bar | mainPackage.sub.sample.Bar |

**d** {*pattern* }
**date** {*pattern* }

输出日志的打印日志，模式语法与`java.text.SimpleDateFormat` 兼容。  

| Conversion Pattern               | Result                    |
| -------------------------------- | ------------------------- |
| %d                               | 2006-10-20 14:06:49,812   |
| %date                            | 2006-10-20 14:06:49,812   |
| %date{ISO8601}                   | 2006-10-20 14:06:49,812   |
| %date{HH:mm:ss.SSS}              | 14:06:49.812              |
| %date{dd MMM yyyy ;HH:mm:ss.SSS} | 20 oct. 2006;14:06:49.812 |

**m / msg / message**

输出应用程序提供的信息。

**n**

输出平台相关的分行符“\n”或者“\r\n”。

**p / le / level**

输出日志级别。

**t / thread**

输出产生日志的线程名。

**logback中变量引用**：

在引用一个变量时，如果该变量未定义，需要为其指定默认值，写法是：

```
${变量名:-默认值}
```

**格式修饰符：**

与转换符共同使用**，**可选的格式修饰符位于“%”和转换符之间。

**左对齐修饰符** ：符号是减号“-”；接着是可选的最小宽度 修饰符，用十进制数表示。

如果字符小于最小宽度，则左填充或右填充，默认是左填充（即右对齐），填充符为空格。如果字符大于最小宽度，字符永远不会被截断。

**最大宽度修饰符**：符号是点号"."后面加十进制数。如果字符大于最大宽度，则从前面截断。点符号“.”后面加减号“-”在加数字，表示从尾部截断。

| Format modifier | Logger name           | Result        |
| --------------- | --------------------- | ------------- |
| [%20.20logger]  | main.Name             | [  main.Name] |
| [%-20.20logger] | main.Name             | [main.Name  ] |
| [%10.10logger]  | main.foo.foo.bar.Name | [o.bar.Name]  |
| [%10.-10logger] | main.foo.foo.bar.Name | [main.foo.f]  |

**支持的颜色字符编码**

- black 黑色
- red 红色
- green 绿色
- yellow 黄色
- blue 蓝色
- magenta 洋红色
- cyan 青色
- white 白色
- gray 灰色

更多颜色可参考：https://logback.qos.ch/manual/layouts.html#coloring

## 3.slf4j应用

pom.xml文件中默认已引入slf4j相关jar包的依赖，直接使用即可。

方式一：

在类中通过LoggerFactory定义Logger对象后即可使用：

```java
@SpringBootApplication
public class SpringbootDem01Application {
    private static Logger log = LoggerFactory.getLogger("SpringbootDem01Application");

    public static void main(String[] args) {
        SpringApplication.run(SpringbootDem01Application.class, args);
        log.info("******舞台已搭建，请开始你的表演******");
    }

}
```

方式二：

在pom.xml文件中引入Lombok依赖，使用该依赖包提供的注解

```xml
<dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
        </dependency>
```

在类中使用@Slf4j注解

```java
@SpringBootApplication
@Slf4j
public class SpringbootDem01Application {

    public static void main(String[] args) {
        SpringApplication.run(SpringbootDem01Application.class, args);
        log.info("******舞台已搭建，请开始你的表演******");
    }

}
```

