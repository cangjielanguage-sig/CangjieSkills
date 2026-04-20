### PemEntry(String, Array\<(String, String)>, ?DerBlob)

```cangjie
public PemEntry(
    public let label: String,
    public let headers: Array<(String, String)>,
    public let body: ?DerBlob
)
```

功能：构造 [PemEntry](x509_package_structs.md#struct-pementry) 对象。

参数：

- label: String - 标签。
- headers: Array\<(String, String)> - 条目头。
- body: ?[DerBlob](x509_package_structs.md#struct-derblob) - 二进制内容。

### let body

```cangjie
public let body: ?DerBlob
```

功能：[PemEntry](x509_package_structs.md#struct-pementry) 实例的二进制内容。

类型：?[DerBlob](x509_package_structs.md#struct-derblob)

### let headers

```cangjie
public let headers: Array<(String, String)>
```

功能：[PemEntry](x509_package_structs.md#struct-pementry) 实例的条目头。

类型：Array\<(String, String)>

### let label

```cangjie
public let label: String
```

功能：[PemEntry](x509_package_structs.md#struct-pementry) 实例的标签。

类型：String

### init(String, DerBlob)

```cangjie
public init(label: String, body: DerBlob)
```

功能：构造 [PemEntry](x509_package_structs.md#struct-pementry) 对象。

参数：

- label: String - 标签
- body: [DerBlob](x509_package_structs.md#struct-derblob) - 二进制内容

### func encode()

```cangjie
public func encode(): String
```

功能：返回 PEM 格式的字符串。行结束符将根据当前操作系统生成。

返回值：

- String - PEM 格式的字符串。

### func header(String)

```cangjie
public func header(name: String): Iterator<String>
```

功能：通过条目头名称，找到对应条目内容。

参数：

- name: String - 条目头名称。

返回值：

- Iterator\<String> - 条目头名称对应内容的迭代器。

### func toString()

```cangjie
public override func toString(): String
```

功能：返回 PEM 对象的标签和二进制内容的长度。

返回值：

- String - PEM 对象的标签和二进制内容的长度。