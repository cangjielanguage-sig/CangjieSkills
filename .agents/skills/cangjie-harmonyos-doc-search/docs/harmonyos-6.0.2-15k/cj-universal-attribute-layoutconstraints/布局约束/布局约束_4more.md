# 布局约束

通过组件的宽高比和显示优先级约束组件显示效果。

## func aspectRatio(Float64)

```cangjie
public func aspectRatio(value: Float64): This
```

**功能：** 指定当前组件的宽高比。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|当前组件的宽高比，aspectRatio = width/height。<br> **说明：** <br> 该属性在不设置值或者设置非法值(小于等于0.0)时不生效。<br> 例如，Row只设置宽度且没有子组件，aspectRatio不设置值或者设置成负数时，此时Row高度为0.0。|

## func aspectRatio(Int64)

```cangjie
public func aspectRatio(value: Int64): This
```

**功能：** 指定当前组件的宽高比。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int64|是|-|当前组件的宽高比，aspectRatio = width/height。<br> **说明：** <br> 该属性在不设置值或者设置非法值(小于等于0)时不生效。<br> 例如，Row只设置宽度且没有子组件，aspectRatio不设置值或者设置成负数时，此时Row高度为0。|

> **说明：**
>
> - 仅设置width、aspectRatio时，height=width/aspectRatio。
> - 仅设置height、aspectRatio时，width=height*aspectRatio。
> - 同时设置width、height和aspectRatio时，height不生效，height=width/aspectRatio。
> - 设置aspectRatio属性后，组件宽高会受父组件内容区大小限制。

## func displayPriority(Int32)

```cangjie
public func displayPriority(value: Int32): This
```

**功能：** 设置当前组件在布局容器中显示的优先级。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|当前组件在布局容器中显示的优先级。<br> 初始值：1。 <br> **说明：** <br> 仅在[Row](./cj-row-column-stack-row.md#row)/[Column](./cj-row-column-stack-column.md#column)/[Flex(单行)](./cj-row-column-stack-flex.md#flex)容器组件中生效。<br>小数点后的数字不作优先级区分，即区间为[x, x + 1)内的数字视为相同优先级。例如：1.0与1.9为同一优先级。子组件的displayPriority均不大于1时，优先级没有区别。当子组件的displayPriority大于1时，displayPriority数值越大，优先级越高。若父容器空间不足，隐藏低优先级子组件。若某一优先级的子组件被隐藏，则优先级更低的子组件也都被隐藏。|