## class WaterfallDisplayAreaRects

```cangjie
public class WaterfallDisplayAreaRects {
    public let left: Rect
    public let top: Rect
    public let right: Rect
    public let bottom: Rect
    public init(
    left!: Rect,
    top!: Rect,
    right!: Rect,
    bottom!: Rect
    )
}
```

**功能：** 瀑布屏的弯曲区域矩形。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### let bottom

```cangjie
public let bottom: Rect
```

**功能：** 瀑布屏底部弯曲区域的大小。

**类型：** [Rect](#class-rect)

**读写能力：** 只读

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### let left

```cangjie
public let left: Rect
```

**功能：** 瀑布屏左侧弯曲区域的大小。

**类型：** [Rect](#class-rect)

**读写能力：** 只读

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### let right

```cangjie
public let right: Rect
```

**功能：** 瀑布屏右侧弯曲区域的大小。

**类型：** [Rect](#class-rect)

**读写能力：** 只读

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### let top

```cangjie
public let top: Rect
```

**功能：** 瀑布屏顶部弯曲区域的大小。

**类型：** [Rect](#class-rect)

**读写能力：** 只读

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### init(Rect, Rect, Rect, Rect)

```cangjie
public init(
    left!: Rect,
    top!: Rect,
    right!: Rect,
    bottom!: Rect
)
```

**功能：** WaterfallDisplayAreaRects构造函数。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|left|[Rect](#class-rect)|是|-| **命名参数。** 左侧弯曲区域。|
|top|[Rect](#class-rect)|是|-| **命名参数。** 顶部弯曲区域。|
|right|[Rect](#class-rect)|是|-| **命名参数。** 右侧弯曲区域。|
|bottom|[Rect](#class-rect)|是|-| **命名参数。** 底部弯曲区域。|