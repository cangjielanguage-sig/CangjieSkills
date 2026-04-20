### func contains(IPAddress)

```cangjie
public func contains(rhs: IPAddress): Bool
```

功能：此 [IPPrefix](net_package_classes.md#class-ipprefix) 地址是否包含指定的 [IPAddress](net_package_classes.md#class-ipaddress) 地址。

参数：

- rhs: [IPAddress](net_package_classes.md#class-ipaddress) - 指定的 [IPAddress](net_package_classes.md#class-ipaddress) 地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示包含指定的 [IPAddress](net_package_classes.md#class-ipaddress) 地址，false 表示不包含。

### func contains(IPPrefix)

```cangjie
public func contains(rhs: IPPrefix): Bool
```

功能：此 [IPPrefix](net_package_classes.md#class-ipprefix) 地址是否包含指定的 [IPPrefix](net_package_classes.md#class-ipprefix) 地址。

参数：

- rhs: [IPPrefix](net_package_classes.md#class-ipprefix) - 指定的 [IPPrefix](net_package_classes.md#class-ipprefix) 地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示包含指定的 [IPPrefix](net_package_classes.md#class-ipprefix) 地址，false 表示不包含。

### func hostmask()

```cangjie
public open func hostmask(): IPAddress
```

功能：返回此 [IPPrefix](net_package_classes.md#class-ipprefix) 地址的主机网络掩码地址。

返回值：

- [IPAddress](net_package_classes.md#class-ipaddress) - 此 [IPPrefix](net_package_classes.md#class-ipprefix) 地址的主机网络掩码地址。

### func masked()

```cangjie
public open func masked(): IPPrefix
```

功能：返回此 [IPPrefix](net_package_classes.md#class-ipprefix) 地址根据前缀长度进行掩码后的 [IPPrefix](net_package_classes.md#class-ipprefix) 地址，比如 `192.168.12.34/16` 返回 `192.168.0.0/16`；`fc00::1:2:3:4/16` 返回 `fc00::/16`。

返回值：

- [IPPrefix](net_package_classes.md#class-ipprefix) - 此 [IPPrefix](net_package_classes.md#class-ipprefix) 地址根据前缀长度进行掩码后的 [IPPrefix](net_package_classes.md#class-ipprefix) 地址。

### func netmask()

```cangjie
public open func netmask(): IPAddress
```

功能：返回此 [IPPrefix](net_package_classes.md#class-ipprefix) 地址的网络掩码地址。

返回值：

- [IPAddress](net_package_classes.md#class-ipaddress) - 此 [IPPrefix](net_package_classes.md#class-ipprefix) 地址的网络掩码地址。

### func network()

```cangjie
public open func network(): IPAddress
```

功能：返回此 [IPPrefix](net_package_classes.md#class-ipprefix) 地址的网络地址。

返回值：

- [IPAddress](net_package_classes.md#class-ipaddress) - 此 [IPPrefix](net_package_classes.md#class-ipprefix) 地址的网络地址。

### func overlaps(IPPrefix)

```cangjie
public func overlaps(rhs: IPPrefix): Bool
```

功能：此 [IPPrefix](net_package_classes.md#class-ipprefix) 地址是不是和指定的 [IPPrefix](net_package_classes.md#class-ipprefix) 地址有重叠。

参数：

- rhs: [IPPrefix](net_package_classes.md#class-ipprefix) - 指定的 [IPPrefix](net_package_classes.md#class-ipprefix) 地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示和指定的 [IPPrefix](net_package_classes.md#class-ipprefix) 地址有重叠，false 表示没有重叠。