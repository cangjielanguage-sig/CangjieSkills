## class Area

```cangjie
public class Area {
    public Area(
        public var width: Float64,
        public var height: Float64,
        public var position: Position,
        public var globalPosition: Position
    )
}
```

**功能：** 当前目标区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var globalPosition

```cangjie
public var globalPosition: Position
```

**功能：** 定义目标元素左上角与屏幕左上角的位置关系。

**类型：** [Position](#class-position)

**读写能力：** 可读写

**起始版本：** 12

### var height

```cangjie
public var height: Float64
```

**功能：** 定义目标元素的宽度。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

### var position

```cangjie
public var position: Position
```

**功能：** 定义目标元素左上角与父元素左上角的相对位置。

**类型：** [Position](#class-position)

**读写能力：** 可读写

**起始版本：** 12

### var width

```cangjie
public var width: Float64
```

**功能：** 定义目标元素的宽度。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

### Area(Float64, Float64, Position, Position)

```cangjie
public Area(
    public var width: Float64,
    public var height: Float64,
    public var position: Position,
    public var globalPosition: Position
)
```

**功能：** 构造一个Area类型的对象。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|Float64|是|-|目标元素的宽度，单位为vp。|
|height|Float64|是|-|目标元素的高度，单位为vp。|
|position|[Position](#class-position)|是|-|目标元素左上角相对父元素左上角的位置。|
|globalPosition|[Position](#class-position)|是|-|目标元素左上角相对页面左上角的位置。|