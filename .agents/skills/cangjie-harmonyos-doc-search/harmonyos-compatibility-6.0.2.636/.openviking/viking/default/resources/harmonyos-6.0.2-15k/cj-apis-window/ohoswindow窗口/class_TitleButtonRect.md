## class TitleButtonRect

```cangjie
public class TitleButtonRect {
    public TitleButtonRect(
        public var right: Int32,
        public var top: Int32,
        public var width: UInt32,
        public var height: UInt32
    )
}
```

**功能：** 标题栏上的最小化、最大化、关闭按钮矩形区域，该区域位置坐标相对窗口右上角。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 12

### var right

```cangjie
public var right: Int32
```

**功能：** 设置矩形区域的右边界，单位为vp。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var top

```cangjie
public var top: Int32
```

**功能：** 设置矩形区域的上边界，单位为vp。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var width

```cangjie
public var width: UInt32
```

**功能：** 设置矩形区域的宽度，单位为vp。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### var height

```cangjie
public var height: UInt32
```

**功能：** 设置矩形区域的高度，单位为vp。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### TitleButtonRect(Int32, Int32, UInt32, UInt32)

```cangjie
public TitleButtonRect(
    public var right: Int32,
    public var top: Int32,
    public var width: UInt32,
    public var height: UInt32
)
```

**功能：** 构建一个TitleButtonRect类型的对象。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|right|Int32|是|-|矩形区域的右边界，单位为vp。|
|top|Int32|是|-|矩形区域的上边界，单位为vp。|
|width|UInt32|是|-|矩形区域的宽度，单位为vp。|
|height|UInt32|是|-|矩形区域的高度，单位为vp。|