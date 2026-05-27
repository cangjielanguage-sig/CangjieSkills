## enum WindowCallbackType

```cangjie
public enum WindowCallbackType {
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
}
```

**功能：** 窗口监听回调事件类型枚举。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### WindowStageEvent

```cangjie
WindowStageEvent
```

**功能：** WindowStage生命周期变化事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### WindowSizeChange

```cangjie
WindowSizeChange
```

**功能：** 窗口尺寸变化事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### WindowAvoidAreaChange

```cangjie
WindowAvoidAreaChange
```

**功能：** 系统规避区变化事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### KeyboardHeightChange

```cangjie
KeyboardHeightChange
```

**功能：** 键盘高度变化事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### TouchOutside

```cangjie
TouchOutside
```

**功能：** 本窗口范围外的点击事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### WindowVisibilityChange

```cangjie
WindowVisibilityChange
```

**功能：** 本窗口可见状态变化的事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### NoInteractionDetected

```cangjie
NoInteractionDetected
```

**功能：** 本窗口在指定超时时间内无交互的事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### Screenshot

```cangjie
Screenshot
```

**功能：** 截屏事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### DialogTargetTouch

```cangjie
DialogTargetTouch
```

**功能：** 模态窗口所遮盖窗口的点击或触摸事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### WindowEvent

```cangjie
WindowEvent
```

**功能：** 窗口生命周期变化事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### WindowStatusChange

```cangjie
WindowStatusChange
```

**功能：** 窗口模式变化事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### SubWindowClose

```cangjie
SubWindowClose
```

**功能：** 子窗口关闭事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### WindowTitleButtonRectChange

```cangjie
WindowTitleButtonRectChange
```

**功能：** 标题栏上的最小化、最大化、关闭按钮矩形区域变化事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### WindowRectChange

```cangjie
WindowRectChange
```

**功能：** 窗口矩形变化事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19