## enum WindowUpdateType

```cangjie
public enum WindowUpdateType <: Equatable<WindowUpdateType> & ToString {
    | WINDOWUPDATETYPE_ADD
    | WINDOWUPDATETYPE_REMOVE
    | WINDOWUPDATETYPE_BOUNDS
    | WINDOWUPDATETYPE_ACTIVE
    | WINDOWUPDATETYPE_FOCUS
    | ...
}
```

**功能：** 窗口变化类型。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**父类型：**

- Equatable\<WindowUpdateType>
- ToString

### WINDOWUPDATETYPE_ACTIVE

```cangjie
WINDOWUPDATETYPE_ACTIVE
```

**功能：** 表示窗口变为活动或不活动的窗口变化事件。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### WINDOWUPDATETYPE_ADD

```cangjie
WINDOWUPDATETYPE_ADD
```

**功能：** 表示添加窗口的窗口变化事件。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### WINDOWUPDATETYPE_BOUNDS

```cangjie
WINDOWUPDATETYPE_BOUNDS
```

**功能：** 表示窗口边界已更改的窗口变化事件。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### WINDOWUPDATETYPE_FOCUS

```cangjie
WINDOWUPDATETYPE_FOCUS
```

**功能：** 表示窗口焦点发生变化的窗口变化事件。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### WINDOWUPDATETYPE_REMOVE

```cangjie
WINDOWUPDATETYPE_REMOVE
```

**功能：** 表示一个窗口被删除的窗口变化事件。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### func !=(WindowUpdateType)

```cangjie
public operator func !=(other: WindowUpdateType): Bool
```

**功能：** 对窗口变化类型进行判不等。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WindowUpdateType](#enum-windowupdatetype)|是|-|窗口变化类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|若窗口变化类型不同，返回true，否则返回false。|

### func ==(WindowUpdateType)

```cangjie
public operator func ==(other: WindowUpdateType): Bool
```

**功能：** 对窗口变化类型进行判等。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WindowUpdateType](#enum-windowupdatetype)|是|-|窗口变化类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|若窗口变化类型相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 将窗口变化类型转换为字符串。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|窗口变化类型的字符串表示。|