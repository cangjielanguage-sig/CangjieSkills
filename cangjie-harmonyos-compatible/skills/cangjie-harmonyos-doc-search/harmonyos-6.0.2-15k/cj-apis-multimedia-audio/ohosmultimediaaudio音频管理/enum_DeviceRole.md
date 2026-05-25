## enum DeviceRole

```cangjie
public enum DeviceRole <: Equatable<DeviceRole> & ToString {
    | INPUT_DEVICE
    | OUTPUT_DEVICE
    | ...
}
```

**功能：** 设备角色。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**父类型：**

- Equatable\<[DeviceRole](#enum-devicerole)>
- ToString

### INPUT_DEVICE

```cangjie
INPUT_DEVICE
```

**功能：** 输入设备角色。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### OUTPUT_DEVICE

```cangjie
OUTPUT_DEVICE
```

**功能：** 输出设备角色。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(DeviceRole)

```cangjie
public operator func !=(other: DeviceRole): Bool
```

**功能：** 对设备角色枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DeviceRole](#enum-devicerole)|是|-|设备角色。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果设备角色不同，返回true，否则返回false。|

### func ==(DeviceRole)

```cangjie
public operator func ==(other: DeviceRole): Bool
```

**功能：** 对设备角色枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DeviceRole](#enum-devicerole)|是|-|设备角色。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果设备角色相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取设备角色枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|设备角色枚举值的字符串表示。|