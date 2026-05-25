## enum WindowStageEventType

```cangjie
public enum WindowStageEventType <: Equatable<WindowStageEventType> {
    | Shown
    | Active
    | Inactive
    | Hidden
    | Resumed
    | Paused
    | ...
}
```

**功能：** 窗口阶段回调事件类型。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**父类型：**

- Equatable\<[WindowStageEventType](#enum-windowstageeventtype)>

### Shown

```cangjie
Shown
```

**功能：** 窗口阶段在前台运行。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### Active

```cangjie
Active
```

**功能：** 窗口阶段获得焦点。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### Inactive

```cangjie
Inactive
```

**功能：** 窗口阶段失去焦点。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### Hidden

```cangjie
Hidden
```

**功能：** 窗口阶段在后台运行。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### Resumed

```cangjie
Resumed
```

**功能：** 窗口阶段在前台交互。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### Paused

```cangjie
Paused
```

**功能：** 窗口阶段在前台非交互。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### operator func !=(WindowStageEventType)

```cangjie
public operator func !=(other: WindowStageEventType): Bool
```

**功能：** 不等比较运算符。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WindowStageEventType](#enum-windowstageeventtype)|是|-|要比较的另一个WindowStageEventType实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，不相等时返回true。|

### operator func ==(WindowStageEventType)

```cangjie
public operator func ==(other: WindowStageEventType): Bool
```

**功能：** 相等比较运算符。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WindowStageEventType](#enum-windowstageeventtype)|是|-|要比较的另一个WindowStageEventType实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，相等时返回true。|