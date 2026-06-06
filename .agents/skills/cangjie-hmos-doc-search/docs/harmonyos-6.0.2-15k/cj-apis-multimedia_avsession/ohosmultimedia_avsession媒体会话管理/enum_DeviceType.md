## enum DeviceType

```cangjie
public enum DeviceType <: Equatable<DeviceType> & ToString {
    | DEVICE_TYPE_LOCAL
    | DEVICE_TYPE_TV
    | DEVICE_TYPE_SMART_SPEAKER
    | DEVICE_TYPE_BLUETOOTH
    | ...
}
```

**功能：** 播放设备的类型枚举。

**系统能力：** 详见各枚举值

**起始版本：** 19

**父类型：**

- Equatable\<[DeviceType](#enum-devicetype)>
- ToString

### DEVICE_TYPE_BLUETOOTH

```cangjie
DEVICE_TYPE_BLUETOOTH
```

**功能：** 蓝牙设备。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

### DEVICE_TYPE_LOCAL

```cangjie
DEVICE_TYPE_LOCAL
```

**功能：** 本地播放类型。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

### DEVICE_TYPE_SMART_SPEAKER

```cangjie
DEVICE_TYPE_SMART_SPEAKER
```

**功能：** 音箱设备。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

### DEVICE_TYPE_TV

```cangjie
DEVICE_TYPE_TV
```

**功能：** 电视。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

### func !=(DeviceType)

```cangjie
public operator func !=(other: DeviceType): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DeviceType](#enum-devicetype)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(DeviceType)

```cangjie
public operator func ==(other: DeviceType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DeviceType](#enum-devicetype)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true, 否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表示。|