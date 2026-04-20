## func isNearExpansion\<CT, D>(CT, CT, D, String)

```cangjie
public func isNearExpansion<CT, D>(
    l: CT,
    r: CT,
    delta!: D,
    cmpType!: String
): Bool where CT <: NearEquatable<CT, D> & Comparable<CT>
```

功能：判断两个参数是否近似相等。在 [PowerAssert](../../unittest_testmacro/unittest_testmacro_package_api/unittest_testmacro_package_macros.md#powerassert-宏) 宏展开时使用。用户不应使用。

参数：

- l: CT - 待判断近似相等的参数。
- r: CT - 待判断近似相等的参数。
- delta!: D - 待判断近似相等时使用的 delta。
- cmpType!: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 判断的类型。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否近似相等。

## func isNearExpansion\<CT, D>(CT, CT, D, String, Bool)

```cangjie
public func isNearExpansion<CT, D>(
    l: CT,
    r: CT,
    delta!: D,
    cmpType!: String,
    overloadHack!: Bool = true
): Bool where CT <: NearEquatable<CT, D>
```

功能：判断两个参数是否近似相等。在 [PowerAssert](../../unittest_testmacro/unittest_testmacro_package_api/unittest_testmacro_package_macros.md#powerassert-宏) 宏展开时使用。用户不应使用。

参数：

- l: CT - 待判断近似相等的参数。
- r: CT - 待判断近似相等的参数。
- delta!: D - 待判断近似相等时使用的 delta。
- cmpType!: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 判断的类型。
- overloadHack!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 为使能函数重载使用新增的参数，默认值为 true 。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否近似相等。