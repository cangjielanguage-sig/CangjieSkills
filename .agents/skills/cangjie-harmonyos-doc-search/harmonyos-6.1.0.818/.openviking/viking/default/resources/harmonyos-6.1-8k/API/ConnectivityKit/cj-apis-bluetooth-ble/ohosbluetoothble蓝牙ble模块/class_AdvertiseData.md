## class AdvertiseData

```cangjie
public class AdvertiseData {
    public var serviceUUIDs: Array<String>
    public var manufactureData: Array<ManufactureData>
    public var serviceData: Array<ServiceData>
    public var includeDeviceName: Bool
    public init(
        serviceUUIDs: Array<String>,
        manufactureData: Array<ManufactureData>,
        serviceData: Array<ServiceData>,
        includeDeviceName!: Bool = false,
        includeTxPower!: Bool = false
    )
}
```

**功能：** 描述BLE广播报文数据内容，也可以用作回复扫描请求的广播报文数据内容。当前只支持传统广播，因此报文最大长度为31个字节。若超出最大长度（31个字节）限制，会导致启动广播失败。若携带了所有参数，尤其是携带了蓝牙设备名称，需要注意广播报文长度。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var includeDeviceName

```cangjie
public var includeDeviceName: Bool
```

**功能：** 是否携带蓝牙设备名称。true表示携带，false表示不携带。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var manufactureData

```cangjie
public var manufactureData: Array<ManufactureData>
```

**功能：** 要携带的制造商数据内容。

**类型：** Array\<[ManufactureData](#class-manufacturedata)>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var serviceData

```cangjie
public var serviceData: Array<ServiceData>
```

**功能：** 要携带的服务数据内容。

**类型：** Array\<[ServiceData](#class-servicedata)>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var serviceUUIDs

```cangjie
public var serviceUUIDs: Array<String>
```

**功能：** 要携带的服务UUID。

**类型：** Array\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### init(Array\<String>, Array\<ManufactureData>, Array\<ServiceData>, Bool, Bool)

```cangjie
public init(
    serviceUUIDs: Array<String>,
    manufactureData: Array<ManufactureData>,
    serviceData: Array<ServiceData>,
    includeDeviceName!: Bool = false,
    includeTxPower!: Bool = false
)
```

**功能：** AdvertiseData 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|serviceUUIDs|Array\<String>|是|-|要携带的服务UUID。|
|manufactureData|Array\<[ManufactureData](#class-manufacturedata)>|是|-|要携带的制造商数据内容。|
|serviceData|Array\<[ServiceData](#class-servicedata)>|是|-|要携带的服务数据内容。|
|includeDeviceName|Bool|否|false| **命名参数。** 是否携带蓝牙设备名称。true表示携带，false表示不携带，默认值为false。|
|includeTxPower|Bool|否|false| **命名参数。** 是否携带广播发送功率。<br>true表示携带广播发送功率，false表示不携带广播发送功率，默认值为false。<br>携带该值后，广播报文长度将多占用3个字节。|