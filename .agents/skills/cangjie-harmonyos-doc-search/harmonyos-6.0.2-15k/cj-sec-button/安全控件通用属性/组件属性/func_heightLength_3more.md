### func height(Length)

```cangjie
public open func height(value: Length): This
```

**功能：** 设置安全控件自身的高度，缺省时将根据元素内容自适配高度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|安全控件自身的高度，缺省时将根据元素内容自适配高度。若设置高度小于当前属性组合下允许的最小高度时，高度不会缩减到设置值，此时高度会大于设置高度，以保证安全控件显示的完整性。|

### func size(Length, Length)

```cangjie
public open func size(width!: Length, height!: Length): This
```

**功能：** 设置高宽尺寸，缺省时将根据元素内容自适配高宽尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|[Length](./cj-common-types.md#interface-length)|是|-|宽度尺寸，缺省时将根据元素内容自适配宽尺寸。若设置尺寸小于当前属性组合下允许的最小尺寸时，宽度会调整到设置值，此时按钮文本信息会自动换行，以保证安全控件显示的完整性。|
|height|[Length](./cj-common-types.md#interface-length)|是|-|高度尺寸，缺省时将根据元素内容自适配高尺寸。若设置尺寸小于当前属性组合下允许的最小尺寸时，高度不会缩减到设置值，此时按钮文本信息会自动换行，以保证安全控件显示的完整性。|

### func constraintSize(Length, Length, Length, Length)

```cangjie
public func constraintSize(
    minWidth!: Length = 0.vp,
    maxWidth!: Length = (Float64.Inf).vp,
    minHeight!: Length = 0.vp,
    maxHeight!: Length = (Float64.Inf).vp
): This
```

**功能：** 设置约束尺寸，组件布局时，进行尺寸范围限制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|minWidth|[Length](./cj-common-types.md#interface-length)|是|-|约束尺寸，组件布局时，进行尺寸范围限制。<br/>初始值：0.vp。|
|maxWidth|[Length](./cj-common-types.md#interface-length)|是|-|约束尺寸，组件布局时，进行尺寸范围限制。<br/>初始值：(Float64.Inf).vp。|
|minHeight|[Length](./cj-common-types.md#interface-length)|是|-|约束尺寸，组件布局时，进行尺寸范围限制。<br/>初始值：0.vp。|
|maxHeight|[Length](./cj-common-types.md#interface-length)|是|-|约束尺寸，组件布局时，进行尺寸范围限制。<br/>初始值：(Float64.Inf).vp。|

> **说明：**
>
> constraintSize的优先级高于Width和Height。取值结果参考[constraintSize取值对width/height影响](./cj-universal-attribute-size.md)。
同width/height一样，若设置尺寸小于当前属性组合下允许的最小尺寸时，高度不会缩减到设置值，宽度会调整到设置值，此时按钮文本信息会自动换行，以保证安全控件显示的完整性。