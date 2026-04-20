## struct SocketType

```cangjie
public struct SocketType <: Equatable<SocketType> & ToString & Hashable {
    public static let DATAGRAM: SocketType = SocketType(2)
    public static let RAW: SocketType = SocketType(3)
    public static let SEQPACKET: SocketType = SocketType(5)
    public static let STREAM: SocketType = SocketType(1)
    public init(`type`: Int32)
}
```

功能：提供了常用的套接字类型，以及通过指定 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 值来构建套接字类型的功能。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[SocketType](#struct-sockettype)>
- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)

### static let DATAGRAM

```cangjie
public static let DATAGRAM: SocketType = SocketType(2)
```

功能：数据报套接字类型。

类型：[SocketType](net_package_structs.md#struct-sockettype)

### static let RAW

```cangjie
public static let RAW: SocketType = SocketType(3)
```

功能：原始套接字类型。

类型：[SocketType](net_package_structs.md#struct-sockettype)

### static let SEQPACKET

```cangjie
public static let SEQPACKET: SocketType = SocketType(5)
```

功能：有序数据包套接字类型。

类型：[SocketType](net_package_structs.md#struct-sockettype)

### static let STREAM

```cangjie
public static let STREAM: SocketType = SocketType(1)
```

功能：流式套接字类型。

类型：[SocketType](net_package_structs.md#struct-sockettype)

### init(Int32)

```cangjie
public init(`type`: Int32)
```

功能：通过指定套接字类型值创建套接字类型。

参数：

- \`type`: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 套接字类型值。

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：返回当前 [SocketType](net_package_structs.md#struct-sockettype) 实例的哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 当前 [SocketType](net_package_structs.md#struct-sockettype) 实例的哈希值。

### func toString()

```cangjie
public func toString(): String
```

功能：返回当前 [SocketType](net_package_structs.md#struct-sockettype) 实例的字符串表示。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 当前 [SocketType](net_package_structs.md#struct-sockettype) 实例的字符串表示。

### operator func !=(SocketType)

```cangjie
public operator func !=(r: SocketType): Bool
```

功能：判断两个 [SocketType](net_package_structs.md#struct-sockettype) 实例是否不等。

参数：

- r: [SocketType](net_package_structs.md#struct-sockettype) - 参与比较的 [SocketType](net_package_structs.md#struct-sockettype) 实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当二者代表的 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 值不等时，返回 `true`；否则，返回 `false`。

### operator func ==(SocketType)

```cangjie
public operator func ==(r: SocketType): Bool
```

功能：判断两个 [SocketType](net_package_structs.md#struct-sockettype) 实例是否相等。

参数：

- r: [SocketType](net_package_structs.md#struct-sockettype) - 参与比较的 [SocketType](net_package_structs.md#struct-sockettype) 实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当二者代表的 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 值相等时，返回 `true`；否则，返回 `false`。