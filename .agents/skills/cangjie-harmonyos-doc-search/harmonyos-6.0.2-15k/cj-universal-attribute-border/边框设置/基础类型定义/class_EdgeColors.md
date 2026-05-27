### class EdgeColors

```cangjie
public class EdgeColors {
    public var bottom: Option<ResourceColor>
    public var left: Option<ResourceColor>
    public var top: Option<ResourceColor>
    public var right: Option<ResourceColor>
    public init(
        bottom!: Option<ResourceColor> = Option.None,
        left!: Option<ResourceColor> = Option.None,
        top!: Option<ResourceColor> = Option.None,
        right!: Option<ResourceColor> = Option.None
    )
}
```

**功能：** 边框颜色类型，用于描述组件边框不同方向的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var bottom

```cangjie
public var bottom: Option<ResourceColor>
```

**功能：** 下侧边框颜色。

**类型：** Option\<[ResourceColor](./cj-common-types.md#interface-resourcecolor)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var left

```cangjie
public var left: Option<ResourceColor>
```

**功能：** 左侧边框颜色。

**类型：** Option\<[ResourceColor](./cj-common-types.md#interface-resourcecolor)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var right

```cangjie
public var right: Option<ResourceColor>
```

**功能：** 右侧边框颜色。

**类型：** Option\<[ResourceColor](./cj-common-types.md#interface-resourcecolor)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var top

```cangjie
public var top: Option<ResourceColor>
```

**功能：** 上侧边框颜色。

**类型：** Option\<[ResourceColor](./cj-common-types.md#interface-resourcecolor)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Option\<ResourceColor>, Option\<ResourceColor>, Option\<ResourceColor>, Option\<ResourceColor>)

```cangjie
public init(top!: Option<ResourceColor> = Option.None, right!: Option<ResourceColor> = Option.None, bottom!: Option<ResourceColor> = Option.None, left!: Option<ResourceColor> = Option.None)
```

**功能：** 构造一个EdgeColors类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
| :------- | :---------- | :---------- | :------- | :------ |
| top |Option\<[ResourceColor](./cj-common-types.md#interface-resourcecolor)>| 否 | Option.None| **命名参数。**  上侧边框宽度。|
| right |Option\<[ResourceColor](./cj-common-types.md#interface-resourcecolor)>| 否 | Option.None| **命名参数。**  右侧边框宽度。|
| bottom |Option\<[ResourceColor](./cj-common-types.md#interface-resourcecolor)>| 否 | Option.None| **命名参数。**  下侧边框宽度。|
| left |Option\<[ResourceColor](./cj-common-types.md#interface-resourcecolor)>| 否 | Option.None| **命名参数。**  左侧边框宽度。|