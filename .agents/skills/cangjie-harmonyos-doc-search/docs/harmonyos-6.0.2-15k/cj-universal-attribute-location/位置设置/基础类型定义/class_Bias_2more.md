### class Bias

```cangjie
public class Bias {
    public Bias(
        public var horizontal!: ?Float32 = None,
        public var vertical!: ?Float32 = None
    )
}
```

**功能：** 设置组件在锚点约束下的偏移参数。其值为到左/上侧锚点的距离与锚点间总距离的比值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var horizontal

```cangjie
public var horizontal: ?Float32 = None
```

**功能：** 水平方向上的bias值。

**类型：** ?Float32

**读写能力：** 可读写

**起始版本：** 12

#### var vertical

```cangjie
public var vertical: ?Float32 = None
```

**功能：** 垂直方向上的bias值。

**类型：** ?Float32

**读写能力：** 可读写

**起始版本：** 12

#### Bias(?Float32, ?Float32)

```cangjie
public Bias(
    public var horizontal!: ?Float32 = None,
    public var vertical!: ?Float32 = None
)
```

**功能：** 创建一个Bias对象。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|horizontal|?Float32|否|None| **命名参数。** 水平方向上的bias值。当子组件的width属性有正确值并且有2个水平方向的锚点时生效。<br> 初始值：0.5。|
|vertical|?Float32|否|None| **命名参数。** 垂直方向上的bias值。当子组件的height属性有正确值并且有2个垂直方向的锚点时生效。<br> 初始值：0.5。|

### class HorizontalAnchor

```cangjie
public class HorizontalAnchor {
    public HorizontalAnchor (
        public var anchor: String,
        public var align: HorizontalAlign
    )
}
```

**功能：** 设置水平对齐参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var align

```cangjie
public var align: HorizontalAlign
```

**功能：** 设置相对于锚点组件的对齐方式。

**类型：** [HorizontalAlign](./cj-common-types.md#enum-horizontalalign)

**读写能力：** 可读写

**起始版本：** 12

#### var anchor

```cangjie
public var anchor: String
```

**功能：** 设置作为锚点的组件的id值。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

#### HorizontalAnchor(String, HorizontalAlign)

```cangjie
public HorizontalAnchor (
    public var anchor: String,
    public var align: HorizontalAlign
)
```

**功能：** 创建HorizontalAnchor对象。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|anchor|String|是|-|作为锚点的组件的id值。|
|align|[HorizontalAlign](./cj-common-types.md#enum-horizontalalign)|是|-|相对于锚点组件的对齐方式。|