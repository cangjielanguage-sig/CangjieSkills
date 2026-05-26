## class DeviceCapability

```cangjie
public class DeviceCapability <: ToString {
    public DeviceCapability(
        public let screenDensity: ScreenDensity,
        public let deviceType: DeviceType
    )
}
```

**功能：** 表示设备支持的能力。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**父类型：**

- ToString

### let deviceType

```cangjie
public let deviceType: DeviceType
```

**功能：** 当前设备类型。

**类型：** [DeviceType](#enum-devicetype)

**读写能力：** 只读

**起始版本：** 12

### let screenDensity

```cangjie
public let screenDensity: ScreenDensity
```

**功能：** 当前设备屏幕密度。

**类型：** [ScreenDensity](#enum-screendensity)

**读写能力：** 只读

**起始版本：** 12

### DeviceCapability(ScreenDensity, DeviceType)

```cangjie
public DeviceCapability(
    public let screenDensity: ScreenDensity,
    public let deviceType: DeviceType
)
```

**功能：** 构建设备支持的能力的对象。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|screenDensity|[ScreenDensity](#enum-screendensity)|是|-|当前设备屏幕密度。|
|deviceType|[DeviceType](#enum-devicetype)|是|-|当前设备类型。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前[DeviceCapability](#class-devicecapability)的信息，以字符串表示。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|当前[DeviceCapability](#class-devicecapability)的信息。|

## class DrawableDescriptor

```cangjie
public class DrawableDescriptor {}
```

**功能：** 表示[DrawableDescriptor](#class-drawabledescriptor)实例。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

## class RawFileDescriptor

```cangjie
public class RawFileDescriptor {
    public RawFileDescriptor(
        public let fd: Int32,
        public let offset: Int64,
        public let length: Int64
    )
}
```

**功能：** 表示rawfile的描述符信息。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

### let fd

```cangjie
public let fd: Int32
```

**功能：** rawfile所在hap的文件描述符。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let length

```cangjie
public let length: Int64
```

**功能：** rawfile的文件长度。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12

### let offset

```cangjie
public let offset: Int64
```

**功能：** rawfile的起始偏移量。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12

### RawFileDescriptor(Int32, Int64, Int64)

```cangjie
public RawFileDescriptor(
    public let fd: Int32,
    public let offset: Int64,
    public let length: Int64
)
```

**功能：** 根据文件描述符，起始偏移量和文件长度，构造[RawFileDescriptor](#class-rawfiledescriptor)实例。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|rawfile所在hap的文件描述符。|
|offset|Int64|是|-|rawfile的起始偏移量。|
|length|Int64|是|-|rawfile的文件长度。|