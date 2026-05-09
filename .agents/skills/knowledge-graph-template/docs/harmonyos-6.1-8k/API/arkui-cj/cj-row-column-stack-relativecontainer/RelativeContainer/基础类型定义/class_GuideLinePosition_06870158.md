### class GuideLinePosition

```cangjie
public class GuideLinePosition {
    public var start: ?Length
    public var end: ?Length
    public init(start!: ?Length = None, end!: ?Length = None)
}
```

**功能：** guideLine位置参数，用于定义guideline的位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var start

```cangjie
public var start: ?Length
```

**功能：** guideline距离容器左侧或者顶部的距离。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var end

```cangjie
public var end: ?Length
```

**功能：** guideline距离容器右侧或者底部的距离。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?Length, ?Length)

```cangjie
public init(start!: ?Length = None, end!: ?Length = None)
```

**功能：** 创建一个GuideLinePosition类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|start|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** guideline距离容器左侧或者顶部的距离。|
|end|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** guideline距离容器右侧或者底部的距离。|