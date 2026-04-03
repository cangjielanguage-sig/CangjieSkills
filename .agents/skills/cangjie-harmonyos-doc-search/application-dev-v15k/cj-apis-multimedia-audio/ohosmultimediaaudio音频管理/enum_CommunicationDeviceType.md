## enum CommunicationDeviceType

```cangjie
public enum CommunicationDeviceType <: Equatable<CommunicationDeviceType> & ToString {
    | SPEAKER
    | ...
}
```

**功能：** 用于通信的可用设备类型。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**起始版本：** 19

**父类型：**

- Equatable\<[CommunicationDeviceType](#enum-communicationdevicetype)>
- ToString

### SPEAKER

```cangjie
SPEAKER
```

**功能：** 扬声器。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(CommunicationDeviceType)

```cangjie
public operator func !=(other: CommunicationDeviceType): Bool
```

**功能：** 对用于通信的可用设备类型枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CommunicationDeviceType](#enum-communicationdevicetype)|是|-|用于通信的可用设备类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果用于通信的可用设备类型不同，返回true，否则返回false。|

### func ==(CommunicationDeviceType)

```cangjie
public operator func ==(other: CommunicationDeviceType): Bool
```

**功能：** 对用于通信的可用设备类型枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CommunicationDeviceType](#enum-communicationdevicetype)|是|-|用于通信的可用设备类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果用于通信的可用设备类型相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取用于通信的可用设备类型枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|用于通信的可用设备类型枚举值的字符串表示。|