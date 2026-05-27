## class AdvertisingDisableParams

```cangjie
public class AdvertisingDisableParams {
    public AdvertisingDisableParams(
        public var advertisingId: UInt32)
}
```

**功能：** 描述临时停止广播设置的参数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### var advertisingId

```cangjie
public var advertisingId: UInt32
```

**功能：** 表示广播ID标识。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### AdvertisingDisableParams(UInt32)

```cangjie
public AdvertisingDisableParams(
    public var advertisingId: UInt32)
```

**功能：** AdvertisingDisableParams 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|advertisingId|UInt32|是|表示当前广播的ID标识。|

## class AdvertisingEnableParams

```cangjie
public class AdvertisingEnableParams {
    public AdvertisingEnableParams(
        public var advertisingId: UInt32,
        public var duration!: UInt16 = 0
    )
}
```

**功能：** 描述临时启动广播设置的参数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### var advertisingId

```cangjie
public var advertisingId: UInt32
```

**功能：** 表示广播ID标识。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### var duration

```cangjie
public var duration: UInt16 = 0
```

**功能：** 表示发送广播持续的时间。单位为10ms，有效范围为1(10ms)到65535(655350ms)，如果未指定此参数或者将其设置为0，则会连续发送广播。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** UInt16

**读写能力：** 可读写

**起始版本：** 19

### AdvertisingEnableParams(UInt32, UInt16)

```cangjie
public AdvertisingEnableParams(
    public var advertisingId: UInt32,
    public var duration!: UInt16 = 0
)
```

**功能：** AdvertisingEnableParams 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|advertisingId|UInt32|是|-|表示当前广播的ID标识。|
|duration|UInt16|否|0| **命名参数。** 表示发送广播持续的时间。单位为10ms，有效范围为1(10ms)到65535(655350ms)，如果未指定此参数或者将其设置为0，则会连续发送广播。|