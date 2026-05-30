## class SheetInfo

```cangjie
public class SheetInfo {
    public SheetInfo(
        public var title: String,
        public var action: () -> Unit,
        public var icon!: Option<AppResource> = Option.None
    ) {}
}
```

**功能：** 设置选项内容，每个选择项支持设置图片、文本和选中的回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var action

```cangjie
public var action:() -> Unit
```

**功能：** 选项选中的回调。

**类型：** ()->Unit

**读写能力：** 可读写

**起始版本：** 19

### var icon

```cangjie
public var icon: Option<AppResource> = Option.None
```

**功能：** 选项的图标，默认无图标显示。

**类型：** Option\<[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)>

**读写能力：** 可读写

**起始版本：** 19

### var title

```cangjie
public var title: String
```

**功能：** 选项的文本内容。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### SheetInfo(String, () -> Unit, Option\<AppResource>)

```cangjie
public SheetInfo(
    public var title: String,
    public var action: () -> Unit,
    public var icon!: Option<AppResource> = Option.None
)
```

**功能：** 选项内容参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数:**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| title | String | 是 | \- | 选项的文本内容。<br/>文本超长时会触发滚动条。 |
| action | () -> Unit | 是 | \- | 选项选中的回调。 |
| icon | Option\<[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)> | 否 | Option.None | **命名参数。**  选项的图标，默认无图标显示。<br/>string格式可用于加载网络图片和本地图片，常用于加载网络图片。当使用相对路径引用本地图片时，例如Image("common/test.jpg")。|

## enum DismissReason

```cangjie
public enum DismissReason {
    | PRESS_BACK
    | TOUCH_OUTSIDE
    | CLOSE_BUTTON
    | SLIDE_DOWN
}
```

**功能：** 弹窗关闭原因。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### CLOSE_BUTTON

```cangjie
CLOSE_BUTTON
```

**功能：** 点击了关闭按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### PRESS_BACK

```cangjie
PRESS_BACK
```

**功能：** 点击三键back、左滑/右滑、键盘ESC。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SLIDE_DOWN

```cangjie
SLIDE_DOWN
```

**功能：** 下拉关闭。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### TOUCH_OUTSIDE

```cangjie
TOUCH_OUTSIDE
```

**功能：** 点击遮障层时。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19