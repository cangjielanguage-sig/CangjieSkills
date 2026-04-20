## enum AVScreenCaptureStateCode

```cangjie
public enum AVScreenCaptureStateCode <: Equatable<AVScreenCaptureStateCode> & ToString {
    | SCREEN_CAPTURE_STATE_INVALID
    | SCREEN_CAPTURE_STATE_STARTED
    | SCREEN_CAPTURE_STATE_CANCELED
    | SCREEN_CAPTURE_STATE_STOPPED_BY_USER
    | SCREEN_CAPTURE_STATE_INTERRUPTED_BY_OTHER
    | SCREEN_CAPTURE_STATE_STOPPED_BY_CALL
    | SCREEN_CAPTURE_STATE_MIC_UNAVAILABLE
    | SCREEN_CAPTURE_STATE_MIC_MUTED_BY_USER
    | SCREEN_CAPTURE_STATE_MIC_UNMUTED_BY_USER
    | SCREEN_CAPTURE_STATE_ENTER_PRIVATE_SCENE
    | SCREEN_CAPTURE_STATE_EXIT_PRIVATE_SCENE
    | SCREEN_CAPTURE_STATE_STOPPED_BY_USER_SWITCHES
    | ...
}
```

**功能：** 表示状态码。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

**父类型：**

- Equatable\<AVScreenCaptureStateCode>
- ToString

### SCREEN_CAPTURE_STATE_CANCELED

```cangjie
SCREEN_CAPTURE_STATE_CANCELED
```

**功能：** 录屏被取消。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

### SCREEN_CAPTURE_STATE_ENTER_PRIVATE_SCENE

```cangjie
SCREEN_CAPTURE_STATE_ENTER_PRIVATE_SCENE
```

**功能：** 录屏进入隐私页面。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

### SCREEN_CAPTURE_STATE_EXIT_PRIVATE_SCENE

```cangjie
SCREEN_CAPTURE_STATE_EXIT_PRIVATE_SCENE
```

**功能：** 录屏退出隐私页面。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

### SCREEN_CAPTURE_STATE_INTERRUPTED_BY_OTHER

```cangjie
SCREEN_CAPTURE_STATE_INTERRUPTED_BY_OTHER
```

**功能：** 录屏被其他录屏打断。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

### SCREEN_CAPTURE_STATE_INVALID

```cangjie
SCREEN_CAPTURE_STATE_INVALID
```

**功能：** 录屏出现error。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

### SCREEN_CAPTURE_STATE_MIC_MUTED_BY_USER

```cangjie
SCREEN_CAPTURE_STATE_MIC_MUTED_BY_USER
```

**功能：** 麦克风被用户打开。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

### SCREEN_CAPTURE_STATE_MIC_UNAVAILABLE

```cangjie
SCREEN_CAPTURE_STATE_MIC_UNAVAILABLE
```

**功能：** 录屏无法使用麦克风收音。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

### SCREEN_CAPTURE_STATE_MIC_UNMUTED_BY_USER

```cangjie
SCREEN_CAPTURE_STATE_MIC_UNMUTED_BY_USER
```

**功能：** 麦克风被用户关闭。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

### SCREEN_CAPTURE_STATE_STARTED

```cangjie
SCREEN_CAPTURE_STATE_STARTED
```

**功能：** 录屏已开始。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

### SCREEN_CAPTURE_STATE_STOPPED_BY_CALL

```cangjie
SCREEN_CAPTURE_STATE_STOPPED_BY_CALL
```

**功能：** 录屏被来电打断。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

### SCREEN_CAPTURE_STATE_STOPPED_BY_USER

```cangjie
SCREEN_CAPTURE_STATE_STOPPED_BY_USER
```

**功能：** 录屏被用户手动停止。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

### SCREEN_CAPTURE_STATE_STOPPED_BY_USER_SWITCHES

```cangjie
SCREEN_CAPTURE_STATE_STOPPED_BY_USER_SWITCHES
```

**功能：** 系统用户切换，录屏中断。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19