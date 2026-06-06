## class PickInfo

```cangjie
public class PickInfo {
    public PickInfo(
        public let pickRect: Rect,
        public let pixelMap: PixelMap
    )
}
```

**功能：** 截取图像的信息。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### let pickRect

```cangjie
public let pickRect: Rect
```

**功能：** 表示截取图像的区域。

**类型：** [Rect](#class-rect)

**读写能力：** 只读

**起始版本：** 19

### let pixelMap

```cangjie
public let pixelMap: PixelMap
```

**功能：** 表示截取的图像PixelMap对象。

**类型：** [PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)

**读写能力：** 只读

**起始版本：** 19

### PickInfo(Rect, PixelMap)

```cangjie
public PickInfo(
    public let pickRect: Rect,
    public let pixelMap: PixelMap
)
```

**功能：** 创建一个PickInfo类型的对象。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pickRect|[Rect](#class-rect)|是|-|表示截取图像的区域。|
|pixelMap|[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)|是|-|表示截取的图像PixelMap对象|

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

**功能：** 表示截取图像的区域。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### var left

```cangjie
public var left: Int32
```

**功能：** 表示截取图像区域的左边界，单位为px。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var top

```cangjie
public var top: Int32
```

**功能：** 表示截取图像区域的上边界，单位为px。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var width

```cangjie
public var width: UInt32
```

**功能：** 表示截取图像区域的宽度，单位为px。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### var height

```cangjie
public var height: UInt32
```

**功能：** 表示截取图像区域的高度，单位为px。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### Rect(Int32, Int32, UInt32, UInt32)

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
|left|Int32|是|-|表示截取图像区域的左边界，单位为px。|
|top|Int32|是|-|表示截取图像区域的上边界，单位为px。|
|width|UInt32|是|-|表示截取图像区域的宽度，单位为px。|
|height|UInt32|是|-|表示截取图像区域的高度，单位为px。|