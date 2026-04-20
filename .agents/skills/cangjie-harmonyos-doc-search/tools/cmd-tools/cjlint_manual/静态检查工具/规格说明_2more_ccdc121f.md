## 规格说明

- G.CON.02 在异常可能出现的情况下，保证释放已持有的锁。

    lock() 函数和 unlock() 函数赋值给变量，赋值后的变量再去加解锁的场景，该规则检查不覆盖。

- G.OTH.03 暂不支持宏检查。
- 只有当宏包在正确的路径下时，`cjlint`才能支持宏检查。

    例：a.cj 为宏包源码，其正确路径应为 xxx/src/a/a.cj。

- `cjlint`只有在宏被调用时才能对其进行检查，且无法对宏包中的冗余代码进行检查。

## 支持语法禁用检查

1. `cjlint` 可以通过将 G.SYN.01 添加至 `cjlint_rule_list.json` 以启用禁用语法的检查。如果使用了禁用的语法元素，`cjlint` 将会报错。

2. 当前`cjlint`所支持检查的禁止使用语法如表中所示:

   | 禁用语法     | 关键词          | 说明                                             |
   | ------------ | --------------- | ------------------------------------------------ |
   | 导入包       | Import          | 不允许随意导入包                                 |
   | let 变量     | Let             | 只用 var 变量，不引入不可写变量的概念            |
   | 创建线程     | Spawn           | 不允许创建线程                                   |
   | 线程同步     | Synchronized    | 防止死锁                                         |
   | 主函数       | Main            | 禁止提供入口主函数                               |
   | 定义宏       | MacroQuote      | 禁止定义宏（但允许使用宏）                       |
   | 跨语言       | Foreign         | 禁止跨语言混合编程                               |
   | while 循环   | While           | 防止复杂循环和死循环                             |
   | 扩展         | Extend          | 禁止使用扩展语法                                 |
   | 类型别名     | Type            | 禁止自行定义类型别名                             |
   | 操作符重载   | Operator        | 禁止重载操作符                                   |
   | 全局变量     | GlobalVariable  | 禁止声明和使用全局变量，防止副作用和内存泄漏     |
   | 定义枚举     | Enum            | 禁用 Enum，避免复杂代码                          |
   | 定义类       | Class           | 禁用 Class，避免复杂代码                         |
   | 定义接口     | Interface       | 禁用 Interface，避免复杂代码                     |
   | 定义结构     | Struct          | 禁用 Struct，避免复杂代码                        |
   | 定义泛型     | Generic         | 禁用 Generic，避免复杂代码                       |
   | 条件编译     | When            | 禁止平台相关代码                                 |
   | 模式匹配     | Match           | 函数式编程范式，开发者不易掌握                   |
   | 捕获异常     | TryCatch        | 避免自行处理异常，易导致错误被忽略               |
   | 高阶函数     | HigherOrderFunc | 函数类型的参数或返回值, 避免复杂代码             |
   | 其他基础类型 | PrimitiveType   | 不应使用 Int64、float64、bool 之外的其他基础类型 |
   | 其他容器类型 | ContainerType   | 应使用 List，Map，Set                            |

3. 通过将上述表格中的关键字添加到 `structural_rule_G_SYN_01.json` 中启用对应语法的禁用检查。举例：禁用导入包

```json
{
  "SyntaxKeyword": [
    "Import"
  ]
}
```