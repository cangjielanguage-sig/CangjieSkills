## class AdvertisingParams

```cangjie
public class AdvertisingParams {
    public AdvertisingParams(
        public var advertisingSettings: AdvertiseSetting,
        public var advertisingData: AdvertiseData,
        public var advertisingResponse: AdvertiseData,
        public var duration!: UInt16 = 0
    )
}
```

**功能：** 描述首次启动广播设置的参数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### var advertisingData

```cangjie
public var advertisingData: AdvertiseData
```

**功能：** 表示广播的数据包内容。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** [AdvertiseData](#class-advertisedata)

**读写能力：** 可读写

**起始版本：** 19

### var advertisingResponse

```cangjie
public var advertisingResponse: AdvertiseData
```

**功能：** 表示回复扫描请求的响应内容。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** [AdvertiseData](#class-advertisedata)

**读写能力：** 可读写

**起始版本：** 19

### var advertisingSettings

```cangjie
public var advertisingSettings: AdvertiseSetting
```

**功能：** 表示发送广播的相关参数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** [AdvertiseSetting](#class-advertisesetting)

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

### AdvertisingParams(AdvertiseSetting, AdvertiseData, AdvertiseData, UInt16)

```cangjie
public AdvertisingParams(
    public var advertisingSettings: AdvertiseSetting,
    public var advertisingData: AdvertiseData,
    public var advertisingResponse: AdvertiseData,
    public var duration!: UInt16 = 0
)
```

**功能：** AdvertisingParams 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|advertisingSettings|[AdvertiseSetting](#class-advertisesetting)|是|-|表示发送广播的相关参数。|
|advertisingData|[AdvertiseData](#class-advertisedata)|是|-|表示广播的数据包内容。|
|advertisingResponse|[AdvertiseData](#class-advertisedata)|是|-|表示回复扫描请求的响应内容。|
|duration|UInt16|否|0| **命名参数。** 表示发送广播持续的时间。单位为10ms，有效范围为1(10ms)到65535(655350ms)，如果未指定此参数或者将其设置为0，则会连续发送广播。|