## class HttpHeaders

```cangjie
public class HttpHeaders <: Iterable<(String, Collection<String>)>
```

功能：此类用于表示 Http 报文中的 header 和 trailer，定义了相关增、删、改、查操作。

> **说明：**
>
> - header 和 trailer 为键值映射集，由若干 field-line 组成，每一个 field-line 包含一个键 (field -name) 和若干值 (field-value)。
> - field-name 由 token 字符组成，不区分大小写，在该类中将转为小写保存。
> - field-value 由 vchar，SP 和 HTAB 组成，vchar 表示可见的 US-ASCII 字符，不得包含前后空格，不得为空值。
> - 详见 [rfc 9110](https://www.rfc-editor.org/rfc/rfc9110.html#name-fields)。

示例：

```text
Example-Field: Foo, Bar
key: Example-Field, value: Foo, Bar
field-name = token
token = 1*tchar
tchar = "!" / "#" / "$" / "%" / "&" / "'" / "*"
/ "+" / "-" / "." / "^" / "_" / "`" / "|" / "~"
/ DIGIT / ALPHA
; any VCHAR, except delimiters
```

父类型：

- Iterable\<(String, Collection\<String>)>

### func add(String, String)

```cangjie
public func add(name: String, value: String): Unit
```

功能：添加指定键值对。如果 name 已经存在，将在其对应的值列表中添加 value；如果 name 不存在，则添加 name 字段及其值 value。

参数：

- name: String - [HttpHeaders](http_package_classes.md#class-httpheaders) 的字段名称。
- value: String - [HttpHeaders](http_package_classes.md#class-httpheaders) 的字段值。

异常：

- [HttpException](http_package_exceptions.md#class-httpexception) - 如果传入的 name/value 包含不合法元素，将抛出此异常。

### func del(String)

```cangjie
public func del(name: String): Unit
```

功能：删除指定 name 对应的键值对。

参数：

- name: String - 删除的字段名称。

### func get(String)

```cangjie
public func get(name: String): Collection<String>
```

功能：获取指定 name 对应的 value 值。

参数：

- name: String - 字段名称，不区分大小写。

返回值：

- Collection\<String> - name 对应的 value 集合，如果指定 name 不存在，返回空集合。

### func getFirst(String)

```cangjie
public func getFirst(name: String): ?String
```

功能：获取指定 name 对应的第一个 value 值。

参数：

- name: String - 字段名称，不区分大小写。

返回值：

- ?String - name 对应的第一个 value 值，如果指定 name 不存在，返回 None。

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

功能：判断当前实例是否为空，即没有任何键值对。

返回值：

- Bool - 如果当前实例为空，返回 true，否则返回 false。

### func iterator()

```cangjie
public func iterator(): Iterator<(String, Collection<String>)>
```

功能：获取迭代器，可用于遍历所有键值对。

返回值：

- Iterator\<(String, Collection\<String>)> - 该键值集的迭代器。

### func set(String, String)

```cangjie
public func set(name: String, value: String): Unit
```

功能：设置指定键值对。如果 name 已经存在，传入的 value 将会覆盖之前的值。

参数：

- name: String - [HttpHeaders](http_package_classes.md#class-httpheaders) 的字段名称。
- value: String - [HttpHeaders](http_package_classes.md#class-httpheaders) 的字段值。

异常：

- [HttpException](http_package_exceptions.md#class-httpexception) - 如果传入的 name/values 包含不合法元素，将抛出此异常。