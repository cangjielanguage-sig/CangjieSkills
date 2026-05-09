## enum WindowCallbackType

```cangjie
public enum WindowCallbackType <: Equatable<WindowCallbackType> {
    | WindowStageEvent
    | WindowSizeChange
    | WindowAvoidAreaChange
    | KeyboardHeightChange
    | TouchOutside
    | WindowVisibilityChange
    | NoInteractionDetected
    | Screenshot
    | DialogTargetTouch
    | WindowEvent
    | WindowStatusChange
    | SubWindowClose
    | WindowTitleButtonRectChange
    | WindowRectChange
    | ...
}
```

**功能：** 监听事件枚举。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**父类型：**

- Equatable\<[WindowCallbackType](#enum-windowcallbacktype)>

### WindowStageEvent

```cangjie
WindowStageEvent
```

**功能：** 表示窗口阶段生命周期变化事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### WindowSizeChange

```cangjie
WindowSizeChange
```

**功能：** 表示窗口大小变化事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### WindowAvoidAreaChange

```cangjie
WindowAvoidAreaChange
```

**功能：** 表示避免区域变化事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### KeyboardHeightChange

```cangjie
KeyboardHeightChange
```

**功能：** 表示键盘高度变化事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### TouchOutside

```cangjie
TouchOutside
```

**功能：** 表示窗口外部点击事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### WindowVisibilityChange

```cangjie
WindowVisibilityChange
```

**功能：** 表示窗口可见性变化。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### NoInteractionDetected

```cangjie
NoInteractionDetected
```

**功能：** 表示窗口长时间无交互。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### Screenshot

```cangjie
Screenshot
```

**功能：** 表示截图事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### DialogTargetTouch

```cangjie
DialogTargetTouch
```

**功能：** 表示模态窗口模式下目标窗口点击事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### WindowEvent

```cangjie
WindowEvent
```

**功能：** 表示窗口生命周期变化事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### WindowStatusChange

```cangjie
WindowStatusChange
```

**功能：** 表示窗口状态变化事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### SubWindowClose

```cangjie
SubWindowClose
```

**功能：** 表示子窗口关闭事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### WindowTitleButtonRectChange

```cangjie
WindowTitleButtonRectChange
```

**功能：** 表示标题按钮区域变化事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### WindowRectChange

```cangjie
WindowRectChange
```

**功能：** 表示窗口矩形变化事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### operator func !=(WindowCallbackType)

```cangjie
public operator func !=(other: WindowCallbackType): Bool
```

**功能：** 不等比较运算符。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WindowCallbackType](#enum-windowcallbacktype)|是|-|要比较的另一个WindowCallbackType实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，不相等时返回true。|