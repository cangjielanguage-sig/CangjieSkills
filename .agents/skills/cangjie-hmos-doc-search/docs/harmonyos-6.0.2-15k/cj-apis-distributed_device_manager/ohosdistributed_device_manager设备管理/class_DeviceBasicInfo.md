## class DeviceBasicInfo

```cangjie
public class DeviceBasicInfo {
    public DeviceBasicInfo(
        public let deviceId: String,
        public let deviceName: String,
        public let deviceType: Int32,  
        public let networkId: String
    )
}
```

**功能：** 分布式设备基本信息。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

### let deviceId

```cangjie
public let deviceId: String
```

**功能：** 设备标识符。实际值为udid-hash与appid和盐值基于sha256方式进行混淆后的值。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let deviceName

```cangjie
public let deviceName: String
```

**功能：** 设备名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let deviceType

```cangjie
public let deviceType: Int32
```

**功能：** [设备类型](#func-getdevicetypestring)。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let networkId

```cangjie
public let networkId: String
```

**功能：** 设备网络标识。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### DeviceBasicInfo(String, String, Int32, String)

```cangjie
public DeviceBasicInfo(
    public let deviceName: String,
    public let deviceType: Int32,
    public let networkId: String
)
```

**功能：** DeviceBasicInfo主构造函数。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deviceId|String|是|-|设备标识。|
|deviceName|String|是|-|设备名称。|
|deviceType|Int32|是|-|[设备类型](#func-getdevicetypestring)。|
|networkId|String|是|-|网络设备Id。|