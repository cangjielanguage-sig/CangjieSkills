## enum WindowEventType

```cangjie
public enum WindowEventType {
    | WINDOW_SHOWN
    | WINDOW_ACTIVE
    | WINDOW_INACTIVE
    | WINDOW_HIDDEN
    | WINDOW_DESTROYED
}
```

**功能：** 窗口生命周期。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### WINDOW_SHOWN

```cangjie
WINDOW_SHOWN
```

**功能：** 切到前台。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### WINDOW_ACTIVE

```cangjie
WINDOW_ACTIVE
```

**功能：** 获焦状态。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### WINDOW_INACTIVE

```cangjie
WINDOW_INACTIVE
```

**功能：** 失焦状态。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### WINDOW_HIDDEN

```cangjie
WINDOW_HIDDEN
```

**功能：** 切到后台。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### WINDOW_DESTROYED

```cangjie
WINDOW_DESTROYED
```

**功能：** 窗口销毁。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

## enum WindowStageEventType

```cangjie
public enum WindowStageEventType {
    | SHOWN
    | ACTIVE
    | INACTIVE
    | HIDDEN
    | RESUMED
    | PAUSED
}
```

**功能：** WindowStage生命周期。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### SHOWN

```cangjie
SHOWN
```

**功能：** 切到前台，例如点击应用图标启动，无论是首次启动还是从后台启动均会触发。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### ACTIVE

```cangjie
ACTIVE
```

**功能：** 获焦状态，例如应用窗口处理点击事件后的状态、应用启动后的状态。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### INACTIVE

```cangjie
INACTIVE
```

**功能：** 失焦状态，例如打开新应用或点击其他窗口后，原获焦窗口的状态。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### HIDDEN

```cangjie
HIDDEN
```

**功能：** 切到后台，例如应用上滑退出、应用窗口关闭。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### RESUMED

```cangjie
RESUMED
```

**功能：** 前台可交互状态，例如应用打开后，可以与用户交互的状态。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### PAUSED

```cangjie
PAUSED
```

**功能：** 前台不可交互状态，例如从屏幕底部上划，应用进入到多任务界面后的状态。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

## enum WindowStatusType

```cangjie
public enum WindowStatusType {
    | UNDEFINED
    | FULL_SCREEN
    | MAXIMIZE
    | MINIMIZE
    | FLOATING
    | SPLIT_SCREEN
}
```

**功能：** 窗口模式枚举。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 12

### UNDEFINED

```cangjie
UNDEFINED
```

**功能：** 表示APP未定义窗口模式。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 12

### FULL_SCREEN

```cangjie
FULL_SCREEN
```

**功能：** 表示APP全屏模式。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 12

### MAXIMIZE

```cangjie
MAXIMIZE
```

**功能：** 表示APP窗口最大化模式。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 12

### MINIMIZE

```cangjie
MINIMIZE
```

**功能：** 表示APP窗口最小化模式。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 12

### FLOATING

```cangjie
FLOATING
```

**功能：** 表示APP自由悬浮形式窗口模式。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 12

### SPLIT_SCREEN

```cangjie
SPLIT_SCREEN
```

**功能：** 表示APP分屏模式。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 12