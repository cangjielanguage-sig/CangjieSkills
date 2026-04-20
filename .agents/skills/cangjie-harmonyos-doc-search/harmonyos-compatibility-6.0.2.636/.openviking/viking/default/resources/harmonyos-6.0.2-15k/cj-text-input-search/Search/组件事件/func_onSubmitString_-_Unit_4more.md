### func onSubmit((String) -> Unit)

```cangjie
public func onSubmit(callback: (String)->Unit): This
```

**功能：** 点击搜索图标、搜索按钮或者按下软键盘搜索按钮时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(String)->Unit|是|-|回调函数，提交搜索内容时触发。参数：当前搜索框中输入的文本内容。|

### func onTextSelectionChange((Int32, Int32) -> Unit)

```cangjie
public func onTextSelectionChange(callback: (Int32, Int32)->Unit): This
```

**功能：** 文本选择的位置发生变化或编辑状态下光标位置发生变化时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int32, Int32)->Unit|是|-|回调函数，文本选择变化或光标位置变化时触发。第一个参数为文本选择区域起始位置，文本框中文字的起始位置为0。第二个参数为文本选择区域结束位置。|

### func onWillDelete((Float64, Int32, String) -> Bool)

```cangjie
public func onWillDelete(callback: (Float64, Int32, String)->Bool): This
```

**功能：** 在将要删除时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Float64, Int32, String)->Bool|是|-|回调函数，在将要删除时触发。<br>在返回true时，表示正常删除，返回false时，表示不删除。<br>在预上屏删除操作时，该回调不触发。<br>仅支持系统输入法输入的场景。|

### func onWillInsert((Float64, String) -> Bool)

```cangjie
public func onWillInsert(callback: (Float64, String)->Bool): This
```

**功能：** 在将要输入时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Float64, String)->Bool|是|-|回调函数，在将要输入时触发。<br>在返回true时，表示正常插入，返回false时，表示不插入。<br>在预上屏操作时，该回调不触发。<br>仅支持系统输入法输入的场景。|