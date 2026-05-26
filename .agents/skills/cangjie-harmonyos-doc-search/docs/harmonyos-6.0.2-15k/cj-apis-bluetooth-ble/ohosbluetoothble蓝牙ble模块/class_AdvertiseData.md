## class AdvertiseData

```cangjie
public class AdvertiseData {
    public AdvertiseData(
        public var serviceUuids: Array<String>,
        public var manufactureData: Array<ManufactureData>,
        public var serviceData: Array<ServiceData>,
        public var includeDeviceName!: Bool = false
    )
}
```

**功能：** 描述BLE广播数据包的内容，广播包数据长度为31个字节。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### var includeDeviceName

```cangjie
public var includeDeviceName: Bool = false
```

**功能：** 表示是否携带设备名，可选参数。true表示携带，false或未设置此参数表示不携带。注意带上设备名时广播包长度不能超出31个字节。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var manufactureData

```cangjie
public var manufactureData: Array<ManufactureData>
```

**功能：** 表示要广播的广播的制造商信息列表。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Array\<[ManufactureData](#class-manufacturedata)>

**读写能力：** 可读写

**起始版本：** 19

### var serviceData

```cangjie
public var serviceData: Array<ServiceData>
```

**功能：** 表示要广播的服务数据列表。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Array\<[ServiceData](#class-servicedata)>

**读写能力：** 可读写

**起始版本：** 19

### var serviceUuids

```cangjie
public var serviceUuids: Array<String>
```

**功能：** 表示要广播的服务列表。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 19

### AdvertiseData(Array\<String>, Array\<ManufactureData>, Array\<ServiceData>, Bool)

```cangjie
public AdvertiseData(
    public var serviceUuids: Array<String>,
    public var manufactureData: Array<ManufactureData>,
    public var serviceData: Array<ServiceData>,
    public var includeDeviceName!: Bool = false
)
```

**功能：** AdvertiseData 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|serviceUuids|Array\<String>|是|-|表示要广播的服务 UUID 列表。|
|manufactureData|Array\<[ManufactureData](#class-manufacturedata)>|是|-|表示要广播的广播的制造商信息列表。|
|serviceData|Array\<[ServiceData](#class-servicedata)>|是|-|表示要广播的服务数据列表。|
|includeDeviceName|Bool|否|false| **命名参数。** 表示是否携带设备名，可选参数。true表示携带，false或未设置此参数表示不携带。注意带上设备名时广播包长度不能超出31个字节。|