### const SOL_SOCKET <sup>(deprecated)</sup>

```cangjie
public static const SOL_SOCKET: Int32
```

功能：常数，用于将套接字选项的 `level` 层级设为 `SOL_SOCKET`。不同系统下的值分别为：

- macOS: 0xFFFF
- Windows: 0xFFFF
- 其他情况：1

> **注意：**
>
> 未来版本即将废弃不再使用，使用 [OptionLevel.SOCKET](#static-const-socket) 替代。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### const TCP_NODELAY

```cangjie
public static const TCP_NODELAY: Int32 = 0x0001
```

功能：常数，用于将套接字选项的 `optname` 设为 `TCP_NODELAY`。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### const TCP_QUICKACK

```cangjie
public static const TCP_QUICKACK: Int32
```

功能：常数，用于将套接字选项的 `optname` 设为 `TCP_QUICKACK`。不同系统下的值分别为：

- macOS: 0xFFFF
- Windows: 0xFFFF
- 其他情况：0x000C

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)