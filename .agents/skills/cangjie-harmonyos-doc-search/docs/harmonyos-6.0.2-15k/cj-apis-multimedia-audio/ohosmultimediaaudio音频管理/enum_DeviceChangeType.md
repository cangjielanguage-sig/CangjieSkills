## enum DeviceChangeType

```cangjie
public enum DeviceChangeType <: Equatable<DeviceChangeType> & ToString {
    | CONNECT
    | DISCONNECT
    | ...
}
```

**功能：** 设备连接状态变化。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**父类型：**

- Equatable\<[DeviceChangeType](#enum-devicechangetype)>
- ToString

### CONNECT

```cangjie
CONNECT
```

**功能：** 设备连接。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### DISCONNECT

```cangjie
DISCONNECT
```

**功能：** 断开设备连接。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(DeviceChangeType)

```cangjie
public operator func !=(other: DeviceChangeType): Bool
```

**功能：** 对设备连接状态变化枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DeviceChangeType](#enum-devicechangetype)|是|-|设备连接状态变化。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果设备连接状态变化不同，返回true，否则返回false。|

### func ==(DeviceChangeType)

```cangjie
public operator func ==(other: DeviceChangeType): Bool
```

**功能：** 对设备连接状态变化枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DeviceChangeType](#enum-devicechangetype)|是|-|设备连接状态变化。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果设备连接状态变化相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取设备连接状态变化枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|设备连接状态变化枚举值的字符串表示。|