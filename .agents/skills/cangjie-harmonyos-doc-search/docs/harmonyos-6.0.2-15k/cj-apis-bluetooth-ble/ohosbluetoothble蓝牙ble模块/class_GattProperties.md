## class GattProperties

```cangjie
public class GattProperties {
    public GattProperties(
        let write!: Bool = true,
        let writeNoResponse!: Bool = true,
        let read!: Bool = true,
        let notify!: Bool = false,
        let indicate!: Bool = false
    )
}
```

**功能：** 描述gatt characteristic的属性。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### GattProperties(Bool, Bool, Bool, Bool, Bool)

```cangjie
public GattProperties(
    let write!: Bool = true,
    let writeNoResponse!: Bool = true,
    let read!: Bool = true,
    let notify!: Bool = false,
    let indicate!: Bool = false
)
```

**功能：** GattProperties构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|write|Bool|否|true| **命名参数。** 表示该特征支持写操作，true表示需要对端设备的回复。|
|writeNoResponse|Bool|否|true| **命名参数。** true表示该特征支持写操作，无需对端设备回复。|
|read|Bool|否|true| **命名参数。** true表示该特征支持读操作。|
|notify|Bool|否|false| **命名参数。** true表示该特征可通知对端设备。|
|indicate|Bool|否|false| **命名参数。** true表示该特征可通知对端设备，需要对端设备的回复。|