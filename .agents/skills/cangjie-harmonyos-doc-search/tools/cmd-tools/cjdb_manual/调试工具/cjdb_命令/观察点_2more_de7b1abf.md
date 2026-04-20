### 观察点

```text
watchpoint set variable -w read variable_name
```

`-w` 指定观察点点类型，有 `read`、`write`、`read_write` 三种类型。

`wa s v`是`watchpoint set variable`的缩写。

例：**watchpoint set variable -w read a**

```text
(cjdb) wa s v -w read a
Watchpoint created: Watchpoint 1: addr = 0x7fffddffed70 size = 8 state = enabled type = r
    declare @ 'test.cj:27'
    watchpoint spec = 'a'
    new value: 10
(cjdb)
```

只支持在基础类型设置观察点。在 `Windows` 上程序的观察点设置条件时，程序最多只会暂停一次。

### 表达式计算

`cjdb` 中使用`expression <cmd-options> -- <expr>`（`expression` 简写为`expr`）可以实现表达式求值。

- 查看字面量

例：**expr 3**

```text
(cjdb) expr 3
(Int64) $0 = 3
(cjdb)
```

- 查看变量名

例：**expr a**

```text
(cjdb) expr a
(Int64) $0 = 3
(cjdb)
```

- 查看算术表达式

例：**expr a + b**

```text
(cjdb) expr a + b
(Int64) $0 = 3
(cjdb)
```

- 查看关系表达式

例：**expr a > b**

```text
(cjdb) expr a > b
(Bool) $0 = false
(cjdb)
```

- 查看逻辑表达式

例：**expr a && b**

```text
(cjdb) expr true && false
(Bool) $0 = false
(cjdb)
```

- 查看后缀表达式

例：**expr a.b**

```text
(cjdb) expr value.member
(Int64) $0 = 1
(cjdb)
```

例：**expr a[b]**

```text
(cjdb) expr array[2]
(Int64) $0 = 3
(cjdb)
```

- 查看泛型实例化变量

例：**expr a**

```text
(cjdb) expr a
(default.A<Int32>) $0 = {
  member = 1
}
(cjdb)
```

支持的表达式计算：包含但不限于字面量、变量名、括号表达式、算术表达式、关系表达式、条件表达式、循环表达式、成员访问表达式、索引访问表达式、区间表达式、位运算表达式、泛型实例化变量等。

> **注意：**
>
> 不支持的表达式计算：带命名参数的函数调用、互操作、扩展、属性、别名、插值字符串、函数名， `Windows` 平台不支持 Float16 类型，且不支持异常抛出。