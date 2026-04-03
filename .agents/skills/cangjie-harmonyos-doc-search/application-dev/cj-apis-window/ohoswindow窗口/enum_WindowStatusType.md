## enum WindowStatusType

```cangjie
public enum WindowStatusType <: Equatable<WindowStatusType> {
    | Undefined
    | FullScreen
    | Maximize
    | Minimize
    | Floating
    | SplitScreen
    | ...
}
```

**功能：** 描述应用程序的窗口状态。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**父类型：**

- Equatable\<[WindowStatusType](#enum-windowstatustype)>

### Undefined

```cangjie
Undefined
```

**功能：** 窗口未定义状态。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### FullScreen

```cangjie
FullScreen
```

**功能：** 窗口全屏状态。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### Maximize

```cangjie
Maximize
```

**功能：** 窗口最大化状态。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### Minimize

```cangjie
Minimize
```

**功能：** 窗口最小化状态。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### Floating

```cangjie
Floating
```

**功能：** 窗口浮动状态。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### SplitScreen

```cangjie
SplitScreen
```

**功能：** 窗口分屏状态。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### operator func !=(WindowStatusType)

```cangjie
public operator func !=(other: WindowStatusType): Bool
```

**功能：** 不等比较运算符。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WindowStatusType](#enum-windowstatustype)|是|-|要比较的另一个WindowStatusType实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，不相等时返回true。|

### operator func ==(WindowStatusType)

```cangjie
public operator func ==(other: WindowStatusType): Bool
```

**功能：** 相等比较运算符。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WindowStatusType](#enum-windowstatustype)|是|-|要比较的另一个WindowStatusType实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，相等时返回true。|