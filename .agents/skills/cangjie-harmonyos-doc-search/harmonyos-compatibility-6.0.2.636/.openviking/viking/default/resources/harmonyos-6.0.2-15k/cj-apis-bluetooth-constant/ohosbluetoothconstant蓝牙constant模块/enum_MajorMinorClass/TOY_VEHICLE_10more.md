### TOY_VEHICLE

```cangjie
TOY_VEHICLE
```

**功能：** 表示玩具车设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### WEARABLE_GLASSES

```cangjie
WEARABLE_GLASSES
```

**功能：** 表示可穿戴眼镜设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### WEARABLE_HELMET

```cangjie
WEARABLE_HELMET
```

**功能：** 表示可穿戴头盔设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### WEARABLE_JACKET

```cangjie
WEARABLE_JACKET
```

**功能：** 表示夹克可穿戴设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### WEARABLE_PAGER

```cangjie
WEARABLE_PAGER
```

**功能：** 表示可穿戴寻呼机设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### WEARABLE_UNCATEGORIZED

```cangjie
WEARABLE_UNCATEGORIZED
```

**功能：** 表示未分类的可穿戴设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### WEARABLE_WRIST_WATCH

```cangjie
WEARABLE_WRIST_WATCH
```

**功能：** 表示可穿戴腕表设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(MajorMinorClass)

```cangjie
public operator func !=(other: MajorMinorClass): Bool
```

**功能：** 对主要次要蓝牙设备类别判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[MajorMinorClass](#enum-majorminorclass)|是|主要次要蓝牙设备类别。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果主要次要蓝牙设备类别不同返回 true，否则返回 false。|

### func ==(MajorMinorClass)

```cangjie
public operator func ==(other: MajorMinorClass): Bool
```

**功能：** 对主要次要蓝牙设备类别进行判等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[MajorMinorClass](#enum-majorminorclass)|是|主要次要蓝牙设备类别。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果主要次要蓝牙设备类别相同返回 true，否则返回 false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回主要次要蓝牙设备类别的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|主要次要蓝牙设备类别的字符串表示。|