### func setSocketOptionIntNative(Int32, Int32, IntNative)

```cangjie
public func setSocketOptionIntNative(
    level: Int32,
    option: Int32,
    value: IntNative
): Unit
```

功能：设置指定的套接字参数。

参数：

- level: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 层级，例如 `SOL_SOCKET`。
- option: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 参数，例如 `SO_KEEPALIVE`。
- value: [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 参数值。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `setsockopt` 返回失败时，抛出异常。

### func toString()

```cangjie
public override func toString(): String
```

功能：返回当前 [TcpServerSocket](net_package_classes.md#class-tcpserversocket) 的状态信息。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 包含当前 [TcpServerSocket](net_package_classes.md#class-tcpserversocket) 状态信息的字符串。