# 自定义弹窗（CustomDialog）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

通过CustomDialogController类显示自定义弹窗。使用弹窗组件时，可优先考虑自定义弹窗，便于自定义弹窗的样式与内容。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## class CustomDialogController

```cangjie
public class CustomDialogController {
    public init(value: CustomDialogControllerOptions)
}
```

**功能：** 构造一个CustomDialogController类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(CustomDialogControllerOptions)

```cangjie
public init(value: CustomDialogControllerOptions)
```

**功能：** 创建自定义弹窗的构造器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[CustomDialogControllerOptions](#class-customdialogcontrolleroptions)|是|-|配置自定义弹窗的参数。|

### func closeDialog()

```cangjie
public func closeDialog(): Unit
```

**功能：** 关闭显示的自定义弹窗，若已关闭，则不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func openDialog()

```cangjie
public func openDialog(): Unit
```

**功能：** 显示自定义弹窗内容，允许多次使用，但如果弹框为SubWindow模式，则该弹框不允许再弹出SubWindow弹框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func releaseSelf()

```cangjie
public func releaseSelf(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22