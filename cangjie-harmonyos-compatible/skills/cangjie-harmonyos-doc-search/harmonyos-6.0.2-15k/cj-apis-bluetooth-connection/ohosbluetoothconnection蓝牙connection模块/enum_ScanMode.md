## enum ScanMode

```cangjie
public enum ScanMode <: Equatable<ScanMode> & ToString {
    | SCAN_MODE_NONE
    | SCAN_MODE_CONNECTABLE
    | SCAN_MODE_GENERAL_DISCOVERABLE
    | SCAN_MODE_LIMITED_DISCOVERABLE
    | SCAN_MODE_CONNECTABLE_GENERAL_DISCOVERABLE
    | SCAN_MODE_CONNECTABLE_LIMITED_DISCOVERABLE
    | ...
}
```

**功能：** 扫描模式。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<ScanMode>
- ToString

### SCAN_MODE_CONNECTABLE

```cangjie
SCAN_MODE_CONNECTABLE
```

**功能：** 可连接扫描模式。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### SCAN_MODE_CONNECTABLE_GENERAL_DISCOVERABLE

```cangjie
SCAN_MODE_CONNECTABLE_GENERAL_DISCOVERABLE
```

**功能：** 可连接general发现模式。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### SCAN_MODE_CONNECTABLE_LIMITED_DISCOVERABLE

```cangjie
SCAN_MODE_CONNECTABLE_LIMITED_DISCOVERABLE
```

**功能：** 可连接limited发现模式。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### SCAN_MODE_GENERAL_DISCOVERABLE

```cangjie
SCAN_MODE_GENERAL_DISCOVERABLE
```

**功能：** general发现模式。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### SCAN_MODE_LIMITED_DISCOVERABLE

```cangjie
SCAN_MODE_LIMITED_DISCOVERABLE
```

**功能：** limited发现模式。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### SCAN_MODE_NONE

```cangjie
SCAN_MODE_NONE
```

**功能：** 没有扫描模式。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(ScanMode)

```cangjie
public operator func !=(other: ScanMode): Bool
```

**功能：** 对扫描模式进行判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[ScanMode](#enum-scanmode)|是|扫描模式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两扫描模式不同返回 true，否则返回 false。|

### func ==(ScanMode)

```cangjie
public operator func ==(other: ScanMode): Bool
```

**功能：** 对扫描模式进行判等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[ScanMode](#enum-scanmode)|是|扫描模式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两扫描模式相同返回 true，否则返回 false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回扫描模式的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|扫描模式的字符串表示。|