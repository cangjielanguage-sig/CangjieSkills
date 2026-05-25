## enum Network

```cangjie
public enum Network <: ToString {
    | DATA_ROAMING_STATUS
    | HTTP_PROXY_CFG
    | NETWORK_PREFERENCE_USAGE
    | ...
}
```

**功能：** 提供设置网络信息的数据项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**父类型：**

- ToString

### DATA_ROAMING_STATUS

```cangjie
DATA_ROAMING_STATUS
```

**功能：** 是否启用数据漫游。值为true，表示启用数据漫游；值为false，表示不启用数据漫游。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### HTTP_PROXY_CFG

```cangjie
HTTP_PROXY_CFG
```

**功能：** 全局HTTP代理的主机名和端口号。主机名和端口号由冒号':'分隔。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### NETWORK_PREFERENCE_USAGE

```cangjie
NETWORK_PREFERENCE_USAGE
```

**功能：** 要使用的网络的用户首选项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### func toString()

```cangjie
public override func toString(): String
```

**功能：** 返回设置网络信息的数据项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**返回值：**

| 类型  | 说明  |
| :------ | :------ |
| String | 设置网络信息的数据项。 |

## enum Phone

```cangjie
public enum Phone <: ToString {
    | RTT_CALLING_STATUS
    | ...
}
```

**功能：** 提供设置来电和去电接听方式的数据项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**父类型：**

- ToString

### RTT_CALLING_STATUS

```cangjie
RTT_CALLING_STATUS
```

**功能：** 是否启用实时文本(RTT)呼叫。启用，来电和去电在设备和运营商支持时作为RTT呼叫应答。值为1，表示启用RTT 呼叫；值为0，表示不启用RTT呼叫。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### func toString()

```cangjie
public override func toString(): String
```

**功能：** 返回设置来电和去电接听方式的数据项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**返回值：**

| 类型  | 说明  |
| :------ | :------ |
| String | 设置来电和去电接听方式的数据项。 |