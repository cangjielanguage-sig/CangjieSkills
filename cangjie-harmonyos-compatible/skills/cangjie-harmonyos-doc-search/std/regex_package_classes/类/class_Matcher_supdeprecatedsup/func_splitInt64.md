### func split(Int64)

```cangjie
public func split(limit: Int64): Array<String>
```

功能：将给定的输入序列根据正则尽可能的分割成多个子序列 （最多分割成 limit 个子串）。

参数：

- limit: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 最多分割的子串个数。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 如果 limit>0，返回最多 limit 个子串；如果 limit<=0，返回最大可分割数个子串。