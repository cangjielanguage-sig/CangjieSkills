## enum SourceTool

```cangjie
public enum SourceTool <: Equatable<SourceTool> {
    | Unknown
    | Finger
    | Pen
    | Mouse
    | Touchpad
    | Joystick
    | ...
}
```

**功能：** 事件输入源

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[SourceTool](#enum-sourcetool)>

### Unknown

```cangjie
Unknown
```

**功能：** 未知输入源。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Finger

```cangjie
Finger
```

**功能：** 手指输入。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Pen

```cangjie
Pen
```

**功能：** 手写笔输入。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Mouse

```cangjie
Mouse
```

**功能：** 鼠标输入。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Touchpad

```cangjie
Touchpad
```

**功能：** 触控板输入。触控板单指输入被视为鼠标输入操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Joystick

```cangjie
Joystick
```

**功能：** 手柄输入。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(SourceTool)

```cangjie
public operator func ==(other: SourceTool): Bool
```

**功能：** 判断两个SourceTool枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SourceTool](#enum-sourcetool)|是|-|要比较的另一个SourceTool枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(SourceTool)

```cangjie
public operator func !=(other: SourceTool): Bool
```

**功能：** 判断两个SourceTool枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SourceTool](#enum-sourcetool)|是|-|要比较的另一个SourceTool枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|