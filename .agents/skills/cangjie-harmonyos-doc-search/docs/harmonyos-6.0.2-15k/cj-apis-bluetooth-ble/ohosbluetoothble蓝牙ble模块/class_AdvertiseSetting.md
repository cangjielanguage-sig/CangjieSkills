## class AdvertiseSetting

```cangjie
public class AdvertiseSetting {
    public var interval: UInt16 = BLE_ADV_DEFAULT_INTERVAL
    public var txPower: Int8 = BLE_ADV_TX_POWER_MEDIUM_VALUE
    public var connectable: Bool = true
    public init(interval: UInt16, txPower: Int8, connectable: Bool)
}
```

**功能：** 描述蓝牙低功耗设备发送广播的参数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### var connectable

```cangjie
public var connectable: Bool = true
```

**功能：** 表示是否是可连接广播，默认值设置为true，表示可连接，false表示不可连接。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var interval

```cangjie
public var interval: UInt16 = BLE_ADV_DEFAULT_INTERVAL
```

**功能：** 表示广播间隔，最小值设置160个slot表示100ms，最大值设置16384个slot，默认值设置为1600个slot表示1s。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** UInt16

**读写能力：** 可读写

**起始版本：** 19

### var txPower

```cangjie
public var txPower: Int8 = BLE_ADV_TX_POWER_MEDIUM_VALUE
```

**功能：** 表示发送功率，最小值设置-127，最大值设置1，默认值设置-7，单位dbm。推荐值：高档（1），中档（-7），低档（-15）。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Int8

**读写能力：** 可读写

**起始版本：** 19

### init(UInt16, Int8, Bool)

```cangjie
public init(interval: UInt16, txPower: Int8, connectable: Bool)
```

**功能：** 构造蓝牙低功耗设备发送广播的参数结构。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|interval|UInt16|是|表示广播间隔，最小值设置160个slot表示100ms，最大值设置16384个slot，默认值设置为1600个slot表示1s。|
|txPower|Int8|是|表示发送功率，最小值设置-127，最大值设置1，默认值设置-7，单位dbm。推荐值：高档（1），中档（-7），低档（-15）。|
|connectable|Bool|是|表示是否是可连接广播，默认值设置为true，表示可连接，false表示不可连接。|