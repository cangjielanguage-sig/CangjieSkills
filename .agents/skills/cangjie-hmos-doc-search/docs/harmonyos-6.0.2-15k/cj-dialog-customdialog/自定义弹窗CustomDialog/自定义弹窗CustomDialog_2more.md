# 自定义弹窗（CustomDialog）

通过CustomDialogController类显示自定义弹窗。使用弹窗组件时，可优先考虑自定义弹窗，便于自定义弹窗的样式与内容。

> **说明：**
>
> - 自定义弹窗组件需要用@CustomDialog修饰，@CustomDialog是一个具有限制的@Component，@CustomDialog修饰的组件必须包含一个类型为Option\<CustomDialogController>的属性。这个属性会在使用到该弹窗的组件中被隐式地赋值。

## class CustomDialogController

```cangjie
public class CustomDialogController {
    public init(options: CustomDialogControllerOptions)
}
```

**功能：** 构造一个CustomDialogController类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(CustomDialogControllerOptions)

```cangjie
public init(options: CustomDialogControllerOptions)
```

**功能：** 创建自定义弹窗的构造器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[CustomDialogControllerOptions](#class-customdialogcontrolleroptions)|是|-|配置自定义弹窗的参数。|

### func \`open\`()

```cangjie
public func `open`()
```

**功能：** 显示自定义弹窗内容，允许多次使用，但如果弹框为SubWindow模式，则该弹框不允许再弹出SubWindow弹框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func bindView(CustomView)

```cangjie
public func bindView(view: CustomView)
```

**功能：** 将CustomView绑定到自定义弹窗构建器，用户无需主动调用，会在宏展开后隐式地调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|view|CustomView|是|-|被绑定的CustomView。|

### func close()

```cangjie
public func close()
```

**功能：** 关闭显示的自定义弹窗，若已关闭，则不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func setBuilder(() -> Unit)

```cangjie
public func setBuilder(builder: ()-> Unit)
```

**功能：** 设置一个构建器，用户无需主动调用，会在宏展开后隐式地调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|() -> Unit|是|-|builder对应的渲染函数。|