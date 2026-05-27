## class AvoidArea

```cangjie
public class AvoidArea {
    public AvoidArea (
        public var visible: Bool,
        public var leftRect: Rect,
        public var topRect: Rect,
        public var rightRect: Rect,
        public var bottomRect: Rect
    )
}
```

**功能：** 窗口内容规避区域。

> **说明：**
>
> 如系统栏区域、刘海屏区域、手势区域、软键盘区域等与窗口内容重叠时，需要窗口内容避让的区域。在规避区无法响应用户点击事件。
>
> 除此之外还需注意规避区域的如下约束，具体为：
>
> - 底部手势区域中非导航条区域支持点击、长按事件透传，不支持拖入。
> - 左右侧边手势区域支持点击、长按以及上下滑动事件透传，不支持拖入。
> - 导航条区域支持长按、点击、拖入事件响应，不支持事件向下透传。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### var bottomRect

```cangjie
public var bottomRect: Rect
```

**功能：** 表示屏幕底部的矩形区。

**类型：** [Rect](#class-rect)

**读写能力：** 可读写

**起始版本：** 19

### var leftRect

```cangjie
public var leftRect: Rect
```

**功能：** 表示屏幕左侧的矩形区。

**类型：** [Rect](#class-rect)

**读写能力：** 可读写

**起始版本：** 19

### var rightRect

```cangjie
public var rightRect: Rect
```

**功能：** 表示屏幕右侧的矩形区。

**类型：** [Rect](#class-rect)

**读写能力：** 可读写

**起始版本：** 19

### var topRect

```cangjie
public var topRect: Rect
```

**功能：** 表示屏幕顶部的矩形区。

**类型：** [Rect](#class-rect)

**读写能力：** 可读写

**起始版本：** 19

### var visible

```cangjie
public var visible: Bool
```

**功能：** 表示规避区域是否可见。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### AvoidArea(Bool, Rect, Rect, Rect, Rect)

```cangjie
public AvoidArea (
    public var visible: Bool,
    public var leftRect: Rect,
    public var topRect: Rect,
    public var rightRect: Rect,
    public var bottomRect: Rect
)
```

**功能：** 构建一个AvoidArea类型的对象。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|visible|Bool|是|-|规避区域是否可见。true表示可见；false表示不可见。|
|leftRect|[Rect](#class-rect)|是|-|屏幕左侧的矩形区。|
|topRect|[Rect](#class-rect)|是|-|屏幕顶部的矩形区。|
|rightRect|[Rect](#class-rect)|是|-|屏幕右侧的矩形区。|
|bottomRect|[Rect](#class-rect)|是|-|屏幕底部的矩形区。|