## class HapticFileDescriptor

```cangjie
public class HapticFileDescriptor {
    public var fd: Int32
    public var offSet: Int64
    public var length: Int64
    public init(fd: Int32, offSet!: Int64 = 0, length!: Int64 = FileFs.stat(fd).size - offSet)
}
```

**功能：** 自定义振动配置文件的描述符，必须确认资源文件可用，其参数可通过[文件管理API](../CoreFileKit/cj-apis-file_fs.md#static-func-openstring-int64)从沙箱路径获取或者通过[资源管理API](../LocalizationKit/cj-apis-resource_manager.md#func-getrawfdstring)从HAP资源获取。使用场景：振动序列被存储在一个文件中，需要根据偏移量和长度进行振动，振动序列存储格式。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

### var fd

```cangjie
public var fd: Int32
```

**功能：** 资源文件描述符。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var length

```cangjie
public var length: Int64
```

**功能：** 资源长度，单位为字节。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### var offSet

```cangjie
public var offSet: Int64
```

**功能：** 距文件起始位置的偏移量，单位为字节。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### init(Int32, Int64, Int64)

```cangjie
public init(fd: Int32, offSet!: Int64 = 0, length!: Int64 = FileFs.stat(fd).size - offSet)
```

**功能：** 用于创建HapticFileDescriptor实例的构造函数。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|资源文件描述符。|
|offSet|Int64|否|0| **命名参数。** 距文件起始位置的偏移量，单位为字节。|
|length|Int64|否|[FileFs.stat(fd).size](../CoreFileKit/cj-apis-file_fs.md#static-func-statint32) - offSet| **命名参数。** 资源长度，单位为字节。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import kit.CoreFileKit.*

let file = FileFs.open("/data/storage/el2/base/haps/entry/files/vib.json")
let descriptor = HapticFileDescriptor(file.fd)
```