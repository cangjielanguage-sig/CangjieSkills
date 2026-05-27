# CheckboxGroup

多选框群组，用于控制多选框全选或者不全选状态。

## 子组件

无

## 创建组件

### init(String)

```cangjie
public init(group!: String = "")
```

**功能：** 创建多选框群组，可以控制群组内的Checkbox全选或者不全选，group值相同的Checkbox和CheckboxGroup为同一群组。

在结合带缓存组件使用时(如List)，未被创建的Checkbox选中状态需要应用手动控制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|group|String|否|""| **命名参数。** 多选框的群组名称。<br/>**说明**：<br/>多个相同群组名称的CheckboxGroup，仅第一个CheckboxGroup生效。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。