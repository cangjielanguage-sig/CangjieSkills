### operator func \[](K)

```cangjie
public operator func [](key: K): V
```

功能：运算符重载 get 方法，如果键存在，返回键对应的值。

参数：

- key: K - 传递值进行判断。

返回值：

- V - 与键对应的值。

异常：

- [NoneValueException](../../core/core_package_api/core_package_exceptions.md#class-nonevalueexception) - 如果该 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 不存在该键，抛此异常。

### operator func \[](K, V)

```cangjie
public operator func [](key: K, value!: V): Unit
```

功能：运算符重载 add 方法，如果键存在，新 value 覆盖旧 value，如果键不存在，添加此键值对。

参数：

- key: K - 传递值进行判断。
- value!: V - 传递要设置的值。