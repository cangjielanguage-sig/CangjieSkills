### init(Bool, Bool, Bool, Bool, Bool, Bool, Bool, Bool)

```cangjie
public init (
    read!: Bool = true,
    readEncrypted!: Bool = false,
    readEncryptedMitm!: Bool = false,
    write!: Bool = true,
    writeEncrypted!: Bool = false,
    writeEncryptedMitm!: Bool = false,
    writeSigned!: Bool = false,
    writeSignedMitm!: Bool = false
)
```

**功能：** GattPermissions 构造器

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|read|Bool|否|true|**命名参数。** 是否允许读取该特征值或描述符内容。|
|readEncrypted|Bool|否|false|**命名参数。** 读取该特征值或描述符内容是否需要加密。|
|readEncryptedMitm|Bool|否|false|**命名参数。** 读取该特征值或描述符内容是否需要防中间人攻击的加密。|
|write|Bool|否|true|**命名参数。** 是否允许写入该特征值或描述符内容。|
|writeEncrypted|Bool|否|false|**命名参数。** 写入该特征值或描述符内容是否需要加密。|
|writeEncryptedMitm|Bool|否|false|**命名参数。** 写入该特征值或描述符内容是否需要防中间人攻击的加密。|
|writeSigned|Bool|否|false|**命名参数。** 写入该特征值或描述符内容是否需要经过签名处理。|
|writeSignedMitm|Bool|否|false|**命名参数。** 写入该特征值或描述符内容是否需要经过防中间人攻击方式的签名处理。|

### func !=(GattPermissions)

```cangjie
public operator func !=(other: GattPermissions): Bool
```

**功能：** 对 GattPermissions 进行判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[GattPermissions](#class-gattpermissions)|是|-|描述符读写操作需要的权限。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果描述符读写操作需要的权限不同，返回true，否则返回false。|

### func ==(GattPermissions)

```cangjie
public operator func ==(other: GattPermissions): Bool
```

**功能：** 对 GattPermissions 进行判等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[GattPermissions](#class-gattpermissions)|是|-|描述符读写操作需要的权限。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果描述符读写操作需要的权限相同，返回true，否则返回false。|