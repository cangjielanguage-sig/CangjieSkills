## enum MajorClass

```cangjie
public enum MajorClass <: Equatable<MajorClass> & ToString {
    | MAJOR_MISC
    | MAJOR_COMPUTER
    | MAJOR_PHONE
    | MAJOR_NETWORKING
    | MAJOR_AUDIO_VIDEO
    | MAJOR_PERIPHERAL
    | MAJOR_IMAGING
    | MAJOR_WEARABLE
    | MAJOR_TOY
    | MAJOR_HEALTH
    | MAJOR_UNCATEGORIZED
    | ...
}
```

**功能：** 蓝牙设备主要类别。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<MajorClass>
- ToString

### MAJOR_AUDIO_VIDEO

```cangjie
MAJOR_AUDIO_VIDEO
```

**功能：** 表示音频和视频设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### MAJOR_COMPUTER

```cangjie
MAJOR_COMPUTER
```

**功能：** 表示计算机设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### MAJOR_HEALTH

```cangjie
MAJOR_HEALTH
```

**功能：** 表示健康设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### MAJOR_IMAGING

```cangjie
MAJOR_IMAGING
```

**功能：** 表示成像设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### MAJOR_MISC

```cangjie
MAJOR_MISC
```

**功能：** 表示杂项设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### MAJOR_NETWORKING

```cangjie
MAJOR_NETWORKING
```

**功能：** 表示网络设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### MAJOR_PERIPHERAL

```cangjie
MAJOR_PERIPHERAL
```

**功能：** 表示外围设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### MAJOR_PHONE

```cangjie
MAJOR_PHONE
```

**功能：** 表示手机设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### MAJOR_TOY

```cangjie
MAJOR_TOY
```

**功能：** 表示玩具设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### MAJOR_UNCATEGORIZED

```cangjie
MAJOR_UNCATEGORIZED
```

**功能：** 表示未分类设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### MAJOR_WEARABLE

```cangjie
MAJOR_WEARABLE
```

**功能：** 表示可穿戴设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(MajorClass)

```cangjie
public operator func !=(other: MajorClass): Bool
```

**功能：** 对主要蓝牙设备类别判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[MajorClass](#enum-majorclass)|是|主要蓝牙设备类别。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果主要蓝牙设备类别不同返回 true，否则返回 false。|

### func ==(MajorClass)

```cangjie
public operator func ==(other: MajorClass): Bool
```

**功能：** 对主要蓝牙设备类别进行判等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[MajorClass](#enum-majorclass)|是|主要蓝牙设备类别。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果主要蓝牙设备类别相同返回 true，否则返回 false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回主要蓝牙设备类别的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|主要蓝牙设备类别。|