### operator func !=(Token)

```cangjie
public operator func !=(r: Token): Bool
```

功能：判断两个 [Token](ast_package_structs.md#struct-token) 对象是否不相等。

参数：

- r: [Token](ast_package_structs.md#struct-token) - 待比较的另一个 [Token](ast_package_structs.md#struct-token) 对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 两个词法单元的种类 `ID`、值、位置不相同时，返回 true。

### operator func +(Token)

```cangjie
public operator func +(r: Token): Tokens
```

功能：使用当前 [Token](ast_package_structs.md#struct-token) 添加一个 [Token](ast_package_structs.md#struct-token) 以获取新的 [Tokens](ast_package_classes.md#class-tokens)。

参数：

- r: [Token](ast_package_structs.md#struct-token) - 待添加的另一个 [Token](ast_package_structs.md#struct-token) 对象。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 添加新的 [Tokens](ast_package_classes.md#class-tokens) 后的词法单元集合。

### operator func +(Tokens)

```cangjie
public operator func +(r: Tokens): Tokens
```

功能：使用当前 [Token](ast_package_structs.md#struct-token) 添加一个 [Tokens](ast_package_classes.md#class-tokens) 以获取新的 [Tokens](ast_package_classes.md#class-tokens)。

参数：

- r: [Tokens](ast_package_classes.md#class-tokens) - 待添加的另一组 [Token](ast_package_structs.md#struct-token) 对象集合。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 添加新的 [Tokens](ast_package_classes.md#class-tokens) 后的词法单元集合。

### operator func ==(Token)

```cangjie
public operator func ==(r: Token): Bool
```

功能：判断两个 [Token](ast_package_structs.md#struct-token) 对象是否相等。

参数：

- r: [Token](ast_package_structs.md#struct-token) - 待比较的另一个 [Token](ast_package_structs.md#struct-token) 对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 两个词法单元的种类 `ID`、值、位置相同时，返回 true。