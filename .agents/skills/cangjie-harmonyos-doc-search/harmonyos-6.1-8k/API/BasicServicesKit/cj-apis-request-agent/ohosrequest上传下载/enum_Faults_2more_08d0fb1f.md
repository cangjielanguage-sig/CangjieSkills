## enum Faults

```cangjie
public enum Faults <: ToString {
    | Others
    | Disconnected
    | Timeout
    | Protocol
    | Fsio
    | ...
}
```

**功能：** 定义任务失败的原因。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**父类型：**

- ToString

### Disconnected

```cangjie
Disconnected
```

**功能：** 表示网络断开连接。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Fsio

```cangjie
Fsio
```

**功能：** 表示文件系统io错误，例如打开/查找/读取/写入/关闭。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Others

```cangjie
Others
```

**功能：** 表示其他故障。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Protocol

```cangjie
Protocol
```

**功能：** 表示协议错误，例如：服务器内部错误（500）、无法处理的数据区间（416）等。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Timeout

```cangjie
Timeout
```

**功能：** 表示任务超时。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**返回值：**

| 类型   | 说明                   |
| :----- | :--------------------- |
| String | 当前枚举的字符串表示。 |

## enum FormItemValue

```cangjie
public enum FormItemValue {
    | StringItem(String)
    | FileItem(FileSpec)
    | FileItemArray(Array<FileSpec>)
    | ...
}
```

**功能：** 表单项的文件信息枚举类型。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### FileItem(FileSpec)

```cangjie
FileItem(FileSpec)
```

**功能：** 表示文件信息。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### FileItemArray(Array\<FileSpec>)

```cangjie
FileItemArray(Array<FileSpec>)
```

**功能：** 表示多个文件信息。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### StringItem(String)

```cangjie
StringItem(String)
```

**功能：** 表示文件路径。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22