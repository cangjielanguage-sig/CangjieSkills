### func onSelect((RichEditorSelection) -> Unit)

```cangjie
public func onSelect(callback: (RichEditorSelection) -> Unit): This
```

**功能：** 鼠标左键双击选中内容时，会触发事件；松开鼠标左键后，会再次触发事件。手指长按选中内容时，会触发事件；松开手指后，会再次触发事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([RichEditorSelection](#class-richeditorselection))->Unit|是|-|回调函数，鼠标左键按下选择，松开左键后触发回调。<br>用手指选择时，松开手指触发回调。<br>RichEditorSelection：选中的所有Span信息。|

### func onSelectionChange((RichEditorRange) -> Unit)

```cangjie
public func onSelectionChange(callback: (RichEditorRange) -> Unit): This
```

**功能：** 内容选择区域或编辑状态下的光标位置发生变化时，将触发该事件。光标位置变化时，回调中选择区域的起始和终止位置相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([RichEditorRange](#class-richeditorrange)) -> Unit|是|-|[RichEditorRange](#class-richeditorrange)为所有内容的选择区域起始和终止位置。订阅文本选择区域发生变化或编辑状态下光标位置发生变化时触发的回调函数。|

### func onSubmit((EnterKeyType, SubmitEvent) -> Unit)

```cangjie
public func onSubmit(callback: (EnterKeyType, SubmitEvent) -> Unit): This
```

**功能：** 按下软键盘输入法回车键时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([EnterKeyType](./cj-text-input-textinput.md#enum-enterkeytype), [SubmitEvent](./cj-text-input-textinput.md#class-submitevent)) -> Unit|是|-|按下软键盘输入法回车键时触发该回调函数。</br>**参数一:** 软键盘输入法回车键类型。具体类型见EnterKeyType枚举说明。</br>**参数二:** 当提交的时候，提供保持组件编辑状态的方法。EnterKeyType指定为NEW_LINE时，默认保持编辑态。|

### func onEditingChange((Bool) -> Unit)

```cangjie
public func onEditingChange(callback: (Bool) -> Unit): This
```

**功能：** 组件内容的编辑状态发生变化时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Bool) -> Unit|是|-| 组件内容的编辑状态发生变化时触发该回调函数。</br>**参数:** true表示编辑态，false表示非编辑态。|

### func onCopy((CopyEvent) -> Unit)

```cangjie
public func onCopy(callback: (CopyEvent) -> Unit): This
```

**功能：** 复制时触发事件。开发者可以通过该方法，覆盖系统默认行为，实现图文的复制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([CopyEvent](#class-copyevent)) -> Unit|是|-|复制时触发该回调函数。</br>**参数:** 定义用户复制事件。|

### func onCut((CutEvent) -> Unit)

```cangjie
public func onCut(callback: (CutEvent) -> Unit): This
```

**功能：** 剪切时触发事件。开发者可以通过该方法，覆盖系统默认行为，实现图文的剪切。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([CutEvent](#class-cutevent)) -> Unit|是|-|剪切时触发该回调函数。</br>**参数:** 定义用户剪切事件。|