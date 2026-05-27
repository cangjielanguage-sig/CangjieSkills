### class SubmitEvent

```cangjie
public class SubmitEvent {
    public var text: String
    public init()
}
```

**功能：** 定义用户提交事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var text: String

```cangjie
public var text: String
```

**功能：** 设置输入框文本内容。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init()

```cangjie
public init()
```

**功能：** 创建SubmitEvent类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum CancelButtonStyle

```cangjie
public enum CancelButtonStyle {
    | CONSTANT
    | INVISIBLE
    | INPUT
}
```

**功能：** 表示文本清除按钮样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### CONSTANT

```cangjie
CONSTANT
```

**功能：** 表示清除按钮常显样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### INPUT

```cangjie
INPUT
```

**功能：** 表示清除按钮输入样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### INVISIBLE

```cangjie
INVISIBLE
```

**功能：** 表示清除按钮常隐样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum EnterKeyType

```cangjie
public enum EnterKeyType {
    | Go
    | EntrySearch
    | Send
    | Next
    | Done
    | PREVIOUS
    | NEW_LINE
}
```

**功能：** 表示键盘操作按钮的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Done

```cangjie
Done
```

**功能：** 表示显示为完成样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### EntrySearch

```cangjie
EntrySearch
```

**功能：** 表示显示为搜索样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Go

```cangjie
Go
```

**功能：** 表示显示Go文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Next

```cangjie
Next
```

**功能：** 表示显示为下一个样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### NEW_LINE

```cangjie
NEWL_INE
```

**功能：** 表示显示为换行样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### PREVIOUS

```cangjie
PREVIOUS
```

**功能：** 表示显示为上一个样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Send

```cangjie
Send
```

**功能：** 表示显示为发送样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### enum TextInputStyle

```cangjie
public enum TextInputStyle {
    | Default
    | Inline
}
```

**功能：** 表示输入风格。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Default

```cangjie
Default
```

**功能：** 表示默认风格，光标宽1.5.vp，光标高度与文本选中底板高度和字体大小相关。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Inline

```cangjie
Inline
```

**功能：** 表示内联输入风格。文本选中底板高度与输入框高度相同。内联输入适用于需要明显区分编辑状态和非编辑状态的场景，如文件列表视图中的重命名。内联输入不支持`showError`属性，并且在内联模式下不支持拖入文本功能。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12