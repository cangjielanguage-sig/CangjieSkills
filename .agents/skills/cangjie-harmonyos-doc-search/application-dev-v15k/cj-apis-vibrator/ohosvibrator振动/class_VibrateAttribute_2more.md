## class VibrateAttribute

```cangjie
public class VibrateAttribute {
    public var usage: Usage
    public var id: Int32
    public init(usage: Usage, id!: Int32 = 0)
}
```

**功能：** 马达振动属性。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

### var id

```cangjie
public var id: Int32
```

**功能：** 振动器id， 默认值为0。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var usage

```cangjie
public var usage: Usage
```

**功能：** 马达振动的使用场景。

**类型：** [Usage](#enum-usage)

**读写能力：** 可读写

**起始版本：** 19

### init(Usage, Int32)

```cangjie
public init(usage: Usage, id!: Int32 = 0)
```

**功能：** 用于创建VibrateAttribute实例的构造函数。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|usage|[Usage](#enum-usage)|是|-|马达振动的使用场景。|
|id|Int32|否|0| **命名参数。** 振动器id， 默认值为0。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*

let attribute = VibrateAttribute(Usage.ALARM)
```

## class VibrateFromFile

```cangjie
public class VibrateFromFile <: VibrateEffect {
    public var fileType: String
    public var hapticFd: HapticFileDescriptor
    public init(fileType: String, hapticFd: HapticFileDescriptor)
}
```

**功能：** 自定义振动类型，仅部分设备支持，当设备不支持此振动类型时，返回错误码，详见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**父类型：**

- [VibrateEffect](#interface-vibrateeffect)

### prop effectType

```cangjie
public prop effectType: String
```

**功能：** 马达振动效果类型。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### var fileType

```cangjie
public var fileType: String
```

**功能：** 值为'file'，按照振动配置文件触发马达振动。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var hapticFd

```cangjie
public var hapticFd: HapticFileDescriptor
```

**功能：** 振动配置文件的描述符。

**类型：** [HapticFileDescriptor](#class-hapticfiledescriptor)

**读写能力：** 可读写

**起始版本：** 19

### init(String, HapticFileDescriptor)

```cangjie
public init(fileType: String, hapticFd: HapticFileDescriptor)
```

**功能：** 用于创建VibrateFromFile实例的构造函数。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fileType|String|是|-|值为'file'，按照振动配置文件触发马达振动。|
|hapticFd|[HapticFileDescriptor](#class-hapticfiledescriptor)|是|-|振动配置文件的描述符。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import kit.CoreFileKit.*

let file = FileFs.open("/data/storage/el2/base/haps/entry/files/vib.json")
let descriptor = HapticFileDescriptor(file.fd)
let vFile = VibrateFromFile("file", descriptor)
```