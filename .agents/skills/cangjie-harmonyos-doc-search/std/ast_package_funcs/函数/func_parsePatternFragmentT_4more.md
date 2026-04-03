## func parsePatternFragment(Tokens, Int64)

```cangjie
public func parsePatternFragment(input: Tokens, startFrom !: Int64 = 0): (Pattern, Int64)
```

功能：用于解析一组词法单元，获取一个 [Pattern](ast_package_classes.md#class-pattern) 类型的节点和继续解析节点的索引。

参数：

- input: [Tokens](ast_package_classes.md#class-tokens) - 待解析源码的词法单元。
- startFrom!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 起始位置。

返回值：

- ([Pattern](ast_package_classes.md#class-pattern), [Int64](../../core/core_package_api/core_package_intrinsics.md#int64)) - 语法树节点，继续解析的位置。

异常：

- [ParseASTException](ast_package_exceptions.md#class-parseastexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [Pattern](ast_package_classes.md#class-pattern) 节点时，抛出异常，异常中包含报错提示信息。

## func parseProgram(Tokens)

```cangjie
public func parseProgram(input: Tokens): Program
```

功能：用于解析单个仓颉文件的源码，获取一个 [Program](ast_package_classes.md#class-program) 类型的节点。

> **注意：**
>
> 仓颉宏展开后的代码不允许出现包的声明和包导入语句。使用该函数时，若输入的源码中包含包声明或包导入语句，输出的 [Program](ast_package_classes.md#class-program) 节点中也会包含（在 [packageHeader](ast_package_classes.md#prop-packageheader) 和 [importLists](ast_package_classes.md#prop-importlists) 属性中），因此不能在宏函数中直接将该节点返回为 [Tokens](ast_package_classes.md#class-tokens)。

参数：

- input: [Tokens](ast_package_classes.md#class-tokens) - 待解析源码的词法单元。

返回值：

- [Program](ast_package_classes.md#class-program) - 一个 [Program](ast_package_classes.md#class-program) 类型的节点。

异常：

- [ParseASTException](ast_package_exceptions.md#class-parseastexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [Program](ast_package_classes.md#class-program) 节点时，抛出异常，异常中包含报错提示信息。

## func parseType(Tokens)

```cangjie
public func parseType(input: Tokens): TypeNode
```

功能：用于解析一组词法单元，获取一个 [TypeNode](ast_package_classes.md#class-typenode) 类型的节点。

参数：

- input: [Tokens](ast_package_classes.md#class-tokens) - 待解析源码的词法单元。

返回值：

- [TypeNode](ast_package_classes.md#class-typenode) - 一个 [TypeNode](ast_package_classes.md#class-typenode) 类型的节点。

异常：

- [ParseASTException](ast_package_exceptions.md#class-parseastexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [TypeNode](ast_package_classes.md#class-typenode) 节点时，抛出异常。

## func parseTypeFragment(Tokens, Int64)

```cangjie
public func parseTypeFragment(input: Tokens, startFrom !: Int64 = 0): (TypeNode, Int64)
```

功能：用于解析一组词法单元，获取一个 [TypeNode](ast_package_classes.md#class-typenode) 类型的节点和继续解析节点的索引。

参数：

- input: [Tokens](ast_package_classes.md#class-tokens) - 待解析源码的词法单元。
- startFrom!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 起始位置。

返回值：

- ([TypeNode](ast_package_classes.md#class-typenode), [Int64](../../core/core_package_api/core_package_intrinsics.md#int64)) - 语法树节点，继续解析的位置。

异常：

- [ParseASTException](ast_package_exceptions.md#class-parseastexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [TypeNode](ast_package_classes.md#class-typenode) 节点时，抛出异常。