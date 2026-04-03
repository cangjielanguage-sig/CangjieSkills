### func onReady(?VoidCallback)

```cangjie
public func onReady(callback: ?VoidCallback): This
```

**功能：** 富文本组件初始化完成后，触发事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[VoidCallback](./cj-common-types.md#type-voidcallback)|是|-|回调函数，富文本组件初始化完成后触发回调。<br>初始值：{ => }。|

### func aboutToImeInput(?Callback\<RichEditorInsertValue, Bool>)

```cangjie
public func aboutToImeInput(callback: ?Callback<RichEditorInsertValue, Bool>): This
```

**功能：** 输入法输入内容前，触发事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[Callback](./cj-common-types.md#type-callbackt-v)\<[RichEditorInsertValue](#class-richeditorinsertvalue), Bool>|是|-|回调函数，输入法输入内容前触发。RichEditorInsertValue：输入法将要输入内容信息。true：组件执行添加内容操作。false：组件不执行添加内容操作。<br>初始值：{ _ => false }。|

### func onImeInputComplete(?Callback\<RichEditorTextSpanResult, Unit>)

```cangjie
public func onImeInputComplete(callback: ?Callback<RichEditorTextSpanResult, Unit>): This
```

**功能：** 输入法完成输入后，触发事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[Callback](./cj-common-types.md#type-callbackt-v)\<[RichEditorTextSpanResult](#class-richeditortextspanresult), Unit>|是|-|回调函数，输入法完成输入后触发回调。RichEditorTextSpanResult：输入法完成输入后的文本Span信息。<br>初始值：{ _ => false }。|

### func onDeleteComplete(?VoidCallback)

```cangjie
public func onDeleteComplete(callback: ?VoidCallback): This
```

**功能：** 输入法完成删除后，触发事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[VoidCallback](./cj-common-types.md#type-voidcallback)|是|-|回调函数，订阅输入法完成删除时触发。<br>初始值：{ => }。|

### func aboutToDelete(?Callback\<RichEditorDeleteValue, Bool>)

```cangjie
public func aboutToDelete(callback: ?Callback<RichEditorDeleteValue, Bool>): This
```

**功能：** 输入法删除内容前，触发事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[Callback](./cj-common-types.md#type-callbackt-v)\<[RichEditorDeleteValue](#class-richeditordeletevalue), Bool>|是|-|回调函数，输入法删除内容前触发该回调 。RichEditorDeleteValue：准备删除的内容所在的文本Span信息。true：组件执行删除操作。false：组件不执行删除操作。<br>初始值：{ _ => false }。|

### func onSelect(?Callback\<RichEditorSelection, Unit>)

```cangjie
public func onSelect(callback: ?Callback<RichEditorSelection, Unit>): This
```

**功能：** 鼠标左键双击选中内容时，会触发事件；松开鼠标左键后，会再次触发事件。手指长按选中内容时，会触发事件；松开手指后，会再次触发事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[Callback](./cj-common-types.md#type-callbackt-v)\<[RichEditorSelection](#class-richeditorselection), Unit>|是|-|回调函数，RichEditorSelection为选中的所有Span信息。<br>初始值：{ _ => }。|