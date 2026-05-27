## class CutoutInfo

```cangjie
public class CutoutInfo {
    public CutoutInfo(
        public let boundingRects: Array<Rect>,
        public let waterfallDisplayAreaRects: WaterfallDisplayAreaRects
    )
}
```

**功能：** 挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### let boudingRects

```cangjie
public let boundingRects: Array<Rect>
```

**功能：** 设置挖孔、刘海等区域的边界矩形。

> **说明：**
>
> 如果没有挖孔、刘海等区域，数组返回为空。

**类型：** Array\<[Rect](#class-rect)>

**读写能力：** 只读

**起始版本：** 19

### let waterfallDisplayAreaRects

```cangjie
public let waterfallDisplayAreaRects: WaterfallDisplayAreaRects
```

**功能：** 设置瀑布屏曲面部分显示区域。

**类型：** [WaterfallDisplayAreaRects](#class-waterfalldisplayarearects)

**读写能力：** 只读

**起始版本：** 19

### CutoutInfo(Array\<Rect>,WaterfallDisplayAreaRects)

```cangjie
public CutoutInfo(
    public let boundingRects: Array<Rect>,
    public let waterfallDisplayAreaRects: WaterfallDisplayAreaRects
)
```

**功能：** 创建一个CutoutInfo类型对象。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|boundingRects|Array\<[Rect](#class-rect)>|是|-|挖孔、刘海等区域的边界矩形。如果没有挖孔、刘海等区域，数组返回为空。|
|waterfallDisplayAreaRects|[WaterfallDisplayAreaRects](#class-waterfalldisplayarearects)|是|-|瀑布屏曲面部分显示区域。|

## class Rect

```cangjie
public class Rect {
    public Rect(
        public var left: Int32,
        public var top: Int32,
        public var width: UInt32,
        public var height: UInt32
    )
}
```

**功能：** 矩形区域信息。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### var height

```cangjie
public var height: UInt32
```

**功能：** 设置矩形区域的高度。

> **说明：**
>
> 单位为像素，该参数应为整数。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### var left

```cangjie
public var left: Int32
```

**功能：** 设置矩形区域的左边界。

> **说明：**
>
> 单位为像素，该参数应为整数。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var top

```cangjie
public var top: Int32
```

**功能：** 设置矩形区域的上边界。

> **说明：**
>
> 单位为像素，该参数应为整数。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var width

```cangjie
public var width: UInt32
```

**功能：** 设置矩形区域的宽度。

> **说明：**
>
> 单位为像素，该参数应为整数。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### Rect(Int32,Int32,Int32,Int32)

```cangjie
public Rect(
    public var left: Int32,
    public var top: Int32,
    public var width: UInt32,
    public var height: UInt32
)
```

**功能：** 创建一个Rect类型的对象。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|left|Int32|是|-|矩形区域的左边界，单位为px，该参数应为整数。|
|top|Int32|是|-|矩形区域的上边界，单位为px，该参数应为整数。|
|width|Int32|是|-|矩形区域的宽度，单位为px，该参数应为整数。|
|height|Int32|是|-|矩形区域的高度，单位为px，该参数应为整数。|