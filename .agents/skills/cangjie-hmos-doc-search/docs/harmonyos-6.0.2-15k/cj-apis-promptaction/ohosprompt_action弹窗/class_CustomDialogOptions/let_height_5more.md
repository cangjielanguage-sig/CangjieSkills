### let height

```cangjie
public let height: Length = 100.vp
```

**功能：** 表示弹窗背板的高度。

> **说明：**
>
> 百分比参数方式：弹窗参考高度为（窗口高度 - 安全区域），在此基础上调小或调大。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let shadowOption

```cangjie
public let shadowOption: Option<ShadowOptions> = None
```

**功能：** 表示弹窗背板阴影。

> **说明：**
>
> - 与shadowStyle联合使用。设置shadowOption为非None时，shadowOption设置值生效。
> - shadowOption与shadowStyle均设置为None时，使用默认值ShadowStyle.OUTER_DEFAULT_MD。

**类型：** Option\<[ShadowOptions](./cj-text-input-text.md#class-shadowoptions)>

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let shadowStyle

```cangjie
public let shadowStyle: Option<ShadowStyle> = None
```

**功能：** 表示弹窗背板阴影。

> **说明：**
>
> - 与shadowOption联合使用。设置shadowOption为None时，shadowStyle设置值生效。
> - shadowOption与shadowStyle均设置为None时，使用默认值ShadowStyle.OUTER_DEFAULT_MD。

**类型：** Option\<[ShadowStyle](#enum-shadowstyle)>

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let backgroundBlurStyle

```cangjie
public let backgroundBlurStyle: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK
```

**功能：** 表示弹窗背板模糊材质。

> **说明：**
>
> - 设置为BlurStyle.NONE即可关闭背景虚化。
> - 当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。

**类型：** [BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### init(Rectangle, DialogAlignment, Offset, Bool, Bool, ()-> Unit)

```cangjie
public init(
    maskRect!: Rectangle = Rectangle(x: 0.vp, y: 0.vp, width: 100.percent, height: 100.percent),
    alignment!: DialogAlignment = DialogAlignment.Default,
    offset!: Offset = Offset(0.vp, 0.vp),
    isModal!: Bool = true,
    showInSubWindow!: Bool = false,
    builder!: ()-> Unit
)
```

**功能：** CustomDialogOptions构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|maskRect|[Rectangle](./cj-common-types.md#class-rectangle)|否|Rectangle(x: 0.vp, y: 0.vp, width: 100.percent, height: 100.percent)| **命名参数。** 弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。<br>**说明：**<br> - showInSubWindow为true时，maskRect不生效。<br> - maskRect在设置部分属性值后，其余属性值默认为0。|
|alignment|[DialogAlignment](./cj-common-types.md#enum-dialogalignment)|否|DialogAlignment.Default| **命名参数。** 弹窗在竖直方向上的对齐方式。|
|offset|[Offset](./cj-common-types.md#class-offset)|否|Offset(0.vp, 0.vp)| **命名参数。** 弹窗相对alignment所在位置的偏移量。|
|isModal|Bool|否|true| **命名参数。** 弹窗是否为模态窗口，模态窗口有蒙层，非模态窗口无蒙层。默认弹窗有蒙层。|
|builder|()->Unit|否|-| **命名参数。** 设置自定义弹窗的内容。<br>**说明：**<br> 使用时结合[@Builder](../../../Dev_Guide/arkui-cj/paradigm/cj-macro-builder.md)和[bind](./cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。如果是全局builder需要在组件内部创建一个builder，在内部builder中调用全局builder。builder根节点宽高百分比相对弹框容器大小。builder非根节点宽高百分比相对父节点大小。|