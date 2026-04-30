## enum DeviceFlag

```cangjie
public enum DeviceFlag <: Equatable<DeviceFlag> & ToString {
    | OUTPUT_DEVICES_FLAG
    | INPUT_DEVICES_FLAG
    | ALL_DEVICES_FLAG
    | ...
}
```

**功能：** 可获取的设备种类。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**父类型：**

- Equatable\<[DeviceFlag](#enum-deviceflag)>
- ToString

### ALL_DEVICES_FLAG

```cangjie
ALL_DEVICES_FLAG
```

**功能：** 所有设备。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### INPUT_DEVICES_FLAG

```cangjie
INPUT_DEVICES_FLAG
```

**功能：** 输入设备。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### OUTPUT_DEVICES_FLAG

```cangjie
OUTPUT_DEVICES_FLAG
```

**功能：** 输出设备。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(DeviceFlag)

```cangjie
public operator func !=(other: DeviceFlag): Bool
```

**功能：** 对设备种类枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DeviceFlag](#enum-deviceflag)|是|-|可获取的设备种类。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果设备种类不同，返回true，否则返回false。|

### func ==(DeviceFlag)

```cangjie
public operator func ==(other: DeviceFlag): Bool
```

**功能：** 对设备种类枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DeviceFlag](#enum-deviceflag)|是|-|可获取的设备种类。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果设备种类相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取设备种类枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|设备种类枚举值的字符串表示。|