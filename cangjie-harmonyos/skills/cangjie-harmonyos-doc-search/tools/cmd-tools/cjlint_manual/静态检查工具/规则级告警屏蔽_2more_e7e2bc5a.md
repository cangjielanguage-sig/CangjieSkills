## 规则级告警屏蔽

可执行文件`cjlint`同目录下的`config`配置目录中包含`cjlint_rule_list.json`和`exclude_lists.json`两个配置文件。`cjlint_rule_list.json`为规则列表配置文件，用于决定执行哪些规则检查。`exclude_lists.json`为告警屏蔽配置文件，用于屏蔽特定规则的告警。

例：若开发者只想检查如下 5 条规则，则`cjlint_rule_list.json`配置文件中只添加要检查的 5 条规则。

```json
{
    "RuleList": [
        "G.FMT.01",
        "G.ENU.01",
        "G.EXP.03",
        "G.OTH.01",
        "G.OTH.02"
    ]
}
```

例：若开发者想要屏蔽某一条规则的某一条告警，可以在`exclude_lists.json`配置文件中添加屏蔽信息。

> **注意：**
>
> `path`不必填写绝对路径，但必须有`xxx.cj`格式，为模糊匹配。`line`为告警行号，为精确匹配。`colum`为告警列号，可选择性填写进行列号精确匹配。

```json
{
    "G.OTH.01" : [
        {"path":"xxx/example.cj", "line":"42"},
        {"path":"xxx/example.cj", "line":"42", "colum": "2"},
        {"path":"example.cj", "line":"42", "colum": "2"}
    ]
}
```

## 源代码注释告警屏蔽

**特殊注释 BNF**

```text
<content of cjlint-ignore comment> ::=  "cjlint-ignore"  [-start] <ignore-rule>{...} [description] | cjlint-ignore  <-end> [description]
<ignore-rule> ::="!"<rule-name>
<rule-name> ::= <letters>
```

> **注意：**
>
> - 特殊注释的 `cjlint-ignore` 与选项 `-start` 和 `-end` 以及屏蔽的规则需要写在同一行上，否则无法进行告警屏蔽。描述信息可以写在不同行。
> - 单行屏蔽，屏蔽规则与屏蔽规则间需要用空格隔开，`cjlint` 会将特殊注释所在行的对应规则告警进行屏蔽。
> - 多行屏蔽，`cjlint` 会以含有 `-start` 的特殊注释为起始行，以含有 `-end` 的特殊注释为结束行，将其间对应的规则进行屏蔽。含有 `-end` 的特殊注释会与其上方最近的含有 `-start` 的特殊注释相匹配。

**单行屏蔽正确示例 1**，屏蔽 G.FUN.02 告警

<!-- compile -->

```cangjie
func foo(a: Int64, b: Int64, c: Int64, d: Int64) { /* cjlint-ignore !G.FUN.02 */
    return a + b + c
}
```

**单行屏蔽正确示例 2**，屏蔽 G.FUN.02 告警

<!-- compile -->

```cangjie
func foo(a: Int64, b: Int64, c: Int64, d: Int64) { // cjlint-ignore !G.FUN.02 description
    return a + b + c
}
```

**多行屏蔽正确示例 1**，屏蔽 G.FUN.02 告警

<!-- compile -->

```cangjie
/*cjlint-ignore -start !G.FUN.02 description */
func foo(a: Int64, b: Int64, c: Int64, d: Int64) {
    return a + b + c
}
/* cjlint-ignore -end description */
```

**多行屏蔽正确示例 2**，屏蔽 G.FUN.02 告警

<!-- compile -->

```cangjie
// cjlint-ignore -start !G.FUN.02 description
func foo(a: Int64, b: Int64, c: Int64, d: Int64) {
    return a + b + c
}
// cjlint-ignore -end description
```

**多行屏蔽正确示例 3**，屏蔽 G.FUN.02 告警

<!-- compile -->

```cangjie
/**
 *  cjlint-ignore -start !G.FUN.02 description
 */
func foo(a: Int64, b: Int64, c: Int64, d: Int64) {
    return a + b + c
}
// cjlint-ignore -end description
```

**单行屏蔽错误示例 1**，屏蔽 G.FUN.02 告警

<!-- compile -->

```cangjie
func foo(a: Int64, b: Int64, c: Int64, d: Int64) { /*cjlint-ignore !G.FUN.02!G.FUN.01*/
    return a + b + c                               // ERROR: 规则间没用空格隔开，屏蔽告警失败
}
```

**单行屏蔽错误示例 2**，屏蔽 G.FUN.02 告警

<!-- compile -->

```cangjie
func foo(a: Int64, b: Int64, c: Int64, d: Int64) { /*cjlint-ignore !G.FUN.02description*/
    return a + b + c                               // ERROR: 规则与描述信息没用空格隔开，屏蔽告警失败
}
```

**多行屏蔽错误示例 1**，屏蔽 G.FUN.02 告警

<!-- compile -->

```cangjie
/* cjlint-ignore -start
 * !G.FUN.02 description */
func foo(a: Int64, b: Int64, c: Int64, d: Int64) {
    return a + b + c
}
/* cjlint-ignore -end description */
// ERROR: 屏蔽规则没与 'cjlint-ignore' 在同一行，屏蔽告警失败
```