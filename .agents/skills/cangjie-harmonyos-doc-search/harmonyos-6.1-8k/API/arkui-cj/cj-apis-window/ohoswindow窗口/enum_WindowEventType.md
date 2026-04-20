## enum WindowEventType

```cangjie
public enum WindowEventType <: Equatable<WindowEventType> {
    | WindowShown
    | WindowActive
    | WindowInactive
    | WindowHidden
    | WindowDestroyed
    | ...
}
```

**功能：** 窗口回调事件类型枚举。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**父类型：**

- Equatable\<[WindowEventType](#enum-windoweventtype)>

### WindowShown

```cangjie
WindowShown
```

**功能：** 窗口显示事件值。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### WindowActive

```cangjie
WindowActive
```

**功能：** 窗口激活事件值。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### WindowInactive

```cangjie
WindowInactive
```

**功能：** 窗口非激活事件值。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### WindowHidden

```cangjie
WindowHidden
```

**功能：** 窗口隐藏事件值。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### WindowDestroyed

```cangjie
WindowDestroyed
```

**功能：** 窗口销毁事件值。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### operator func !=(WindowEventType)

```cangjie
public operator func !=(other: WindowEventType): Bool
```

**功能：** 不等比较运算符。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WindowEventType](#enum-windoweventtype)|是|-|要比较的另一个WindowEventType实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，不相等时返回true。|

### operator func ==(WindowEventType)

```cangjie
public operator func ==(other: WindowEventType): Bool
```

**功能：** 相等比较运算符。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WindowEventType](#enum-windoweventtype)|是|-|要比较的另一个WindowEventType实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，相等时返回true。|