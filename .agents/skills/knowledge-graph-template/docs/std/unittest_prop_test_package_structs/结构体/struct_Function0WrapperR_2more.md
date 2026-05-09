## struct Function0Wrapper\<R>

```cangjie
public struct Function0Wrapper<R> {
    public Function0Wrapper(public let function: () -> R)
}
```

功能：将闭包封装为结构体。

### Function0Wrapper(() -> R)

```cangjie
public Function0Wrapper(public let function: () -> R)
```

功能：Function0Wrapper 构造器。

参数：

- function: () -> R - 被封装的闭包。

### let function

```cangjie
public let function: () -> R
```

功能：函数对象自身。

类型：()->R

### operator func ()()

```cangjie
public operator func () (): R
```

功能：调用操作符函数。将闭包转换为结构体的调用操作符函数。

返回值：

- R - 同闭包的返回值。

### extend\<R> Function0Wrapper\<R> <: Arbitrary\<Function0Wrapper\<R>> where R <: Arbitrary\<R>

```cangjie
extend<R> Function0Wrapper<R> <: Arbitrary<Function0Wrapper<R>> where R <: Arbitrary<R>
```

功能：为 [Function0Wrapper](#struct-function0wrapperr) 扩展 [Arbitrary](./unittest_prop_test_package_interfaces.md#interface-arbitraryt) 实现。

父类型：

- [Arbitrary](unittest_prop_test_package_interfaces.md#interface-arbitraryt)\<[Function0Wrapper](#struct-function0wrapperr)\<R>>

#### static func arbitrary(RandomSource)

```cangjie
public static func arbitrary(random: RandomSource): Generator<Function0Wrapper<R>>
```

功能：获取生成 [Function0Wrapper](#struct-function0wrapperr)\<R> 类型随机值生成器。

返回值：

- [Generator](../unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<[Function0Wrapper](../unittest_prop_test_package_api/unittest_prop_test_package_structs.md#struct-function0wrapperr)\<R>> - 生成器。

## struct KeyRandom

```cangjie
public struct KeyRandom <: KeyFor<RandomSource> {}
```

功能：用于在 [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) 创建键值。

父类型：

- [KeyFor](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-keyfor)<[RandomSource](./unittest_prop_test_package_interfaces.md#interface-randomsource)>

### prop random

```cangjie
public static prop random: KeyRandom
```

功能：配置项的键值。

### prop name

```cangjie
public prop name: String
```

功能：配置项的键值的名称。