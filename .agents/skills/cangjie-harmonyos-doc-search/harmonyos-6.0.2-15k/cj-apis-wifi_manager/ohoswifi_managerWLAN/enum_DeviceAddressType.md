## enum DeviceAddressType

```cangjie
public enum DeviceAddressType <: ToString {
    | RANDOM_DEVICE_ADDRESS
    | REAL_DEVICE_ADDRESS
    | ...
}
```

**功能：** wifi 设备地址（mac/bssid）类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

**父类型：**

- ToString

### RANDOM_DEVICE_ADDRESS

```cangjie
RANDOM_DEVICE_ADDRESS
```

**功能：** 随机设备地址。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

### REAL_DEVICE_ADDRESS

```cangjie
REAL_DEVICE_ADDRESS
```

**功能：** 真实设备地址。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|