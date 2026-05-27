## class WaterfallDisplayAreaRects

```cangjie
public class WaterfallDisplayAreaRects {
    public WaterfallDisplayAreaRects(
        public let left: Rect,
        public let top: Rect,
        public let right: Rect,
        public let bottom: Rect
    )
}
```

**功能：** 瀑布屏曲面部分显示区域信息。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### let bottom

```cangjie
public let bottom: Rect
```

**功能：** 设置瀑布曲面区域底部矩形区域。

**类型：** [Rect](#class-rect)

**读写能力：** 只读

**起始版本：** 19

### let left

```cangjie
public let left: Rect
```

**功能：** 设置瀑布曲面区域的左侧矩形区域。

**类型：** [Rect](#class-rect)

**读写能力：** 只读

**起始版本：** 19

### let right

```cangjie
public let right: Rect
```

**功能：** 设置瀑布曲面区域右侧矩形区域。

**类型：** [Rect](#class-rect)

**读写能力：** 只读

**起始版本：** 19

### let top

```cangjie
public let top: Rect
```

**功能：** 设置瀑布曲面区域的顶部矩形区域。

**类型：** [Rect](#class-rect)

**读写能力：** 只读

**起始版本：** 19

### WaterfallDisplayAreaRects(Rect,Rect,Rect,Rect)

```cangjie
public WaterfallDisplayAreaRects(
    public let left: Rect,
    public let top: Rect,
    public let right: Rect,
    public let bottom: Rect
)
```

**功能：** 创建一个WaterfallDisplayAreaRects类型的对象。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|left|[Rect](#class-rect)|是|-|瀑布曲面区域的左侧矩形区域。|
|top|[Rect](#class-rect)|是|-|瀑布曲面区域的顶部矩形区域。|
|right|[Rect](#class-rect)|是|-|瀑布曲面区域的右侧矩形区域。|
|bottom|[Rect](#class-rect)|是|-|瀑布曲面区域的底部矩形区域。|

## enum Orientation

```cangjie
public enum Orientation {
    | PORTRAIT
    | LANDSCAPE
    | PORTRAIT_INVERTED
    | LANDSCAPE_INVERTED
    | ...
}
```

**功能：** 显示设备当前的显示方向类型。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### LANDSCAPE

```cangjie
LANDSCAPE
```

**功能：** 表示设备当前以横屏方式显示。

**起始版本：** 19

### LANDSCAPE_INVERTED

```cangjie
LANDSCAPE_INVERTED
```

**功能：** 表示设备当前以反向横屏方式显示。

**起始版本：** 19

### PORTRAIT

```cangjie
PORTRAIT
```

**功能：** 表示设备当前以竖屏方式显示。

**起始版本：** 19

### PORTRAIT_INVERTED

```cangjie
PORTRAIT_INVERTED
```

**功能：** 表示设备当前以反向竖屏方式显示。

**起始版本：** 19

## enum DisplayState

```cangjie
public enum DisplayState {
    | STATE_UNKNOWN
    | STATE_OFF
    | STATE_ON
    | STATE_DOZE
    | STATE_DOZE_SUSPEND
    | STATE_VR
    | STATE_ON_SUSPEND
    | ...
}
```

**功能：** 显示设备的状态类型。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### STATE_DOZE

```cangjie
STATE_DOZE
```

**功能：** 表示显示设备为低电耗模式。

**起始版本：** 19

### STATE_DOZE_SUSPEND

```cangjie
STATE_DOZE_SUSPEND
```

**功能：** 表示显示设备为睡眠模式，CPU为挂起状态。

**起始版本：** 19

### STATE_OFF

```cangjie
STATE_OFF
```

**功能：** 表示显示设备状态为关闭。

**起始版本：** 19

### STATE_ON

```cangjie
STATE_ON
```

**功能：** 表示显示设备状态为开启。

**起始版本：** 19

### STATE_ON_SUSPEND

```cangjie
STATE_ON_SUSPEND
```

**功能：** 表示显示设备为开启状态，CPU为挂起状态。

**起始版本：** 19

### STATE_UNKNOWN

```cangjie
STATE_UNKNOWN
```

**功能：** 表示显示设备状态未知。

**起始版本：** 19

### STATE_VR

```cangjie
STATE_VR
```

**功能：** 表示显示设备为VR模式。

**起始版本：** 19