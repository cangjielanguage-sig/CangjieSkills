### func onEditChanged((Bool) -> Unit)

```cangjie
public func onEditChanged(callback: (Bool) -> Unit): This
```

**功能：** 输入状态变化时，触发该事件。有光标时为编辑态，无光标时为非编辑态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Bool)->Unit|是|-|回调函数，编辑状态改变时触发，返回当前编辑状态。参数为true表示正在输入。|

### func onPaste((String) -> Unit)

```cangjie
public func onPaste(callback: (String) -> Unit): This
```

**功能：** 进行粘贴操作时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(String)->Unit|是|-|回调函数，粘贴时触发，返回粘贴的文本内容。|

### func onSubmit((EnterKeyType) -> Unit)

```cangjie
public func onSubmit(callback: (EnterKeyType) -> Unit): This
```

**功能：** 按下输入法回车键触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([EnterKeyType](./cj-text-input-textinput.md#enum-enterkeytype))->Unit|是|-|回调函数，按下回车键或者软键盘回车键触发。参数：当前软键盘回车键类型。类型为EnterKeyType.NEW_LINE时不触发onSubmit。|

### func onTextSelectionChange((Int32, Int32) -> Unit)

```cangjie
public func onTextSelectionChange(callback: (Int32, Int32) -> Unit): This
```

**功能：** 文本选择的位置发生变化或编辑状态下光标位置发生变化时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int32, Int32)->Unit|是|-|回调函数，文本选择的位置发生变化或编辑状态下光标位置发生变化时触发，第一个参数表示所选文本的起始位置，文字的起始位置为0。第二个参数表示所选文本的结束位置。|

### func onWillDelete((Float64, Int32, String) -> Bool)

```cangjie
public func onWillDelete(callback: (Float64, Int32, String) -> Bool): This
```

**功能：** 在将要删除时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Float64, Int32, String)->Bool|是|-|回调函数，在将要删除时触发。<br/>仅支持系统输入法输入的场景。<br>第一个参数表示删除的值的位置信息。<br>第二个参数表示删除值的方向。<br>第三个参数表示删除的值。<br>在返回true时，表示正常删除，返回false时，表示不删除。<br>在预上屏删除操作时，该回调不触发。仅支持系统输入法输入的场景。|

### func onWillInsert((Float64, String) -> Bool)

```cangjie
public func onWillInsert(callback: (Float64, String) -> Bool): This
```

**功能：** 在将要输入时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Float64, String)->Bool|是|-|回调函数，在将要输入时触发。<br/>仅支持系统输入法输入的场景。<br>第一个参数表示插入的值的位置信息。<br>第二个参数表示插入的值。<br>返回true时，表示正常插入，返回false时，表示不插入。<br>在预上屏和候选词操作时，该回调不触发。仅支持系统输入法输入的场景。|