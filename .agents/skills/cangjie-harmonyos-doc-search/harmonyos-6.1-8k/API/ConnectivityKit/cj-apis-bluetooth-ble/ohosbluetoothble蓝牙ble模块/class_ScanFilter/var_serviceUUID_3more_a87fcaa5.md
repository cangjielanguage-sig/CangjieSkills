### var serviceUUID

```cangjie
public var serviceUUID: String
```

**功能：** 过滤包含该服务UUID的广播报文。例如：00001888-0000-1000-8000-00805f9b34fb。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var serviceUUIDMask

```cangjie
public var serviceUUIDMask: String
```

**功能：** 搭配serviceUUID过滤器使用，可设置过滤部分服务UUID。例如：FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### init(String, String, String, String, String, String, Array\<Byte>, Array\<Byte>, UInt16, Array\<Byte>, Array\<Byte>)

```cangjie
public init(
    deviceId!: String = "",
    name!: String = "",
    serviceUUID!: String = "",
    serviceUUIDMask!: String = "",
    serviceSolicitationUUID!: String = "",
    serviceSolicitationUUIDMask!: String = "",
    serviceData!: Array<Byte> = [],
    serviceDataMask!: Array<Byte> = [],
    manufactureId!: UInt16 = 0,
    manufactureData!: Array<Byte> = [],
    manufactureDataMask!: Array<Byte> = []
)
```

**功能：** 创建扫描过滤参数结构体ScanFilter。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deviceId|String|否|""|**命名参数。** 过滤该BLE设备地址的广播报文。例如："XX:XX:XX:XX:XX:XX"。预留字段，本版本暂不支持。|
|name|String|否|""|**命名参数。** 过滤该BLE设备名称的广播报文。预留字段，本版本暂不支持。|
|serviceUUID|String|否|""|**命名参数。** 过滤包含该服务UUID的广播报文。例如：00001888-0000-1000-8000-00805f9b34fb。预留字段，本版本暂不支持。|
|serviceUUIDMask|String|否|""|**命名参数。** 搭配serviceUUID过滤器使用，可设置过滤部分服务UUID。例如：FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF。预留字段，本版本暂不支持。|
|serviceSolicitationUUID|String|否|""|**命名参数。** 过滤包含该服务请求UUID的广播报文。例如：00001888-0000-1000-8000-00805F9B34FB。预留字段，本版本暂不支持。|
|serviceSolicitationUUIDMask|String|否|""|**命名参数。** 搭配serviceSolicitationUuid过滤器使用，可设置过滤部分服务请求UUID。例如：FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF。预留字段，本版本暂不支持。|
|serviceData|Array\<Byte>|否|[]|**命名参数。** 过滤包含该服务数据的广播报文。例如：[0x90,0x00,0xF1,0xF2]。预留字段，本版本暂不支持。|
|serviceDataMask|Array\<Byte>|否|[]|**命名参数。** 搭配serviceData过滤器使用，可设置过滤部分服务数据。例如：[0xFF,0xFF,0xFF,0xFF]。预留字段，本版本暂不支持。|
|manufactureId|UInt16|否|0|**命名参数。** 过滤包含该制造商标识符的广播报文。例如：0x0006。预留字段，本版本暂不支持。|
|manufactureData|Array\<Byte>|否|[]|**命名参数。** 搭配manufactureId过滤器使用，过滤包含该制造商数据的广播报文。例如：[0x1F,0x2F,0x3F]。预留字段，本版本暂不支持。|
|manufactureDataMask|Array\<Byte>|否|[]|**命名参数。** 搭配manufactureData过滤器使用，可设置过滤部分制造商数据。例如：[0xFF,0xFF,0xFF]。预留字段，本版本暂不支持。|