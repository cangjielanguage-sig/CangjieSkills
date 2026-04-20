### operator func ==(Path)

```cangjie
public operator func ==(that: Path): Bool
```

功能：判断 [Path](fs_package_structs.md#struct-path) 是否相等。

判等时将对 [Path](fs_package_structs.md#struct-path) 进行规范化，如果规范化后的字符串相等，则认为两个 [Path](fs_package_structs.md#struct-path) 实例相等。规范化规则详见函数 [normalize](./fs_package_structs.md#func-normalize)。

参数：

- that: [Path](fs_package_structs.md#struct-path) - 另一个 [Path](fs_package_structs.md#struct-path)。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - true，是同一路径；false，不是同一路径。