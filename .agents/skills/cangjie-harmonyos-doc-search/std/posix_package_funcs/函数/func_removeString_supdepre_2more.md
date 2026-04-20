## func remove(String) <sup>(deprecated)</sup>

```cangjie
public func remove(path: String): Int32
```

功能：删除文件或目录。

- 对于文件，[remove](posix_package_funcs.md#func-removestring-deprecated)() 等同于 [unlink](posix_package_funcs.md#func-unlinkstring-deprecated)()。
- 对于目录，[remove](posix_package_funcs.md#func-removestring-deprecated)() 等同于 rmdir()。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 成功返回 `0`，错误返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `path` 包含空字符时，抛出异常。

## func rename(String, String) <sup>(deprecated)</sup>

```cangjie
public func rename(oldName: String, newName: String): Int32
```

功能：重命名文件，如果需要将会移动文件所在目录。文件的任何其他硬链接不受影响。旧路径打开的文件描述符也不受影响。

各种限制将决定重命名操作是否成功，具体场景如下：

- 如果 `newName` 已经存在，它将被原子替换，这样另一个尝试访问 `newName` 的进程就不会发现它丢失，但是可能会有一个窗口，其中旧路径和新路径都引用要重命名的文件。
- 如果旧路径和新路径是引用同一文件的现有硬链接，则重命名不做任何操作，并返回成功状态。
- 如果 `newName` 存在，但操作因某种原因失败，则重命名保证保留 `newName` 的实例。
- `oldName` 可以指定目录。在这种情况下，`newName` 必须不存在，或者它必须指定空目录。
- 如果旧路径引用符号链接，则链接将重命名；如果新路径引用符号链接，则链接将被覆盖。

> **注意：**
>
> 未来版本即将废弃。

参数：

- oldName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件名(含路径)。
- newName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件名(含路径)。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 成功返回 `0`，错误返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `oldName` 或 `newName` 包含空字符时，抛出异常。