# CheckboxGroup

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

多选框群组，用于控制多选框全选或者不全选状态。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

无

## 创建组件

### init(?String)

```cangjie
public init(group!: ?String = None)
```

**功能：** 创建多选框群组，可以控制群组内的Checkbox全选或者不全选，group值相同的Checkbox和CheckboxGroup为同一群组。

在结合带缓存组件使用时(如List)，未被创建的Checkbox选中状态需要应用手动控制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|group|?String|否|None| **命名参数。** 多选框的群组名称。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。

## 组件属性

### func selectAll(?Bool)

```cangjie
public func selectAll(value: ?Bool): This
```

**功能：** 设置是否全选。若同组的[Checkbox](./cj-button-picker-checkbox.md)显式设置了select属性，则Checkbox的优先级高。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-|是否全选。初始值：false。<br>值为true时，多选框群组都被选中。值为false时，多选框群组都不被选中。|

### func selectedColor(?ResourceColor)

```cangjie
public func selectedColor(value: ?ResourceColor): This
```

**功能：** 设置被选中或部分选中状态的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|被选中或部分选中状态的颜色。|

## 组件事件

### func onChange(?OnCheckboxGroupChangeCallback)

```cangjie
public func onChange(callback: ?OnCheckboxGroupChangeCallback): This
```

**功能：** CheckboxGroup的选中状态或群组内的Checkbox的选中状态发生变化时，触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[OnCheckboxGroupChangeCallback](#type-oncheckboxgroupchangecallback)|是|-|多选框群组的信息。初始值：{ _ => }|