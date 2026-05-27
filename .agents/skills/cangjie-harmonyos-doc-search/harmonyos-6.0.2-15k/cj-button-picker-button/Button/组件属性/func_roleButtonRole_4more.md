### func role(ButtonRole)

```cangjie
public func role(value: ButtonRole): This
```

**功能：** 设置Button组件的角色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ButtonRole](#enum-buttonrole)|是|-|设置Button组件的角色。<br>初始值：BottonRole.Normal。|

### func shape(ShapeType)

```cangjie
public func shape(shapeType: ShapeType): This
```

**功能：** 设置Button组件的形状。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|shapeType|[ShapeType](./cj-common-types.md#enum-shapetype)|是|-|形状类型。|

### func shape(ButtonType)

```cangjie
public func shape(buttonType: ButtonType): This
```

**功能：** 设置Button组件的形状。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|buttonType|[ButtonType](#enum-buttontype)|是|-|按键形状类型。|

### func stateEffect(Bool)

```cangjie
public func stateEffect(value: Bool): This
```

**功能：** 设置是否开启按压态显示效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|按钮按下时是否开启按压态显示效果，当设置为false时，按压效果关闭。<br/>初始值：true|

> **说明**
>
> 使用多态样式设置按压态时，需优先设置stateEffect为false，防止内置按压态与多态样式按压态冲突。