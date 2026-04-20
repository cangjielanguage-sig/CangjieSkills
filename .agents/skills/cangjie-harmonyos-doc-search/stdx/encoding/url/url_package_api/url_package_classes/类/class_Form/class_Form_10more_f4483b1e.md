## class Form

```cangjie
public class Form {
    public init()
    public init(queryComponent: String)
}
```

功能：[Form](url_package_classes.md#class-form) 以 key-value 键值对形式存储 http 请求的表单信息，通常为请求 [URL](url_package_classes.md#class-url) 中的 query 部分。

同一个 key 可以对应多个 value，value 以数组形式存储。`&` 符号分隔多个键值对；`=` 分隔的左侧作为 key 值，右侧作为 value 值（没有 `=` 或者 value 为空，均是允许的）。使用示例见 [Form 的构造使用](../url_samples/form.md)。

### init()

```cangjie
public init()
```

功能：构造一个默认的 [Form](url_package_classes.md#class-form) 实例。

### init(String)

```cangjie
public init(queryComponent: String)
```

功能：根据 [URL](url_package_classes.md#class-url) 编码的查询字符串，即 [URL](url_package_classes.md#class-url) 实例的 query 部分构造 [Form](url_package_classes.md#class-form) 实例。

解析 [URL](url_package_classes.md#class-url) 编码的查询字符串，得到若干键值对，并将其添加到新构造的 [Form](url_package_classes.md#class-form) 实例中。

参数：

- queryComponent: String - [URL](url_package_classes.md#class-url) 的 query 组件部分的字符串，但是不包括组件前面的 `?` 符号。

异常：

- IllegalArgumentException - 当[URL](url_package_classes.md#class-url) 字符串中包含不符合 utf8 编码规则的字节时，抛出异常。
- [UrlSyntaxException](url_package_exceptions.md#class-urlsyntaxexception) - 当 [URL](url_package_classes.md#class-url) 字符串中包含非法转义字符时，抛出异常。

### func add(String, String)

```cangjie
public func add(key: String, value: String): Unit
```

功能：新增 key-value 映射，如果 key 已存在，则将 value 添加到原来 value 数组的最后面。

参数：

- key: String - 指定键，可以是新增的。
- value: String - 将该值添加到指定键对应的值数组中。

### func clone()

```cangjie
public func clone(): Form
```

功能：克隆 [Form](url_package_classes.md#class-form)。

返回值：

- [Form](url_package_classes.md#class-form) - 克隆得到的新 [Form](url_package_classes.md#class-form) 实例。

### func get(String)

```cangjie
public func get(key: String): Option<String>
```

功能：根据 key 获取第一个对应的 value 值。

举例：

- 当 query 组件部分是 `a=b` 时，`form.get("a")`获得 `Some(b)`。
- 当 query 组件部分是 `a=` 时，`form.get("a")`获得 `Some()`。
- 当 query 组件部分是 `a` 时，`form.get("a")`获得 `Some()`。
- 当 query 组件部分是 `a` 时，`form.get("c")`获得 `None`。

参数：

- key: String - 指定键。

返回值：

- Option\<String> - 根据指定键获取的第一个值，用 Option\<String> 类型表示。

### func getAll(String)

```cangjie
public func getAll(key: String): ArrayList<String>
```

功能：根据指定的键（key）获取该键（key）对应的所有 value 值。

参数：

- key: String - 用户指定的键（key），用于获取对应的 value 值。

返回值：

- ArrayList\<String> - 根据指定键（key）获取的全部 value 值对应的数组。当指定键（key）不存在时，返回空数组。

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

功能：判断 [Form](url_package_classes.md#class-form) 是否为空。

返回值：

- Bool - 如果为空，则返回 true；否则，返回 false。

### func remove(String)

```cangjie
public func remove(key: String): Unit
```

功能：删除 key 及其对应 value。

参数：

- key: String - 需要删除的键。

### func set(String, String)

```cangjie
public func set(key: String, value: String): Unit
```

功能：重置指定 key 对应的 value。

参数：

- key: String - 指定键。
- value: String - 将指定键的值设置为 value。