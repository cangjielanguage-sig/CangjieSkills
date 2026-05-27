### class GuideLinePosition

```cangjie
public class GuideLinePosition {
    public GuideLinePosition(
        public var start!: ?Length = None,
        public var end!: ?Length = None
    )
}
```

**功能：** guideLine位置参数，用于定义guideline的位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var end

```cangjie
public var end: ?Length = None
```

**功能：** guideline距离容器右侧或者底部的距离。

**类型：** ?[Length](cj-common-types.md#interface-Length)

**读写能力：** 可读写

**起始版本：** 12

#### var start

```cangjie
public var start: ?Length = None
```

**功能：** guideline距离容器左侧或者顶部的距离。

**类型：** ?[Length](cj-common-types.md#interface-Length)

**读写能力：** 可读写

**起始版本：** 12

#### GuideLinePosition(?Length, ?Length)

```cangjie
public GuideLinePosition(
    public var start!: ?Length = None,
    public var end!: ?Length = None
)
```

**功能：** 创建一个GuideLinePosition类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|start|?[Length](cj-common-types.md#interface-Length)|否|None| **命名参数。** guideline距离容器左侧或者顶部的距离。|
|end|?[Length](cj-common-types.md#interface-Length)|否|None| **命名参数。** guideline距离容器右侧或者底部的距离。|