## class ImportContent

```cangjie
public class ImportContent <: Node {
    public init()
}
```

父类型：

- [Node](#class-node)

### prop commas

```cangjie
public mut prop commas: Tokens
```

功能：获取或设置 [ImportContent](ast_package_classes.md#class-importcontent) 节点中的 "," 词法单元序列，只有 `importKind` 为 `ImportKind.Multi` 时非空。

类型：[Tokens](ast_package_classes.md#class-tokens)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Tokens](ast_package_classes.md#class-tokens) 不是 "," 词法单元序列时，抛出异常。

### prop identifier

```cangjie
public mut prop identifier: Token
```

功能：获取或设置 [ImportContent](ast_package_classes.md#class-importcontent) 节点中被导入的项，它可能是包中的顶层定义或声明，也可能是子包的名字。

类型：[Token](ast_package_structs.md#struct-token)

### prop importAlias

```cangjie
public mut prop importAlias: Tokens
```

功能：获取或设置 [ImportContent](ast_package_classes.md#class-importcontent) 节点中导入的定义或声明的别名词法单元序列，只有 `importKind` 为 `ImportKind.Alias` 时非空。如：`import packageName.xxx as yyy` 中的 `as yyy`。

类型：[Tokens](ast_package_classes.md#class-tokens)

### prop importKind

```cangjie
public mut prop importKind: ImportKind
```

功能：获取或设置 [ImportContent](ast_package_classes.md#class-importcontent) 节点中导入类型。

类型：[ImportKind](ast_package_enums.md#enum-importkind)

### prop items

```cangjie
public mut prop items: ArrayList<ImportContent>
```

功能：获取或设置 [ImportContent](ast_package_classes.md#class-importcontent) 节点中被导入的所有项，只有 `importKind` 为 `ImportKind.Multi` 时非空。

类型：ArrayList\<[ImportContent](ast_package_classes.md#class-importcontent)>

### prop lBrace

```cangjie
public mut prop lBrace: Token
```

功能：获取或设置 [ImportContent](ast_package_classes.md#class-importcontent) 节点中的 `{` 操作符词法单元，只有 `importKind` 为 `ImportKind.Multi` 时非空。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `{` 操作符时，抛出异常。

### prop prefixPaths

```cangjie
public mut prop prefixPaths: Tokens
```

功能：获取或设置 [ImportContent](ast_package_classes.md#class-importcontent) 节点中完整包名的前缀部分的词法单元序列，可能为空。如 `import a.b.c` 中的 `a` 和 `b`。

类型：[Tokens](ast_package_classes.md#class-tokens)

### prop prefixDots

```cangjie
public mut prop prefixDots: Tokens
```

功能：获取或设置 [ImportContent](ast_package_classes.md#class-importcontent) 节点中完整包名中用于分隔每层子包的词法单元序列，可能为空。如 `import a.b.c` 中的两个 "."。

类型：[Tokens](ast_package_classes.md#class-tokens)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Tokens](ast_package_classes.md#class-tokens) 不是 "." 词法单元序列时，抛出异常。

### prop rBrace

```cangjie
public mut prop rBrace: Token
```

功能：获取或设置 [ImportContent](ast_package_classes.md#class-importcontent) 节点中的 `}` 操作符词法单元，只有 `importKind` 为 `ImportKind.Multi` 时非空。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `}` 操作符时，抛出异常。

### init()

```cangjie
public init()
```

功能：构造一个默认的 [ImportContent](ast_package_classes.md#class-importcontent) 对象。