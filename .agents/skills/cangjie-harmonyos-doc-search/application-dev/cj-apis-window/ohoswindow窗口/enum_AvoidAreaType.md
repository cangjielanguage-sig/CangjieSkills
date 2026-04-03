## enum AvoidAreaType

```cangjie
public enum AvoidAreaType <: Equatable<AvoidAreaType> {
    | TypeSystem
    | TypeCutout
    | TypeSystemGesture
    | TypeKeyboard
    | TypeNavigationIndicator
    | ...
}
```

**功能：** 描述避免区域类型。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**父类型：**

- Equatable\<[AvoidAreaType](#enum-avoidareatype)>

### TypeSystem

```cangjie
TypeSystem
```

**功能：** 系统默认区域。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### TypeCutout

```cangjie
TypeCutout
```

**功能：** 刘海屏区域。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### TypeSystemGesture

```cangjie
TypeSystemGesture
```

**功能：** 系统手势区域。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### TypeKeyboard

```cangjie
TypeKeyboard
```

**功能：** 键盘区域。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### TypeNavigationIndicator

```cangjie
TypeNavigationIndicator
```

**功能：** 导航指示器区域。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### operator func !=(AvoidAreaType)

```cangjie
public operator func !=(other: AvoidAreaType): Bool
```

**功能：** 不等比较运算符。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AvoidAreaType](#enum-avoidareatype)|是|-|要比较的另一个AvoidAreaType实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，不相等时返回true。|

### operator func ==(AvoidAreaType)

```cangjie
public operator func ==(other: AvoidAreaType): Bool
```

**功能：** 相等比较运算符。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AvoidAreaType](#enum-avoidareatype)|是|-|要比较的另一个AvoidAreaType实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，相等时返回true。|