## enum DeviceStateChange

```cangjie
public enum DeviceStateChange <: Equatable<DeviceStateChange> & ToString {
    | UNKNOWN
    | AVAILABLE
    | UNAVAILABLE
    | ...
}
```

**功能：** 设备状态。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**父类型：**

- Equatable\<DeviceStateChange>
- ToString

### AVAILABLE

```cangjie
AVAILABLE
```

**功能：** 表示设备处于可用状态，表示设备间信息已在分布式数据中同步完成, 可以运行分布式业务。

**起始版本：** 19

### UNAVAILABLE

```cangjie
UNAVAILABLE
```

**功能：** 表示设备物理下线，此时状态未知。

**起始版本：** 19

### UNKNOWN

```cangjie
UNKNOWN
```

**功能：** 表示设备物理上线，此时状态未知，在状态更改为可用之前，分布式业务无法使用。

**起始版本：** 19

### func !=(DeviceStateChange)

```cangjie
public operator func !=(other: DeviceStateChange): Bool
```

**功能：** 对设备状态改变进行判不等。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DeviceStateChange](#enum-devicestatechange)|是|-|获取设备状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果设备状态不改变，返回true，否则返回false。|

### func ==(DeviceStateChange)

```cangjie
public operator func ==(other: DeviceStateChange): Bool
```

**功能：** 对设备状态改变进行判等。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DeviceStateChange](#enum-devicestatechange)|是|-|获取设备状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果设备状态改变，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回设备状态的字符串表示。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|设备状态的字符串表示。|