### func aboutToIMEInput((RichEditorInsertValue) -> Bool)

```cangjie
public func aboutToIMEInput(callback: (RichEditorInsertValue) -> Bool): This
```

**功能：** 输入法输入内容前，触发事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([RichEditorInsertValue](#class-richeditorinsertvalue))->Bool|是|-|回调函数，输入法输入内容前触发。<br>[RichEditorInsertValue](#class-richeditorinsertvalue)：输入法将要输入内容信息。<br>true：组件执行添加内容操作。<br>false：组件不执行添加内容操作。|

### func aboutToDelete((RichEditorDeleteValue) -> Bool)

```cangjie
public func aboutToDelete(callback: (RichEditorDeleteValue) -> Bool): This
```

**功能：** 输入法删除内容前，触发事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([RichEditorDeleteValue](#class-richeditordeletevalue))->Bool|是|-|回调函数，输入法删除内容前触发该回调 。<br>[RichEditorDeleteValue](#class-richeditordeletevalue)：准备删除的内容所在的文本Span信息。<br>true：组件执行删除操作。<br>false：组件不执行删除操作。|

### func onDeleteComplete(() -> Unit)

```cangjie
public func onDeleteComplete(callback: () -> Unit): This
```

**功能：** 输入法完成删除后，触发事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，订阅输入法完成删除时触发。|

### func onDidChange((TextRange, TextRange) -> Unit)

```cangjie
public func onDidChange(callback: (TextRange, TextRange) -> Unit): This
```

**功能：** 组件执行增删操作后，触发事件。文本实际未发生增删时，不触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([TextRange](#class-textrange), [TextRange](#class-textrange))->Unit|是|-|回调函数，件执行增删操作后，触发回调。文本实际未发生增删时，不触发该回调。参数：图文变化前后的内容范围。|

### func onIMEInputComplete((RichEditorTextSpanResult) -> Unit)

```cangjie
public func onIMEInputComplete(callback: (RichEditorTextSpanResult) -> Unit): This
```

**功能：** 输入法完成输入后，触发事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([RichEditorTextSpanResult](#class-richeditortextspanresult))->Unit|是|-|回调函数，输入法完成输入后触发回调。<br>RichEditorTextSpanResult：输入法完成输入后的文本Span信息。|

### func onPaste((PasteEvent) -> Unit)

```cangjie
public func onPaste(callback: (PasteEvent) -> Unit): This
```

**功能：** 完成粘贴前，触发事件。

> **说明：**
>
> 开发者可以通过该方法，覆盖系统默认行为，实现图文的粘贴。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([PasteEvent](#class-pasteevent))->Unit|是|-|回调函数，完成粘贴前，触发回调。<br>PasteEvent：定义用户粘贴事件。|

### func onReady(() -> Unit)

```cangjie
public func onReady(callback: () -> Unit): This
```

**功能：** 富文本组件初始化完成后，触发事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，富文本组件初始化完成后触发回调。|