### class EditMenuOptions

```cangjie
public class EditMenuOptions {
    public var onCreateMenu: (Array<TextMenuItem>) -> Array<TextMenuItem>
    public var onMenuClick: (TextMenuItem, TextRange) -> Bool
    public init(
        onCreateMenu: (Array<TextMenuItem>) -> Array<TextMenuItem>,
        onMenuClick: (TextMenuItem, TextRange) -> Bool
    )
}
```

**功能：** 扩展菜单选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### var onCreateMenu

```cangjie
public var onCreateMenu: (Array<TextMenuItem>) -> Array<TextMenuItem>
```

**功能：** 菜单数据模版编辑能力。创建菜单时触发该回调函数。

**类型：** (Array<[TextMenuItem](./cj-text-input-text.md#class-textmenuitem)>) -> Array<[TextMenuItem](./cj-text-input-text.md#class-textmenuitem)>

**读写能力：** 可读写

**起始版本：** 20

#### var onMenuClick

```cangjie
public var onMenuClick: (TextMenuItem, TextRange) -> Bool
```

**功能：** 菜单项功能函数。点击菜单项时触发该回调函数。

**类型：** ([TextMenuItem](./cj-text-input-text.md#class-textmenuitem), [TextRange](#class-textrange)) -> Bool

**读写能力：** 可读写

**起始版本：** 20

#### init((Array\<TextMenuItem>) -> Array\<TextMenuItem>, (TextMenuItem, TextRange) -> Bool)

```cangjie
public init(
        onCreateMenu: (Array<TextMenuItem>) -> Array<TextMenuItem>,
        onMenuClick: (TextMenuItem, TextRange) -> Bool
    )
```

**功能：** 创建EditMenuOptions类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onCreateMenu|(Array<[TextMenuItem](./cj-text-input-text.md#class-textmenuitem)>) -> Array<[TextMenuItem](./cj-text-input-text.md#class-textmenuitem)>|是|-|菜单数据模版编辑能力。创建菜单时触发该回调函数。|
|onMenuClick|([TextMenuItem](./cj-text-input-text.md#class-textmenuitem), [TextRange](#class-textrange)) -> Bool|是|-|菜单项功能函数。点击菜单项时触发该回调函数。|