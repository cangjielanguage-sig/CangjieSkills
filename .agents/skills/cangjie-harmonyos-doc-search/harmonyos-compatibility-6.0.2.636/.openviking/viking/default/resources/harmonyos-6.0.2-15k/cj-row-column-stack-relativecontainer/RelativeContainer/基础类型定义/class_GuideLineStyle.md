### class GuideLineStyle

```cangjie
public class GuideLineStyle {
    public GuideLineStyle (
        public var id: String,
        public var direction: Axis,
        public var position: GuideLinePosition
    )
}
```

**功能：** guideLine参数，用于定义一条guideline的id、方向和位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var direction

```cangjie
public var direction: Axis
```

**功能：** 指定guideline的方向。垂直方向的guideline仅能作为组件水平方向的锚点，作为垂直方向的锚点时值为0；水平方向的guideline仅能作为组件垂直方向的锚点，作为水平方向的锚点时值为0。

**类型：** [Axis](cj-common-types.md#enum-axis)

**读写能力：** 可读写

**起始版本：** 12

#### var id

```cangjie
public var id: String
```

**功能：** guideline的id，必须是唯一的并且不可与容器内组件重名。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

#### var position

```cangjie
public var position: GuideLinePosition
```

**功能：** 指定guideline的位置。当未声明或声明异常值（如undefined）时，guideline的位置默认为start: 0。start和 end两种声明方式选择一种即可。若同时声明，仅start生效。若容器在某个方向的size被声明为"auto"，则该方向上guideline的位置只能使用start方式声明（不允许使用百分比）。

**类型：** [GuideLinePosition](#class-guidelineposition)

**读写能力：** 可读写

**起始版本：** 12

#### GuideLineStyle(String, Axis, GuideLinePosition)

```cangjie
public GuideLineStyle (
    public var id: String,
    public var direction: Axis,
    public var position: GuideLinePosition
)
```

**功能：** 创建一个GuideLineStyle类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|String|是|-|guideline的id，必须是唯一的并且不可与容器内组件重名。|
|direction|[Axis](cj-common-types.md#enum-axis)|是|-|指定guideline的方向。<br>垂直方向的guideline仅能作为组件水平方向的锚点，作为垂直方向的锚点时值为0；水平方向的guideline仅能作为组件垂直方向的锚点，作为水平方向的锚点时值为0。<br> 初始值：Axis.Vertical|
|position|[GuideLinePosition](#class-guidelineposition)|是|-|指定guideline的位置。当未声明或声明异常值时，guideline的位置初始值为start: 0。start和end两种声明方式选择一种即可。若同时声明，仅start生效。<br> 初始值：{start: 0}|