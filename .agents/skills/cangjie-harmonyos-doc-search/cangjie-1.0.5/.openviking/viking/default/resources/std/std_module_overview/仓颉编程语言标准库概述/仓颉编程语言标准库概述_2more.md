# 仓颉编程语言标准库概述

仓颉编程语言标准库（std）是安装仓颉 SDK 时默认自带的库。标准库预先定义了一组函数、类、结构体等，旨在提供常用的功能和工具，以便开发者能够更快速、更高效地编写程序。

仓颉标准库有其三项特点和追求：

- 使用方便：标准库随编译器、工具链一起发布，不需要用户另外下载，开箱即用。
- 功能通用：标准库提供了开发者最常使用的一些库能力，旨在为开发者解决大部分基础问题。
- 质量标杆：标准库追求在性能、代码风格等方面为其他仓颉库树立范例和标杆。

## 使用指导

在仓颉编程语言中，标准库包含了若干包（package），而包是编译的最小单元。每个包可以单独输出 AST（Abstract Syntax Trees，抽象语法树）文件、静态库文件、动态库文件等产物。包可以定义子包，从而构成树形结构。没有父包的包称为 root 包，root 包及其子包（包括子包的子包）构成的整棵树称为模块（module）。模块的名称与 root 包相同，是开发者发布的最小单元。

包的导入规则如下：

- 可以导入某个包中的一个顶层声明或定义，语法如下：

    ```cangjie
    import fullPackageName.itemName
    ```

    其中 fullPackageName 为完整路径包名，itemName 为声明的名字，例如：

    ```cangjie
    import std.collection.ArrayList
    ```

- 如果要导入的多个 itemName 同属于一个 fullPackageName，可以使用：

    ```cangjie
    import fullPackageName.{itemName[, itemName]*}
    ```

    例如：

    ```cangjie
    import std.collection.{ArrayList, HashMap}
    ```

- 还可以将 fullPackageName 包中所有 public 修饰的顶层声明或定义全部导入，语法如下：

    ```cangjie
    import fullPackageName.*
    ```

    例如：

    ```cangjie
    import std.collection.*
    ```