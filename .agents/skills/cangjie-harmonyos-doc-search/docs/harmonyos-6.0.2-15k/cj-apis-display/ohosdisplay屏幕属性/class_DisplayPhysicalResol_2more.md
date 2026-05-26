## class DisplayPhysicalResolution

```cangjie
public class DisplayPhysicalResolution {
    public DisplayPhysicalResolution(
        public let foldDisplayMode: FoldDisplayMode,
        public let physicalWidth: UInt32,
        public let physicalHeight: UInt32
    )
}
```

**功能：** 折叠设备的显示模式以及对应的物理屏幕分辨率信息。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### let foldDisplayMode

```cangjie
public let foldDisplayMode: FoldDisplayMode
```

**功能：** 设置折叠设备的显示模式。

**类型：** [FoldDisplayMode](#enum-folddisplaymode)

**读写能力：** 只读

**起始版本：** 19

### let physicalWidth

```cangjie
public let physicalWidth: UInt32
```

**功能：** 设置折叠设备的宽度。

> **说明：**
>
> 单位为像素，该参数应为整数。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let physicalHeight

```cangjie
public let physicalHeight: UInt32
```

**功能：** 设置折叠设备的高度。

> **说明：**
>
> 单位为像素，该参数应为整数。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### DisplayPhysicalResolution(FoldDisplayMode,UInt32,UInt32)

```cangjie
public DisplayPhysicalResolution(
    public let foldDisplayMode: FoldDisplayMode,
    public let physicalWidth: UInt32,
    public let physicalHeight: UInt32
)
```

**功能：** 创建一个DisplayPhysicalResolution类型的对象。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|foldDisplayMode|[FoldDisplayMode](#enum-folddisplaymode)|是|-|折叠设备的显示模式。|
|physicalWidth|UInt32|是|-|折叠设备的宽度，单位为px，该参数应为大于0的整数。|
|physicalHeight|UInt32|是|-|折叠设备的高度，单位为px，该参数应为大于0的整数。|

## class FoldCreaseRegion

```cangjie
public class FoldCreaseRegion {
    public FoldCreaseRegion(
        public let displayId: UInt32,
        public let creaseRects: Array<Rect>
    )
}
```

**功能：** 折叠折痕区域。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

### let creaseRects

```cangjie
public let creaseRects: Array<Rect>
```

**功能：** 设置折痕区域。

**类型：** Array&lt;[Rect](#class-rect)>

**读写能力：** 只读

**起始版本：** 19

### let displayId

```cangjie
public let displayId: UInt32
```

**功能：** 设置显示器ID，用于识别折痕所在的屏幕。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### FoldCreaseRegion(UInt32,Array&lt;Rect>)

```cangjie
public FoldCreaseRegion(
    public let displayId: UInt32,
    public let creaseRects: Array<Rect>
)
```

**功能：** 创建一个FoldCreaseRegion类型的对象。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|displayId|Array&lt;[Rect](#class-rect)>|是|-|显示器ID，用于识别折痕所在的屏幕。|
|creaseRects|UInt32|是|-|折痕区域。|