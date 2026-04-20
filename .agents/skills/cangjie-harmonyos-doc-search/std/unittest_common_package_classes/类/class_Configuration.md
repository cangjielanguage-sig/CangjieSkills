## class Configuration

```cangjie
public class Configuration <: ToString {
    public init()
}
```

功能：存储 `@Configure` 宏生成的 `unittest` 配置数据的对象。[Configuration](#class-configuration) 与 [HashMap](../../collection/collection_package_api/collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 类似，但它的键是 [KeyFor](./unittest_common_package_interfaces.md#interface-keyfor) 类型，值为任何给定类型。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

### init()

```cangjie
public init()
```

功能：构造一个空的 Configuration 实例。

### func clone()

```cangjie
public func clone(): Configuration
```

功能：拷贝一份 Configuration 对象。

返回值：

- [Configuration](#class-configuration) - 拷贝的对象。

### func get\<T>(KeyFor\<T>)

```cangjie
public func get<T>(key: KeyFor<T>): ?T
```

功能：获取 key 对应的值。

T 为 泛型参数，用于在对象中查找对应类型的值。

参数：

- key: [KeyFor](./unittest_common_package_interfaces.md#interface-keyfor) - 配置项的键值。

返回值：

- ?T - 未找到时返回 None，找到对应类型及名称的值时返回 Some\<T>(v) 。

### func getByName\<T>(String)

```cangjie
public func getByName<T>(name: String): ?T
```

功能：获取 key 对应的值。

T 为 泛型参数，用于在对象中查找对应类型的值。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 键名称。

返回值：

- ?T - 未找到时返回 None，找到对应类型及名称的值时返回 Some\<T>(v) 。

### func remove\<T>(KeyFor\<T>)

```cangjie
public func remove<T>(key: KeyFor<T>): ?T
```

功能：删除对应键名称和类型的值。

参数：

- key: [KeyFor](./unittest_common_package_interfaces.md#interface-keyfor) - 配置项的键值。

返回值：

- ?T - 当存在该值时返回该值，当不存在时返回 None。

### func removeByName\<T>(String)

```cangjie
public func removeByName<T>(name: String): ?T
```

功能：删除对应键名称和类型的值。

参数：

- key: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 键名称。

返回值：

- ?T - 当存在该值时返回该值，当不存在时返回 None。

### func set\<T>(KeyFor\<T>, T)

```cangjie
public func set<T>(key: KeyFor<T>, value: T)
```

功能：给对应键名称和类型设置值。

参数：

- key: [KeyFor](./unittest_common_package_interfaces.md#interface-keyfor) - 配置项的键值。
- value: T - 键值。

### func setByName\<T>(String, T)

```cangjie
public func setByName<T>(name: String, value: T): Unit
```

功能：给对应键名称和类型设置值。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 键名称。
- value: T - 键值。

### func toString()

```cangjie
public func toString(): String
```

功能：该对象的字符化对象，当内部对象未实现 [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring) 接口时，输出 '\<not printable>' 。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 字符串。

### static func merge(Configuration, Configuration)

```cangjie
public static func merge(parent: Configuration, child: Configuration): Configuration
```

功能：合并 child 到 parent 配置中。其中如有同名键值 child 覆盖 parent 。

参数：

- parent: [Configuration](#class-configuration) - 需要合并的配置
- child: [Configuration](#class-configuration) - 需要合并的配置

返回值：

- [Configuration](#class-configuration) - 合并完成的配置