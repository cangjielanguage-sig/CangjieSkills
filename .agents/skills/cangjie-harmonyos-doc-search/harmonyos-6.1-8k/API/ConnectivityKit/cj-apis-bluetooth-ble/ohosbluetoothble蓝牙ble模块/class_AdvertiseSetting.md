## class AdvertiseSetting

```cangjie
public class AdvertiseSetting {
    public var interval: UInt16
    public var txPower: Int8
    public var connectable: Bool
    public init(interval!: UInt16 = BLE_ADV_DEFAULT_INTERVAL, txPower!: Int8 = BLE_ADV_TX_POWER_MEDIUM_VALUE, connectable!: Bool = true)
}
```

**功能：** 描述BLE广播的发送参数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var connectable

```cangjie
public var connectable: Bool
```

**功能：** 是否是可连接广播。true表示发送可连接广播，false表示发送不可连接广播。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var interval

```cangjie
public var interval: UInt16
```

**功能：** 广播发送间隔。

取值范围：[32, 16777215]，单位：slot（时间槽），一个slot代表0.625毫秒。

其中传统广播的最大值是16384。

**类型：** UInt16

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var txPower

```cangjie
public var txPower: Int8
```

**功能：** 广播发送功率。取值范围：[-127, 1]，单位：dBm。

考虑到发送广播的性能和功耗，建议高档取值为1，中档取为-7，低档取值为-15。

**类型：** Int8

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### init(UInt16, Int8, Bool)

```cangjie
public init(interval!: UInt16 = BLE_ADV_DEFAULT_INTERVAL, txPower!: Int8 = BLE_ADV_TX_POWER_MEDIUM_VALUE, connectable!: Bool = true)
```

**功能：** 构造蓝牙低功耗设备发送广播的参数结构。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|interval|UInt16|否|BLE_ADV_DEFAULT_INTERVAL|**命名参数。** 广播发送间隔。取值范围：[32, 16777215]，单位：slot（时间槽），一个slot代表0.625毫秒，默认值为1600。|
|txPower|Int8|否|BLE_ADV_TX_POWER_MEDIUM_VALUE|**命名参数。** 广播发送功率。取值范围：[-127, 1]，单位：dBm，默认值为-7。|
|connectable|Bool|否|true|**命名参数。** 是否是可连接广播。true表示发送可连接广播，false表示发送不可连接广播，默认值为true。|