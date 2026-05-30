### class DragInteractionOptions

```cangjie
public class DragInteractionOptions {
    public DragInteractionOptions(
        public let isMultiSelectionEnabled!: Bool = false,
        public let defaultAnimationBeforeLifting!: Bool = false
    )
}
```

**功能：** 拖拽过程中的效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let isMultiSelectionEnabled

```cangjie
public let isMultiSelectionEnabled: Bool = false
```

**功能：** 表示拖拽过程中背板图是否支持多选聚拢效果。true表示支持多选聚拢效果，false表示不支持多选聚拢效果。该参数只在[Grid](./cj-scroll-swipe-grid.md)和[List](./cj-scroll-swipe-list.md)组件中的[GridItem](./cj-scroll-swipe-griditem.md)组件和[ListItem](./cj-scroll-swipe-listitem.md)组件生效。<br>当一个item组件设置为多选拖拽时，该组件的子组件不可拖拽。聚拢组件预览图设置的优先级为[dragPreview](./cj-universal-attribute-dragcontrol.md#func-dragpreview---unit)中的string，组件自截图，不支持dragPreview中的Builder形式。<br>不支持组件绑定[bindContextMenu](./cj-universal-attribute-menu.md#func-bindcontextmenu---unit-responsetype)中参数存在isShown的模式。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

#### let defaultAnimationBeforeLifting

```cangjie
public let defaultAnimationBeforeLifting: Bool = false
```

**功能：** 表示是否启用长按浮起阶段组件自身的默认点按效果（缩小）。true表示启用默认点按效果，false表示不启用默认点按效果。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

#### DragInteractionOptions(Bool, Bool)

```cangjie
public DragInteractionOptions(public let isMultiSelectionEnabled!: Bool = false, public let defaultAnimationBeforeLifting!: Bool = false)
```

**功能：** 构造DragInteractionOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isMultiSelectionEnabled|Bool|否|false| **命名参数。** 表示拖拽过程中背板图是否支持多选聚拢效果。true表示支持多选聚拢效果，false表示不支持多选聚拢效果。该参数只在[Grid](./cj-scroll-swipe-grid.md)和[List](./cj-scroll-swipe-list.md)组件中的[GridItem](./cj-scroll-swipe-griditem.md)组件和[ListItem](./cj-scroll-swipe-listitem.md)组件生效。<br>当一个item组件设置为多选拖拽时，该组件的子组件不可拖拽。聚拢组件预览图设置的优先级为[dragPreview](./cj-universal-attribute-dragcontrol.md#func-dragpreview---unit)中的string，组件自截图，不支持dragPreview中的Builder形式。<br>不支持组件绑定[bindContextMenu](./cj-universal-attribute-menu.md#func-bindcontextmenu---unit-responsetype)中参数存在isShown的模式。|
|defaultAnimationBeforeLifting|Bool|否|false| **命名参数。** 表示是否启用长按浮起阶段组件自身的默认点按效果（缩小）。true表示启用默认点按效果，false表示不启用默认点按效果。|