## class Area

```cangjie
public class Area {
    public var width: Length
    public var height: Length
    public var position: Position
    public var globalPosition: Position
    public init(width: Length, height: Length, position: Position, globalPosition: Position)
}
```

**功能：** 当前目标区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var width

```cangjie
public var width: Length
```

**功能：** 定义目标元素的宽度。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var height

```cangjie
public var height: Length
```

**功能：** 定义目标元素的高度。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var position

```cangjie
public var position: Position
```

**功能：** 定义目标元素左上角与父元素左上角的相对位置。

**类型：** [Position](#class-position)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var globalPosition

```cangjie
public var globalPosition: Position
```

**功能：** 定义目标元素左上角与屏幕左上角的位置关系。

**类型：** [Position](#class-position)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(Length, Length, Position, Position)

```cangjie
public init(width: Length, height: Length, position: Position, globalPosition: Position)
```

**功能：** 构造一个Area类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|[Length](./cj-common-types.md#interface-length)|是|-|目标元素的宽度，单位为vp。|
|height|[Length](./cj-common-types.md#interface-length)|是|-|目标元素的高度，单位为vp。|
|position|[Position](#class-position)|是|-|目标元素左上角相对父元素左上角的位置。|
|globalPosition|[Position](#class-position)|是|-|目标元素左上角相对页面左上角的位置。|