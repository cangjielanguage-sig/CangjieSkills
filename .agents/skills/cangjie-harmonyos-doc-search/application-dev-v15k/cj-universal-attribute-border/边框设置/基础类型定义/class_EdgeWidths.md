### class EdgeWidths

```cangjie
public class EdgeWidths {
    public var top: Length
    public var right: Length
    public var bottom: Length
    public var left: Length
    public init(top!: Length = 0.vp, right!: Length = 0.vp, bottom!: Length = 0.vp, left!: Length = 0.vp)
}
```

**功能：** 设置弹窗背板的边框宽度。引入该对象时，至少传入一个参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var top

```cangjie
public var top: Length
```

**功能：** 上侧边框宽度。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var right

```cangjie
public var right: Length
```

**功能：** 右侧边框宽度。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var left

```cangjie
public var left: Length
```

**功能：** 左侧边框宽度。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var bottom

```cangjie
public var bottom: Length
```

**功能：** 下侧边框宽度。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(left!: Length = 0.vp, right!: Length = 0.vp, top!: Length = 0.vp, bottom!: Length = 0.vp)

```cangjie
public init(left!: Length = 0.vp, right!: Length = 0.vp, top!: Length = 0.vp, bottom!: Length = 0.vp)
```

**功能：** 构造EdgeWidths对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :--- | :--- | :--- | :--- |:--- |
| left | [Length](./cj-common-types.md#interface-length)  | 否 | 0.vp | **命名参数。**  左侧边框宽度。 |
| right | [Length](./cj-common-types.md#interface-length)  | 否 | 0.vp | **命名参数。** 右侧边框宽度。 |
| top | [Length](./cj-common-types.md#interface-length)  | 否 | 0.vp | **命名参数。** 上侧边框宽度。 |
| bottom | [Length](./cj-common-types.md#interface-length)  | 否 | 0.vp | **命名参数。** 下侧边框宽度。 |