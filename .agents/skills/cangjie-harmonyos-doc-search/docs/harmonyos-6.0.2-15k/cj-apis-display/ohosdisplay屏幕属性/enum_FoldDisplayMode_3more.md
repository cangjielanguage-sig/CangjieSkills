## enum FoldDisplayMode

```cangjie
public enum FoldDisplayMode {
    | FOLD_DISPLAY_MODE_UNKNOWN
    | FOLD_DISPLAY_MODE_FULL
    | FOLD_DISPLAY_MODE_MAIN
    | FOLD_DISPLAY_MODE_SUB
    | FOLD_DISPLAY_MODE_COORDINATION
    | ...
}
```

**功能：** 可折叠设备的显示模式类型。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

### FOLD_DISPLAY_MODE_COORDINATION

```cangjie
FOLD_DISPLAY_MODE_COORDINATION
```

**功能：** 表示设备当前双屏协同显示。

**起始版本：** 19

### FOLD_DISPLAY_MODE_FULL

```cangjie
FOLD_DISPLAY_MODE_FULL
```

**功能：** 表示设备当前全屏显示。

**起始版本：** 19

### FOLD_DISPLAY_MODE_MAIN

```cangjie
FOLD_DISPLAY_MODE_MAIN
```

**功能：** 表示设备当前主屏幕显示。

**起始版本：** 19

### FOLD_DISPLAY_MODE_SUB

```cangjie
FOLD_DISPLAY_MODE_SUB
```

**功能：** 表示设备当前子屏幕显示。

**起始版本：** 19

### FOLD_DISPLAY_MODE_UNKNOWN

```cangjie
FOLD_DISPLAY_MODE_UNKNOWN
```

**功能：** 表示设备当前折叠显示模式未知。

**起始版本：** 19

## enum FoldStatus

```cangjie
public enum FoldStatus {
    | FOLD_STATUS_UNKNOWN
    | FOLD_STATUS_EXPANDED
    | FOLD_STATUS_FOLDED
    | FOLD_STATUS_HALF_FOLDED
    | ...
}
```

**功能：** 当前可折叠设备的折叠状态类型。

> **说明：**
>
> 如果是双折轴设备，则在充电口朝下的状态下，从右到左分别是折轴一和折轴二。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

### FOLD_STATUS_EXPANDED

```cangjie
FOLD_STATUS_EXPANDED
```

**功能：** 表示设备当前折叠状态为完全展开。如果是双折轴设备，则表示折轴一折叠状态为完全展开，折轴二折叠状态为折叠。

**起始版本：** 19

### FOLD_STATUS_FOLDED

```cangjie
FOLD_STATUS_FOLDED
```

**功能：** 表示设备当前折叠状态为折叠。如果是双折轴设备，则表示折轴一折叠状态为折叠，折轴二折叠状态为折叠。

**起始版本：** 19

### FOLD_STATUS_HALF_FOLDED

```cangjie
FOLD_STATUS_HALF_FOLDED
```

**功能：** 表示设备当前折叠状态为半折叠。半折叠指完全展开和折叠之间的状态。如果是双折轴设备，则表示折轴一折叠状态为半折叠，折轴二折叠状态为折叠。

**起始版本：** 19

### FOLD_STATUS_UNKNOWN

```cangjie
FOLD_STATUS_UNKNOWN
```

**功能：** 表示设备当前折叠状态未知。

**起始版本：** 19

## enum HDRFormat

```cangjie
public enum HDRFormat {
    | NONE
    | VIDEO_HLG
    | VIDEO_HDR10
    | VIDEO_HDR_VIVID
    | IMAGE_HDR_VIVID_DUAL
    | IMAGE_HDR_VIVID_SINGLE
    | IMAGE_HDR_ISO_DUAL
    | IMAGE_HDR_ISO_SINGLE
    | ...
}
```

**功能：** HDR格式类型。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 19

### IMAGE_HDR_ISO_DUAL

```cangjie
IMAGE_HDR_ISO_DUAL
```

**功能：** 设置支持图片的HDR_ISO格式，以dual JPEG格式存储。

**起始版本：** 19

### IMAGE_HDR_ISO_SINGLE

```cangjie
IMAGE_HDR_ISO_SINGLE
```

**功能：** 设置支持图片的HDR_ISO格式，以single HEIF格式存储。

**起始版本：** 19

### IMAGE_HDR_VIVID_DUAL

```cangjie
IMAGE_HDR_VIVID_DUAL
```

**功能：** 设置支持图片的HDR_VIVID格式，以dual JPEG格式存储。

**起始版本：** 19

### IMAGE_HDR_VIVID_SINGLE

```cangjie
IMAGE_HDR_VIVID_SINGLE
```

**功能：** 设置支持图片的HDR_VIVID格式，以single HEIF格式存储。

**起始版本：** 19

### NONE

```cangjie
NONE
```

**功能：** 设置不支持HDR类型。

**起始版本：** 19

### VIDEO_HDR10

```cangjie
VIDEO_HDR10
```

**功能：** 设置支持视频的HDR10格式。

**起始版本：** 19

### VIDEO_HLG

```cangjie
VIDEO_HLG
```

**功能：** 设置支持视频的HLG格式。

**起始版本：** 19

### VIDEO_HDR_VIVID

```cangjie
VIDEO_HDR_VIVID
```

**功能：** 设置支持视频的HDR_VIVID格式。

**起始版本：** 19