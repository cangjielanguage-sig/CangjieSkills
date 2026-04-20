## class GenericTypeInfo

```cangjie
public class GenericTypeInfo <: TypeInfo & Equatable<GenericTypeInfo> {}
```

功能：描述泛型类型信息。

父类型：

- [TypeInfo](./reflect_package_classes.md#class-typeinfo)
- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[GenericTypeInfo](./reflect_package_classes.md#class-generictypeinfo)>

### operator func ==(GenericTypeInfo)

```cangjie
public operator func ==(that: GenericTypeInfo): Bool
```

功能：判断该泛型类型信息与给定的另一个泛型类型信息是否相等。

参数：

- that: [GenericTypeInfo](reflect_package_classes.md#class-generictypeinfo) - 被比较相等性的另一个泛型类型信息。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该泛型类型信息与 `that` 相等则返回 `true`，否则返回 `false`。