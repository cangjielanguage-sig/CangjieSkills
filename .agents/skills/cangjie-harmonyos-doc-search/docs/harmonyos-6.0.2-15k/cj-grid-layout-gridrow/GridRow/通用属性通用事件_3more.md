## 通用属性/通用事件

通用属性：除文本样式外，其余全部支持。

通用事件：全部支持。

## 组件属性

### func alignItems(ItemAlign)

```cangjie
public func alignItems(value: ItemAlign): This
```

**功能：** 设置GridRow中的GridCol垂直主轴方向对齐方式。GridCol本身也可通过alignSelf([ItemAlign](./cj-common-types.md#enum-itemalign))设置自身对齐方式。当上述两种对齐方式都设置时，以GridCol自身设置为准。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ItemAlign](./cj-common-types.md#enum-itemalign)|是|-|GridRow中的GridCol垂直主轴方向对齐方式。<br>初始值：ItemAlign.Start<br>**说明：**<br>ItemAlign支持的枚举：ItemAlign.Start、ItemAlign.Center、ItemAlign.End、ItemAlign.Stretch。|

## 组件事件

### func onBreakpointChange((String) -> Unit)

```cangjie
public func onBreakpointChange(callback: (String)->Unit): This
```

**功能：** 断点发生变化时触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(String)->Unit|是|-|断点发生变化时触发回调取值为"xs"、"sm"、"md"、"lg"、"xl"、"xxl"|