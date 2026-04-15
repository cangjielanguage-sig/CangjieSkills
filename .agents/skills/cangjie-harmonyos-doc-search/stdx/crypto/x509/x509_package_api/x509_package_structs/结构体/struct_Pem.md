## struct Pem

```cangjie
public struct Pem <: Collection<PemEntry> & ToString {
    public Pem(private let items: Array<PemEntry>)
}
```

功能：结构体 [Pem](x509_package_structs.md#struct-pem) 为条目序列，可以包含多个 [PemEntry](x509_package_structs.md#struct-pementry)。

父类型：

- Collection\<[PemEntry](#struct-pementry)>
- ToString

### prop size

```cangjie
public override prop size: Int64
```

功能：条目序列的数量。

类型：Int64

### Pem(Array\<PemEntry>)

```cangjie
public Pem(private let items: Array<PemEntry>)
```

功能：构造 [Pem](x509_package_structs.md#struct-pem) 对象。

参数：

- items: Array\<[PemEntry](x509_package_structs.md#struct-pementry)> - 多个 [PemEntry](x509_package_structs.md#struct-pementry) 对象。

### static func decode(String)

```cangjie
public static func decode(text: String): Pem
```

功能：将 PEM 文本解码为条目序列。

参数：

- text: String - PEM 字符串。

返回值：

- [Pem](x509_package_structs.md#struct-pem) - PEM 条目序列。

异常：

- [X509Exception](./x509_package_exceptions.md#class-x509exception) - 数据为空时，或解码失败抛出异常。

### func encode()

```cangjie
public func encode(): String
```

功能：返回 PEM 格式的字符串。行结束符将根据当前操作系统生成。

返回值：

- String - PEM 格式的字符串。

### func isEmpty()

```cangjie
public override func isEmpty(): Bool
```

功能：判断 PEM 文本解码为条目序列是否为空。

返回值：

- Bool - PEM 文本解码为条目序列为空返回 true；否则，返回 false。

### func iterator()

```cangjie
public override func iterator(): Iterator<PemEntry>
```

功能：生成 PEM 文本解码为条目序列的迭代器。

返回值：

- Iterator\<[PemEntry](x509_package_structs.md#struct-pementry)> - PEM 文本解码为条目序列的迭代器。

### func toString()

```cangjie
public override func toString(): String
```

功能：返回一个字符串，字符串内容是包含每个条目序列的标签。

返回值：

- String - 包含每个条目序列的标签的字符串。