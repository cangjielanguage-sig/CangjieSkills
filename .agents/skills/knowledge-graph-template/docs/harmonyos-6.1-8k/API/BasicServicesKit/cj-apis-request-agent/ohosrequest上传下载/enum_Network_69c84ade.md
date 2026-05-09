## enum Network

```cangjie
public enum Network <: Equatable<Network> & ToString {
    | AnyType
    | Wifi
    | Cellular
    | ...
}
```

**功能：** 定义网络选项。

网络不满足设置条件时，未执行的任务会等待执行，执行中的任务将失败或暂停。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### AnyType

```cangjie
AnyType
```

**功能：** 表示不限网络类型。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Wifi

```cangjie
Wifi 
```

**功能：** 表示无线网络。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Cellular

```cangjie
Cellular 
```

**功能：** 表示蜂窝数据网络。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22