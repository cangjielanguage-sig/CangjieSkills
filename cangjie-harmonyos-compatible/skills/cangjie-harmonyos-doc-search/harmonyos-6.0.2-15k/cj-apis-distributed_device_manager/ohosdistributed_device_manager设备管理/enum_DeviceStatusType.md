## enum DeviceStatusType

```cangjie
public enum DeviceStatusType <: Equatable<DeviceStatusType> & ToString {
    | DEVICE_STATE_CHANGE
    | DISCOVER_SUCCESS
    | DEVICE_NAME_CHANGE
    | DISCOVER_FAILURE
    | UNKNOWN
    | ...
}
```

**功能：** 作为[on](#func-ondevicestatustype-callbackobject)或[off](#func-offdevicestatustype-callbackobject)函数中的\`type`参数传入，用于表示注册函数的类型。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**父类型：**

- Equatable\<DeviceStatusType>
- ToString

### DEVICE_NAME_CHANGE

```cangjie
DEVICE_NAME_CHANGE
```

**功能：** 表示设备名称发生变化。

**起始版本：** 19

### DEVICE_STATE_CHANGE

```cangjie
DEVICE_STATE_CHANGE
```

**功能：** 表示设备状态发生变化。

**起始版本：** 19

### DISCOVER_FAILURE

```cangjie
DISCOVER_FAILURE
```

**功能：** 表示发现设备失败。

**起始版本：** 19

### DISCOVER_SUCCESS

```cangjie
DISCOVER_SUCCESS
```

**功能：** 表示发现设备成功。

**起始版本：** 19

### UNKNOWN

```cangjie
UNKNOWN
```

**功能：** 表示未知的类型。

**起始版本：** 19

### func !=(DeviceStatusType)

```cangjie
public operator func !=(other: DeviceStatusType): Bool
```

**功能：** 对注册函数类型进行判不等。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DeviceStatusType](#enum-devicestatustype)|是|-|获取注册函数类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果获取注册函数类型不同，返回true，否则返回false。|

### func ==(DeviceStatusType)

```cangjie
public operator func ==(other: DeviceStatusType): Bool
```

**功能：** 对注册函数类型进行判等。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DeviceStatusType](#enum-devicestatustype)|是|-|获取注册函数类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果获取注册函数类型相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回注册函数类型的字符串表示。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|注册函数类型的字符串表示。|