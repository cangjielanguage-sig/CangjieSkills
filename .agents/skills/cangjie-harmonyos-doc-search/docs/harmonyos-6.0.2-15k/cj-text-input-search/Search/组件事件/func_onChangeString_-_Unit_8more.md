### func onChange((String) -> Unit)

```cangjie
public func onChange(callback: (String)->Unit): This
```

**功能：** 输入内容发生变化时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(String)->Unit|是|-|回调函数，当前输入文本内容变化时触发。|

### func onContentScroll((Float32, Float32) -> Unit)

```cangjie
public func onContentScroll(callback: (Float32, Float32)->Unit): This
```

**功能：** 文本内容滚动时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Float32, Float32)->Unit|是|-|回调函数，文本内容滚动时触发，第一个参数表示X轴方向的偏移量，第二个参数表示Y轴方向的偏移量。单位：px。|

### func onCopy((String) -> Unit)

```cangjie
public func onCopy(callback: (String)->Unit): This
```

**功能：** 进行复制操作时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(String)->Unit|是|-|回调函数，剪切时触发。参数：返回剪切的文本内容。|

### func onCut((String) -> Unit)

```cangjie
public func onCut(callback: (String)->Unit): This
```

**功能：** 进行剪切操作时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(String)->Unit|是|-|回调函数，剪切时触发。参数：返回剪切的文本内容。|

### func onDidDelete((Float64, Int32, String) -> Unit)

```cangjie
public func onDidDelete(callback: (Float64, Int32, String)->Unit): This
```

**功能：** 在删除完成时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Float64, Int32, String)->Unit|是|-|回调函数，在删除完成时触发。<br/>仅支持系统输入法输入的场景。<br>第一个参数表示删除的值的位置信息。<br>第二个参数表示删除值的方向。<br>第三个参数表示删除的值。|

### func onDidInsert((Float64, String) -> Unit)

```cangjie
public func onDidInsert(callback: (Float64, String)->Unit): This
```

**功能：** 在输入完成时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Float64, String)->Unit|是|-|回调函数，在输入完成时触发。<br/>仅支持系统输入法输入的场景。<br>第一个参数表示插入的值的位置信息。<br>第二个参数表示插入的值。|

### func onEditChange((Bool) -> Unit)

```cangjie
public func onEditChange(callback: (Bool)->Unit): This
```

**功能：** 输入状态变化时，触发该事件。有光标时为编辑态，无光标时为非编辑态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Bool)->Unit|是|-|回调函数，编辑状态改变时触发。参数：返回当前编辑状态。参数为true表示正在输入。|

### func onPaste((String) -> Unit)

```cangjie
public func onPaste(callback: (String)->Unit): This
```

**功能：** 进行粘贴操作时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(String)->Unit|是|-|回调函数，组件触发系统剪切板粘贴操作时触发。|