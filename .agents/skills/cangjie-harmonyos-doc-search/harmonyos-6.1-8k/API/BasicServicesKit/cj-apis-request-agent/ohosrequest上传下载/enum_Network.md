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

**父类型：**

- Equatable\<Network>
- ToString

### AnyType

```cangjie
AnyType
```

**功能：** 表示不限网络类型。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Cellular

```cangjie
Cellular
```

**功能：** 表示蜂窝数据网络。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Wifi

```cangjie
Wifi
```

**功能：** 表示无线网络。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### func !=(Network)

```cangjie
public operator func !=(other: Network): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名 | 类型                     | 必填 | 默认值 | 说明     |
| :----- | :----------------------- | :--- | :----- | :------- |
| other  | [Network](#enum-network) | 是   | -      | 另一个网络选项。|

**返回值：**

| 类型 | 说明                                      |
| :--- | :---------------------------------------- |
| Bool | 两个枚举值不相等返回true，否则返回false。 |

### func ==(Network)

```cangjie
public operator func ==(other: Network): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名 | 类型                     | 必填 | 默认值 | 说明     |
| :----- | :----------------------- | :--- | :----- | :------- |
| other  | [Network](#enum-network) | 是   | -      | 另一个网络选项。 |

**返回值：**

| 类型 | 说明                                    |
| :--- | :-------------------------------------- |
| Bool | 两个枚举值相等返回true，否则返回false。 |

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**返回值：**

| 类型   | 说明                       |
| :----- | :------------------------- |
| String | 获取当前枚举的字符串表示。 |