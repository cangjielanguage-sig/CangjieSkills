## enum WindowType

```cangjie
public enum WindowType <: Equatable<WindowType> {
    | TypeApp
    | TypeMain
    | TypeFloat
    | TypeDialog
    | ...
}
```

**功能：** 窗口类型。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**父类型：**

- Equatable\<[WindowType](#enum-windowtype)>

### TypeApp

```cangjie
TypeApp
```

**功能：** 应用程序窗口。此窗口类型不支持在创建窗口时使用，仅可在[getWindowProperties](#func-getwindowproperties)接口的返回值中用于读取。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### TypeMain

```cangjie
TypeMain
```

**功能：** 应用主窗口。此窗口类型不支持在创建窗口时使用，仅可在[getWindowProperties](#func-getwindowproperties)接口的返回值中用于读取。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### TypeFloat

```cangjie
TypeFloat
```

**功能：** 浮动窗口。需要"ohos.permission.SYSTEM_FLOAT_WINDOW"权限。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### TypeDialog

```cangjie
TypeDialog
```

**功能：** 对话框窗口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### operator func !=(WindowType)

```cangjie
public operator func !=(other: WindowType): Bool
```

**功能：** 不等比较运算符。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WindowType](#enum-windowtype)|是|-|要比较的另一个WindowType实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，不相等时返回true。|

### operator func ==(WindowType)

```cangjie
public operator func ==(other: WindowType): Bool
```

**功能：** 相等比较运算符。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WindowType](#enum-windowtype)|是|-|要比较的另一个WindowType实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，相等时返回true。|