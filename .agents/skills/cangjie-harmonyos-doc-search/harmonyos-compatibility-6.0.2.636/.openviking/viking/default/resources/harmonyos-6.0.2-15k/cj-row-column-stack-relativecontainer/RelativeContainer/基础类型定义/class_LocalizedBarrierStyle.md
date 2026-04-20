### class LocalizedBarrierStyle

```cangjie
public class LocalizedBarrierStyle {
    public LocalizedBarrierStyle(
        public var id: String,
        public var localizedDirection: LocalizedBarrierDirection,
        public var referencedId: Array<String>
    )
}
```

**功能：** barrier参数，用于定义一条barrier的id、方向和生成时所依赖的组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var id

```cangjie
public var id: String
```

**功能：** barrier的id，必须是唯一的并且不可与容器内组件重名。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

#### var localizedDirection

```cangjie
public var localizedDirection: LocalizedBarrierDirection
```

**功能：** 指定barrier的方向。

垂直方向（TOP，BOTTOM）的barrier仅能作为组件的水平方向锚点，作为垂直方向锚点时值为0。水平方向（START，END）的barrier仅能作为组件的垂直方向锚点，作为水平方向锚点时值为0。

**类型：** [LocalizedBarrierDirection](#enmu-localizedbarrierdirection)

**读写能力：** 可读写

**起始版本：** 19

#### var referencedId

```cangjie
public var referencedId: Array<String>
```

**功能：** 指定生成barrier所依赖的组件。

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 19

#### LocalizedBarrierStyle(String, LocalizedBarrierDirection, Array\<String>)

```cangjie
public LocalizedBarrierStyle(
    public var id: String,
    public var localizedDirection: LocalizedBarrierDirection,
    public var referencedId: Array<String>
)
```

**功能：** 创建一个LocalizedBarrierStyle类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|String|是|-|barrier的id，必须是唯一的并且不可与容器内组件重名。|
|localizedDirection|[LocalizedBarrierDirection](#enmu-localizedbarrierdirection)|是|-|指定barrier的方向。<br> 垂直方向（TOP，BOTTOM）的barrier仅能作为组件的水平方向锚点，作为垂直方向锚点时值为0。水平方向（START，END）的barrier仅能作为组件的垂直方向锚点，作为水平方向锚点时值为0。|
|referencedId|Array\<String>|是|-|指定生成barrier所依赖的组件。|