## 组件事件

### func onPopupSelect((Int64) -> Unit)

```cangjie
public func onPopupSelect(callback: (Int64) -> Unit): This
```

**功能：** 字母索引提示弹窗字符串列表选中触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int64)->Unit|是|-|回调函数，字母索引提示弹窗字符串列表选中时触发。|

### func onRequestPopupData((Int64) -> Array\<String>)

```cangjie
public func onRequestPopupData(callback: (Int64) -> Array<String>): This
```

**功能：** 选中字母索引后触发该事件，请求索引提示弹窗显示内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int64)->Array\<String>|是|-|回调函数，当前选中索引触发。<br>返回值：索引对应的字符串数组，此字符串数组在弹窗中竖排显示，字符串列表最多显示5个，超出部分可以滑动显示。|

### func onSelect((Int64) -> Unit)

```cangjie
public func onSelect(callback: (Int64) -> Unit): This
```

**功能：** 索引条选中触发该事件，返回值为当前选中索引。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int64)->Unit|是|-|回调函数，索引条选中时触发。|

## 基础类型定义

### enum IndexerAlign

```cangjie
public enum IndexerAlign {
    | Left
    | Right
}
```

**功能：** 提示弹窗显示位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Left

```cangjie
Left
```

**功能：** 索引条显示在弹框左侧。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Right

```cangjie
Right
```

**功能：** 索引条显示在弹框右侧。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取参数值,返回解锁结果是否复用对应的整数值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

> **说明：**
>
> 未来版本即将弃用。

**起始版本：** 12