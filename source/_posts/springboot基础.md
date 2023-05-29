---
title: springboot基础
tags:
  - 基础
  - springboot基础
categories:
  - springbootboot
keywords: "springboot，基础"
cover: https://p5.qhimg.com/bdr/__85/t0187a94f89728d19ef.jpg
toc: True
abbrlink: 20220829
---

# springboot基础

## 1.springboot介绍

 Spring Boot是由spring的Pivotal团队提供的全新框架，其设计目的是用来简化新Spring应用的初始搭建以及开发过程。该框架使用了特定的方式来进行配置，从而使开发人员不再需要定义样板化的配置。用我的话来理解，就是spring boot其实不是什么新的框架，它默认配置了很多框架的使用方式，就像maven整合了所有的jar包，spring boot整合了所有的框架。

平时如果我们需要搭建一个spring web项目的时候需要怎么做呢？

1）配置web.xml，加载spring和spring mvc

2）配置数据库连接、配置spring事务

3）配置加载配置文件的读取，开启注解

4）配置日志文件

…

配置完成之后部署tomcat 调试

…

但是如果使用spring boot呢？

很简单，我仅仅只需要非常少的几个配置就可以迅速方便的搭建起来一套web项目或者是构建一个微服务

Spring Boot 具有以下特点：

**1 内嵌 Servlet 容器**

   Spring Boot 使用嵌入式的 Servlet 容器（例如 Tomcat、Jetty 或者 Undertow 等），应用无需打成 WAR 包 。

**2 提供 starter 简化 Maven 配置**

   Spring Boot 提供了一系列的“starter”项目对象模型（POMS）来简化 Maven 配置。

**3 提供了大量的自动配置**

   Spring Boot 提供了大量的默认自动配置，来简化项目的开发，开发人员也通过配置文件修改默认配置。

**4 自带应用监控**

   Spring Boot 可以对正在运行的项目提供监控。

**5 无代码生成和 xml 配置**

   Spring Boot 不需要任何 xml 配置即可实现 Spring 的所有配置

## 2.spring boot项目创建

搭建一个springboot 项目步骤如下：

### 2.1  新建maven项目

通过idea创建新项目（https://start.spring.io/）




### 2.2 启动程序

程序启动后，结果如下图说明启动成功


## 3.pom文件配置

### 3.1 properties

可以做自定义配置，比如配置maven编译时指定的字符集：

```xml
<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
```

指定maven编译时指定的jdk版本：

```xml
<maven.compiler.source>1.8</maven.compiler.source>
<maven.compiler.target>1.8</maven.compiler.target>
```

也可以在build标签中配置，效果等同于以上配置：

```xml
<plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                    <encoding>UTF-8</encoding>
                </configuration>
            </plugin>
```

还可以自定义依赖包的版本号标签，在添加依赖包时使用版本号标签：

```xml
<fastjson.version>1.2.83</fastjson.version>
```

```xml
<dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>fastjson</artifactId>
            <version>${fastjson.version}</version>
        </dependency>
```



## 4.springboot配置文件

Spring Boot 提供了大量的自动配置，极大地简化了spring 应用的开发过程，当用户创建了一个 Spring Boot 项目后，即使不进行任何配置，该项目也能顺利的运行起来。当然，用户也可以根据自身的需要使用配置文件修改 Spring Boot 的默认设置。

SpringBoot 默认使用以下 2 种全局的配置文件，其文件名是固定的。

- application.properties
- application.yml

其中，application.yml 是一种使用 YAML 语言编写的文件，它与 application.properties 一样，可以在 Spring Boot 启动时被自动读取，修改 Spring Boot 自动配置的默认值。

.properties 文件我们都熟知了，这里主要介绍下.yml 文件的语法以及使用

### 4.1 YAML配置

**YAML 简介**

YAML 全称 YAML Ain't Markup Language，它是一种以数据为中心的标记语言，比 XML 和 JSON 更适合作为配置文件。

想要使用 YAML 作为属性配置文件（以 .yml 结尾）

下面是一个简单的 application.yml 属性配置文件。

```yml
server:
   port: 8081
```

**YAML 语法**

YAML 的语法如下：

- 使用缩进表示层级关系。
- 缩进时不允许使用 Tab 键，只允许使用空格。
- 缩进的空格数不重要，但同级元素必须左侧对齐，一般缩进两个空格。
- 大小写敏感。

### 4.2 多环境YAML配置

在resources目录下创建application-dev.yml和application-prod.yml文件，分别表示开发环境和生产环境。文件名的前缀需要以appliaction-开头。

在application-dev.yml中配置端口号：

```yaml
server:
  port: 8081
```

在application-prod.yml中配置端口号：

```yaml
server:
  port: 8082
```

在application.yml中指定哪个配置文件生效：

```yaml
spring:
  profiles:
    active: dev
```

此时指定为dev环境，即开发环境生效。如需要使用生产环境的配置，则将spring.profiles.active指定为prod即可

也可以通过获取pom文件中的配置项来指定多环境配置文件：

在pom.xml文件中添加profiles：

```html
<profiles>
        <profile>
            <id>dev</id>
            <properties>
                <profileActive>dev</profileActive>
            </properties>
            <activation>
              	<!--默认为dev环境打包方式-->
                <activeByDefault>true</activeByDefault>
            </activation>
        </profile>
        <profile>
            <id>prod</id>
            <properties>
                <profileActive>prod</profileActive>
            </properties>
        </profile>
    </profiles>
```

在profile中指定dev环境为默认生效的环境配置。

在application.yml文件中修改：

```yaml
spring:
  profiles:
    active: @profileActive@
```

通过profileActive动态获取生效的配置环境。

## 5.springboot启动注解

### 5.1 SpringBootApplication 注解

@SpringBootApplication是一个复合注解，包括元注解和@ComponentScan，和@SpringBootConfiguration，@EnableAutoConfiguration。

**元注解**

@Target、@Retention、@Documented、@Inherited

**@Target**：用于设定注解范围，即注解可以用在什么地方

```java
public enum ElementType {
    /** Class, interface (including annotation type), or enum declaration */
    TYPE,

    /** Field declaration (includes enum constants) */
    FIELD,

    /** Method declaration */
    METHOD,

    /** Formal parameter declaration */
    PARAMETER,

    /** Constructor declaration */
    CONSTRUCTOR,

    /** Local variable declaration */
    LOCAL_VARIABLE,

    /** Annotation type declaration */
    ANNOTATION_TYPE,

    /** Package declaration */
    PACKAGE,

    /**
     * Type parameter declaration
     *
     * @since 1.8
     */
    TYPE_PARAMETER,

    /**
     * Use of a type
     *
     * @since 1.8
     */
    TYPE_USE
}
```

**@Retention**：定义了被它注解了的注解可以保留多久，我们点击它的枚举类型看看

```java
public enum RetentionPolicy {
    /**
     * Annotations are to be discarded by the compiler.
     */
    SOURCE,

    /**
     * Annotations are to be recorded in the class file by the compiler
     * but need not be retained by the VM at run time.  This is the default
     * behavior.
     */
    CLASS,

    /**
     * Annotations are to be recorded in the class file by the compiler and
     * retained by the VM at run time, so they may be read reflectively.
     *
     * @see java.lang.reflect.AnnotatedElement
     */
    RUNTIME
}
```

```
source：注解只保留在源文件，当Java文件编译成class文件的时候，注解被遗弃；被编译器忽略

class：注解被保留到class文件，但jvm加载class文件时候被遗弃，这是默认的生命周期

runtime：注解不仅被保存到class文件中，jvm加载class文件之后，仍然存在

生命周期：runtime>class>source
```

**@Documented**：表明这个注解应该被 javadoc工具记录. 默认情况下,javadoc是不包括注解的. 但如果声明注解时指定了 @Documented,则它会被 javadoc 之类的工具处理, 所以注解类型信息也会被包括在生成的文档中，是一个标记注解，没有成员。
**@Inherited**：如果一个类用上了@Inherited修饰的注解，那么其子类也会继承这个注解。

**@SpringBootConfiguration**：SpringBootConfiguration与Spring中的@Configuation的作用基本一致，只不过@SpringBootConfiguration是springboot的注解，而@Configuration是spring的注解。

```java
@Target({ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Configuration
@Indexed
public @interface SpringBootConfiguration {
    @AliasFor(
        annotation = Configuration.class
    )
    boolean proxyBeanMethods() default true;
}
```

其中：

@Configuration等价于`<Beans></Beans>`

@Indexed是Spring 5.0版本新加入的功能，在很多应用中，随着应用变得越来越大，就会出现启动变得非常慢的问题，可以通过@Indexed来提高启动效率。它可以为Spring的**模式注解**添加索引，以提升应用启动性能。

**模式注解**：

| Spring注解       | 场景说明       |
| -------------- | ---------- |
| @Repository    | 数据仓库模式注解   |
| @Component     | 通用组件模式注解   |
| @Service       | 服务模式注解     |
| @Controller    | Web控制器模式注解 |
| @Configuration | 配置类模式注解    |

添加依赖：spring5.0版本以下不支持

```xml
<dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context-indexer</artifactId>
        </dependency>
```

项目编译打包时，会在自动生成META-INF/spring.components文件，文件包含被@Indexed注释的类的模式解析结果。当Spring应用上下文进行组件扫描时，META-INF/spring.components会被org.springframework.context.index.CandidateComponentsIndexLoader读取并加载，转换为CandidateComponentsIndex对象，此时组件扫描会读取CandidateComponentsIndex，而不进行实际扫描，从而提高组件扫描效率，减少应用启动时间。

**@EnableAutoConfiguration**：自动扫描装配，扫描加载项目以外的bean，即pom文件中依赖的jar中的bean。

```java
@Target({ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
@AutoConfigurationPackage
@Import({AutoConfigurationImportSelector.class})
public @interface EnableAutoConfiguration {
    String ENABLED_OVERRIDE_PROPERTY = "spring.boot.enableautoconfiguration";

    Class<?>[] exclude() default {};

    String[] excludeName() default {};
}
```

其中：

**@AutoConfigurationPackage**：自动扫描包，打开看具体注解内容

```
@Target({ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
@Import({Registrar.class})
public @interface AutoConfigurationPackage {
    String[] basePackages() default {};

    Class<?>[] basePackageClasses() default {};
}
```

**@Import**：用于导入配置类或者一些需要前置加载的类，你就当作Import 包.类

**Registrar**：

```java
static class Registrar implements ImportBeanDefinitionRegistrar, DeterminableImports {
        Registrar() {
        }

        public void registerBeanDefinitions(AnnotationMetadata metadata, BeanDefinitionRegistry registry) {
            AutoConfigurationPackages.register(registry, (String[])(new AutoConfigurationPackages.PackageImports(metadata)).getPackageNames().toArray(new String[0]));
        }

        public Set<Object> determineImports(AnnotationMetadata metadata) {
            return Collections.singleton(new AutoConfigurationPackages.PackageImports(metadata));
        }
    }
```

在registerBeanDefinitions方法中，register(register,新建一个PackageImports匿名对象，将metadata这个对象形参填入，然后使用getPackageNames方法填入数组)

其实这就是扫描主配置类同级目录以及子包，然后记录下来，并将相应的组件导入到springboot创建管理的容器中。

**AutoConfigurationImportSelector**：该方法的含义是扫描所有类路径下的META-INF/spring.factories文件.映射为一个map.取出EnableAutoConfiguration对应的数据以及其他的bean存在容器中。

spring.factories在spring-boot依赖包中。

```java
protected List<String> getCandidateConfigurations(AnnotationMetadata metadata, AnnotationAttributes attributes) {
        List<String> configurations = new ArrayList(SpringFactoriesLoader.loadFactoryNames(this.getSpringFactoriesLoaderFactoryClass(), this.getBeanClassLoader()));
        ImportCandidates.load(AutoConfiguration.class, this.getBeanClassLoader()).forEach(configurations::add);
        Assert.notEmpty(configurations, "No auto configuration classes found in META-INF/spring.factories nor in META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports. If you are using a custom packaging, make sure that file is correct.");
        return configurations;
    }

    protected Class<?> getSpringFactoriesLoaderFactoryClass() {
        return EnableAutoConfiguration.class;
    }
```

**@ComponentScan**：用于类或接口上主要是指定扫描路径，spring会把指定路径下带有指定注解的类注册到IOC容器中。

```java
@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.TYPE})
@Documented
@Repeatable(ComponentScans.class)
public @interface ComponentScan {
    @AliasFor("basePackages")
    String[] value() default {};

    @AliasFor("value")
    String[] basePackages() default {};

    Class<?>[] basePackageClasses() default {};

    Class<? extends BeanNameGenerator> nameGenerator() default BeanNameGenerator.class;

    Class<? extends ScopeMetadataResolver> scopeResolver() default AnnotationScopeMetadataResolver.class;

    ScopedProxyMode scopedProxy() default ScopedProxyMode.DEFAULT;

    String resourcePattern() default "**/*.class";

    boolean useDefaultFilters() default true;

    ComponentScan.Filter[] includeFilters() default {};

    ComponentScan.Filter[] excludeFilters() default {};

    boolean lazyInit() default false;

    @Retention(RetentionPolicy.RUNTIME)
    @Target({})
    public @interface Filter {
        FilterType type() default FilterType.ANNOTATION;

        @AliasFor("classes")
        Class<?>[] value() default {};

        @AliasFor("value")
        Class<?>[] classes() default {};

        String[] pattern() default {};
    }
}
```

其中：

basePackages、value：指定扫描路径，如果为空则以@ComponentScan注解的类所在的包为基本的扫描路径。

由于@ComponentScan注解只能扫描spring-boot项目包内的bean并注册到spring容器中，因此需要@EnableAutoConfiguration，注解来注册项目包外的bean。而spring.factories文件，则是用来记录项目包外需要注册的bean类名。