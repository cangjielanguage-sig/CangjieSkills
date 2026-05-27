### class RichEditorImageSpanOptions

```cangjie
public class RichEditorImageSpanOptions {
    public var offset: Int32
    public var imageStyle: RichEditorImageSpanStyle
    public init(offset!: Int32 = Int32.Max, imageStyle!: RichEditorImageSpanStyle = RichEditorImageSpanStyle())
}
```

**功能：** 表示添加图片的偏移位置和图片样式信息的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var offset

```cangjie
public var offset: Int32
```

**功能：** 表示添加图片的位置。省略时，添加到所有内容的最后。

> **说明：**
>
> 当值小于0时，放在所有内容最前面；当值大于所有内容长度时，放在所有内容最后面。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var imageStyle

```cangjie
public var imageStyle: RichEditorImageSpanStyle
```

**功能：** 表示图片样式信息的类型。省略时，使用系统默认图片信息。

**类型：** [RichEditorImageSpanStyle](#class-richeditorimagespanstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(Int32, RichEditorImageSpanStyle)

```cangjie
public init(offset!: Int32 = Int32.Max, imageStyle!: RichEditorImageSpanStyle = RichEditorImageSpanStyle())
```

**功能：** 创建RichEditorImageSpanOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| offset | Int32 | 否 | Int32.Max | **命名参数。**  添加图片的位置。省略时，添加到所有文本字符串的最后。 <br>当值小于0时，放在字符串最前面；当值大于字符串长度时，放在字符串最后面。 |
| imageStyle | [RichEditorImageSpanStyle](#class-richeditorimagespanstyle) | 否 | RichEditorImageSpanStyle() | **命名参数。**  图片样式信息。省略时，使用系统默认图片信息。 |

### class RichEditorTextSpanOptions

```cangjie
public class RichEditorTextSpanOptions {
    public init(offset!: Int32 = Int32.Max, style!: RichEditorTextStyle = RichEditorTextStyle())
}
```

**功能：** 添加文本的偏移位置和文本样式信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(Int32, RichEditorTextStyle)

```cangjie
public init(offset!: Int32 = Int32.Max, style!: RichEditorTextStyle = RichEditorTextStyle())
```

**功能：** 创建RichEditorTextSpanOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| offset | Int32 | 否 | Int32.Max | **命名参数。**  添加文本的位置。省略时，添加到所有文本字符串的最后。<br>当值小于0时，放在字符串最前面；当值大于字符串长度时，放在字符串最后面。|
| style | [RichEditorTextStyle](#class-richeditortextstyle) | 否 | RichEditorTextStyle() | **命名参数。**  文本样式信息。省略时，使用系统默认文本信息。 |

### class  SelectionMenuOptions

```cangjie
public class SelectionMenuOptions {
    public init(onAppear!: () -> Unit = { => }, onDisappear!: () -> Unit = { => })
}
```

**功能：** 菜单选项类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(() -> Unit,() -> Unit)

```cangjie
public init(onAppear!: () -> Unit = { => }, onDisappear!: () -> Unit = { => })
```

**功能：** 创建SelectionMenuOptions类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| onAppear | () -> Unit | 否 | { => } | **命名参数。**  回调函数，自定义选择菜单弹出时触发回调函数。 |
| onDisappear | () -> Unit | 否 | { => } | **命名参数。**  回调函数，自定义选择菜单关闭时触发回调函数。 |