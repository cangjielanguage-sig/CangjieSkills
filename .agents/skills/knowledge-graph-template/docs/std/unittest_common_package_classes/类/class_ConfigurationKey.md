## class ConfigurationKey

```cangjie
abstract sealed class ConfigurationKey <: Equatable<ConfigurationKey> & Hashable {}
```

功能：配置项的键值对象。提供判等及 hashCode 方法。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[ConfigurationKey](#class-configurationkey)>
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)

### func hashCode()

```cangjie
public override func hashCode(): Int64
```

功能：获取 hashCode 值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - hashCode 值。

### let name

```cangjie
public let name: String
```

功能：配置键值的名称。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### operator func ==(ConfigurationKey)

```cangjie
public override operator func ==(that: ConfigurationKey): Bool
```

功能：判等。

参数：

- that: [ConfigurationKey](#class-configurationkey) - 被对比的数据

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否相等。

### operator func !=(that: ConfigurationKey)

```cangjie
public override operator func !=(that: ConfigurationKey): Bool
```

功能：判不等。

参数：

- that: [ConfigurationKey](#class-configurationkey) - 被对比的数据

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否不相等。

### extend ConfigurationKey

```cangjie
extend ConfigurationKey {
    static func create<T>(name: String): ConfigurationKey 
}
```

#### static func create\<T>(String)

功能：创建 [ConfigurationKey](#class-configurationkey)。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 配置键值的名称。

返回值：

- [ConfigurationKey](#class-configurationkey) - 创建的配置键值。