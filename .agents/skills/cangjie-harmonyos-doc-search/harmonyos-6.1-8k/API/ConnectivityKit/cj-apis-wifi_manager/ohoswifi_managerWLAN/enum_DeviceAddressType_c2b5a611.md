## enum DeviceAddressType

```cangjie
public enum DeviceAddressType <: Equatable<DeviceAddressType> & ToString {
    | RandomDeviceAddress
    | RealDeviceAddress
    | ...
}
```

**功能：** wifi 设备地址（mac/bssid）类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 22

**父类型：**

- Equatable\<DeviceAddressType>
- ToString

### RandomDeviceAddress

```cangjie
RandomDeviceAddress
```

**功能：** 随机设备地址。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 22

### RealDeviceAddress

```cangjie
RealDeviceAddress
```

**功能：** 真实设备地址。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 22

### func !=(DeviceAddressType)

```cangjie
public operator func !=(other: DeviceAddressType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DeviceAddressType](#enum-deviceaddresstype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(DeviceAddressType)

```cangjie
public operator func ==(other: DeviceAddressType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DeviceAddressType](#enum-deviceaddresstype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|