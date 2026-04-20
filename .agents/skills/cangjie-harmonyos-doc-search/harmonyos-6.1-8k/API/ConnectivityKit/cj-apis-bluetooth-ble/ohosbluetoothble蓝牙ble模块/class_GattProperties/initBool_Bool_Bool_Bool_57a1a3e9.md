### init(Bool, Bool, Bool, Bool, Bool, Bool, Bool, Bool)

```cangjie
public init(
    write!: Bool = true,
    writeNoResponse!: Bool = true,
    read!: Bool = true,
    notify!: Bool = false,
    indicate!: Bool = false,
    broadcast!: Bool = false,
    authenticatedSignedWrite!: Bool = false,
    extendedProperties!: Bool = false
)
```

**功能：** GattProperties构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|write|Bool|否|true|**命名参数。** 该特征值是否支持写入操作。|
|writeNoResponse|Bool|否|true|**命名参数。** 该特征值是否支持写入操作。|
|read|Bool|否|true|**命名参数。** 该特征值是否支持读取操作。|
|notify|Bool|否|false|**命名参数。** 该特征值是否支持主动向对端设备通知特征值内容。|
|indicate|Bool|否|false|**命名参数。** 该特征值是否支持向对端设备指示特征值内容。|
|broadcast|Bool|否|false|**命名参数。** 该特征值是否支持作为广播内容由server端发送。<br>true表示支持，server端可将特征值内容以[ServiceData](#class-servicedata)类型在广播报文中携带，false表示不支持。默认值为false。预留字段，本版本暂不支持。|
|authenticatedSignedWrite|Bool|否|false|**命名参数。** 该特征值是否支持签名写入操作，通过对写入内容进行签名校验替代加密流程。<br>true表示支持，且该特征值权限[GattPermissions](#class-gattpermissions)中的writeSigned或writeSignedMitm需设置为true，否则该属性不生效，false表示不支持。默认值为false。预留字段，本版本暂不支持。|
|extendedProperties|Bool|否|false|**命名参数。** 该特征值是否存在扩展属性。<br>true表示存在扩展属性，false表示不存在。默认值为false。预留字段，本版本暂不支持。|