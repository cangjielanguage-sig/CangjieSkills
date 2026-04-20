## interface PrettyPrintable

```cangjie
public interface PrettyPrintable {
    func pprint(to: PrettyPrinter): PrettyPrinter
}
```

功能：类型实现该接口表示可以较好地进行颜色及缩进格式的打印。

### func pprint(PrettyPrinter)

```cangjie
func pprint(to: PrettyPrinter): PrettyPrinter
```

功能：将类型值打印到指定的打印器中。

参数：

- to: [PrettyPrinter](./unittest_common_package_classes.md#class-prettyprinter) - 打印器。

返回值：

- [PrettyPrinter](./unittest_common_package_classes.md#class-prettyprinter) - 打印器。

### extend\<T> Array\<T> <: PrettyPrintable where T <: PrettyPrintable

```cangjie
extend<T> Array<T> <: PrettyPrintable where T <: PrettyPrintable
```

功能：对 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> 扩展实现 [PrettyPrintable](#interface-prettyprintable)。

#### func pprint(PrettyPrinter)

```cangjie
public func pprint(to: PrettyPrinter): PrettyPrinter
```

功能：将类型值打印到指定的打印器中。

参数：

- to: [PrettyPrinter](./unittest_common_package_classes.md#class-prettyprinter) - 打印器。

返回值：

- [PrettyPrinter](./unittest_common_package_classes.md#class-prettyprinter) - 打印器。

### extend\<T> ArrayList\<T> <: PrettyPrintable where T <: PrettyPrintable

```cangjie
extend<T> ArrayList<T>  <: PrettyPrintable where T <: PrettyPrintable
```

功能：对 [ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<T> 扩展实现 [PrettyPrintable](#interface-prettyprintable)。

#### func pprint(PrettyPrinter)

```cangjie
public func pprint(to: PrettyPrinter): PrettyPrinter
```

功能：将类型值打印到指定的打印器中。

参数：

- to: [PrettyPrinter](./unittest_common_package_classes.md#class-prettyprinter) - 打印器。

返回值：

- [PrettyPrinter](./unittest_common_package_classes.md#class-prettyprinter) - 打印器。

## interface KeyFor

```cangjie
public interface KeyFor<T> {
    prop name: String
}
```

功能：[Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) 中配置型的键的类型。

可以通过 [@UnitestOption](./../../unittest_testmacro/unittest_testmacro_package_api/unittest_testmacro_package_macros.md#unittestoption-宏) 定义自定义配置项键值。内置的 unittest 配置项可以根据[命名规则](../../unittest_testmacro/unittest_testmacro_package_api/unittest_testmacro_package_macros.md#customassertion-宏)获取。例如，可以通过 `KeyRandomSeed.randomSeed` 键从 [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) 中提取 `randomSeed` 。

### prop name

```cangjie
prop name: String
```

功能：[Configuration](./unittest_common_package_classes.md#class-configuration) 中使用的键名称的字符串表示形式。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)。