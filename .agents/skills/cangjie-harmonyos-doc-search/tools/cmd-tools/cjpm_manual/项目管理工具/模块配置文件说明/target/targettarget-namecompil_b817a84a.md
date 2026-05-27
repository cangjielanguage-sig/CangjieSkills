#### "target.target-name.compile-macros-for-target"

该字段用于配置宏包的交叉编译方式，有如下三种情况：

方式一：宏包在交叉编译时默认仅编译本地平台的产物，不编译目标平台的产物，对该模块内的所有宏包生效

```text
[target.目标平台]
  compile-macros-for-target = ""
```

方式二：在交叉编译时同时编译本地平台和目标平台的产物，对该模块内的所有宏包生效

```text
[target.目标平台]
  compile-macros-for-target = "all" # 配置项为字符串形式，可选值必须为 all
```

方式三：指定该模块内的某些宏包在交叉编译时同时编译本地平台和目标平台的产物，其它未指定的宏包采取方式一的默认模式

```text
[target.目标平台]
  compile-macros-for-target = ["pkg1", "pkg2"] # 配置项为字符串数字形式，可选值是宏包名
```