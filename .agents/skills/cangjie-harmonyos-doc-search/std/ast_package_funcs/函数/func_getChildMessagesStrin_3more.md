## func getChildMessages(String)

```cangjie
public func getChildMessages(children:String): ArrayList<MacroMessage>
```

功能：获取特定内层宏发送的信息。

> **注意：**
>
> 该函数只能作为函数被直接调用，不能作为赋值给变量，不能作为实参或返回值使用。

参数：

- children: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待接收信息的内层宏名称。

返回值：

- [ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[MacroMessage](ast_package_classes.md#class-macromessage)> - 返回一组 [MacroMessage](ast_package_classes.md#class-macromessage) 的对象。

## func getTokenKind(UInt16)

```cangjie
public func getTokenKind(no: UInt16): TokenKind
```

功能：将词法单元种类序号转化为 [TokenKind](ast_package_enums.md#enum-tokenkind)。

参数：

- no: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 需要转换的序号。

返回值：

- [TokenKind](ast_package_enums.md#enum-tokenkind) - 词法单元种类序号对应的 [TokenKind](ast_package_enums.md#enum-tokenkind)。

> **注意：**
>
> 当前 [SINGLE_QUOTED_STRING_LITERAL](ast_package_enums.md#single_quoted_string_literal) 和 [STRING_LITERAL](ast_package_enums.md#string_literal) 共用序号 147，输入序号 147 只能获得 [STRING_LITERAL](ast_package_enums.md#string_literal)，其他 [TokenKind](ast_package_enums.md#enum-tokenkind) 无共用序号情况。

## func insideParentContext(String)

```cangjie
public func insideParentContext(parentMacroName: String): Bool
```

功能：检查当前宏调用是否在特定的宏调用内，返回一个布尔值。

> **注意：**
>
> - 在嵌套宏场景下，内层宏也可以通过发送键/值对的方式与外层宏通信。当内层宏执行时，通过调用标准库函数 [setItem](ast_package_funcs.md#func-setitemstring-bool) 向外层宏发送信息；随后，当外层宏执行时，调用标准库函数 [getChildMessages](ast_package_funcs.md#func-getchildmessagesstring) 接收每一个内层宏发送的信息（一组键/值对映射）。
> - 该函数只能作为函数被直接调用，不能作为赋值给变量，不能作为实参或返回值使用。

参数：

- parentMacroName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待检查的外层宏调用的名字。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 若当前宏嵌套在特定的宏调用内，返回 true。