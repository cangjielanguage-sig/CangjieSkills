## 组件事件

### func onPopupSelect(?OnAlphabetIndexerPopupSelectCallback)

```cangjie
public func onPopupSelect(callback: ?OnAlphabetIndexerPopupSelectCallback): This
```

**功能：** 字母索引提示弹窗字符串列表选中触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[OnAlphabetIndexerPopupSelectCallback](#type-onalphabetindexerpopupselectcallback)|是|-|回调函数，字母索引提示弹窗字符串列表选中时触发。初始值: { _: Int64 => }|

### func onRequestPopupData(?OnAlphabetIndexerRequestPopupDataCallback)

```cangjie
public func onRequestPopupData(callback: ?OnAlphabetIndexerRequestPopupDataCallback): This
```

**功能：** 选中字母索引后触发该事件，请求索引提示弹窗显示内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[OnAlphabetIndexerRequestPopupDataCallback](#type-onalphabetindexerrequestpopupdatacallback)|是|-|回调函数，当前选中索引触发。<br>返回值：索引对应的字符串数组，此字符串数组在弹窗中竖排显示，字符串列表最多显示5个，超出部分可以滑动显示。初始值: { _: Int64 => Array\<String>() }|

### func onSelect(?OnAlphabetIndexerSelectCallback)

```cangjie
public func onSelect(callback: ?OnAlphabetIndexerSelectCallback): This
```

**功能：** 索引条选中触发该事件，返回值为当前选中索引。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[OnAlphabetIndexerSelectCallback](#type-onalphabetindexerselectcallback)|是|-|回调函数，索引条选中时触发。初始值: { _: Int64 => }|

## 基础类型定义

### type OnAlphabetIndexerSelectCallback

```cangjie
public type OnAlphabetIndexerSelectCallback = (Int64) -> Unit
```

**功能：** 索引项被选中时触发的事件。

**类型：** (Int64) -> Unit

### type OnAlphabetIndexerRequestPopupDataCallback

```cangjie
public type OnAlphabetIndexerRequestPopupDataCallback = (Int64) -> Array<String>
```

**功能：** usingPopup设置值为true，索引项被选中时触发的事件。

**类型：** (Int64) -> Array\<String>

### type OnAlphabetIndexerPopupSelectCallback

```cangjie
public type OnAlphabetIndexerPopupSelectCallback = (Int64) -> Unit
```

**功能：** 提示弹窗二级索引项被选中时触发的事件。

**类型：** (Int64) -> Unit