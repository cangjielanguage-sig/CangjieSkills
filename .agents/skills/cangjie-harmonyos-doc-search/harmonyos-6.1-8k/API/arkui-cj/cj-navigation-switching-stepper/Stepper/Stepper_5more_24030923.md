# Stepper

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

步骤导航器。当完成一个任务需要多个步骤时，可以使用步骤导航器展示当前进展。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

仅能包含子组件[StepperItem](./cj-navigation-switching-stepperitem.md)。

## 创建组件

### init(?UInt32, () -> Unit)

```cangjie
public init(index!: ?UInt32 = None, child!: () -> Unit = {=>})
```

**功能：** 构造一个步骤导航器组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|?UInt32|否|None| **命名参数。** 步骤导航器当前显示StepperItem的索引值。<br>初始值：0。|
|child|() -> Unit|否|{=>}| **命名参数。** 步骤导航器的子组件。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。