## class AdvertisingParams

```cangjie
public class AdvertisingParams {
    public var advertisingSettings: AdvertiseSetting
    public var advertisingData: AdvertiseData
    public var advertisingResponse: AdvertiseData
    public var duration: UInt16
    public init(
        advertisingSettings: AdvertiseSetting,
        advertisingData: AdvertiseData,
        advertisingResponse!: AdvertiseData = AdvertiseData([], [], []),
        duration!: UInt16 = 0
    )
}
```

**功能：** 首次启动BLE广播时设置的参数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var advertisingData

```cangjie
public var advertisingData: AdvertiseData
```

**功能：** 需要发送的广播报文数据内容。

**类型：** [AdvertiseData](#class-advertisedata)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var advertisingResponse

```cangjie
public var advertisingResponse: AdvertiseData
```

**功能：** 回复扫描请求的广播报文数据内容。

**类型：** [AdvertiseData](#class-advertisedata)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var advertisingSettings

```cangjie
public var advertisingSettings: AdvertiseSetting
```

**功能：** 广播的发送参数。

**类型：** [AdvertiseSetting](#class-advertisesetting)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var duration

```cangjie
public var duration: UInt16
```

**功能：** 发送广播的持续时间。取值范围：[1, 65535]，单位：10ms。

**类型：** UInt16

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### init(AdvertiseSetting, AdvertiseData, AdvertiseData, UInt16)

```cangjie
public init(
    advertisingSettings: AdvertiseSetting,
    advertisingData: AdvertiseData,
    advertisingResponse!: AdvertiseData = AdvertiseData([], [], []),
    duration!: UInt16 = 0
)
```

**功能：** AdvertisingParams 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|advertisingSettings|[AdvertiseSetting](#class-advertisesetting)|是|-|广播的发送参数。|
|advertisingData|[AdvertiseData](#class-advertisedata)|是|-|需要发送的广播报文数据内容。|
|advertisingResponse|[AdvertiseData](#class-advertisedata)|否|AdvertiseData([],[],[])| **命名参数。** 回复扫描请求的广播报文数据内容。|
|duration|UInt16|否|0| **命名参数。** 发送广播的持续时间。取值范围：[1, 65535]，单位：10ms。|