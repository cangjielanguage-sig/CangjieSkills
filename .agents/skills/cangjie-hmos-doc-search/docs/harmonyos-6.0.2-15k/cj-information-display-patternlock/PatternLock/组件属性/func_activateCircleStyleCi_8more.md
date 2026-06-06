### func activateCircleStyle(CircleStyleOptions)

```cangjie
public func activateCircleStyle(value: CircleStyleOptions): This
```

**功能：** 设置宫格圆点在“激活”状态的背景圆环样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[CircleStyleOptions](#class-circlestyleoptions)|是|-|宫格圆点在“激活”状态的背景圆环样式。|

### func activeColor(Color)

```cangjie
public func activeColor(color: Color): This
```

**功能：** 设置宫格圆点在“激活”状态的填充颜色，“激活”状态为手指经过圆点但还未选中的状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[Color](./cj-common-types.md#class-color)|是|-|宫格圆点在“激活”状态的填充颜色。<br/>初始值：0xff182431。|

### func autoReset(Bool)

```cangjie
public func autoReset(value: Bool): This
```

**功能：** 设置在完成密码输入后再次在组件区域按下时是否重置组件状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|在完成密码输入后再次在组件区域按下时是否重置组件状态。为true时，完成密码输入后再次在组件区域按下时会重置组件状态（即清除之前输入的密码）；为false时，不会重置组件状态。<br/>初始值：true。|

### func circleRadius(Length)

```cangjie
public func circleRadius(value: Length): This
```

**功能：** 设置宫格中圆点的半径。设置为0或负数时取初始值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|宫格中圆点的半径。<br/>初始值：6.vp。<br/>取值范围：(0, sideLength/11]，设置小于等于0的值时按初始值处理，超过最大值按最大值处理。|

### func pathColor(Color)

```cangjie
public func pathColor(color: Color): This
```

**功能：** 设置连线的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[Color](./cj-common-types.md#class-color)|是|-|连线的颜色。<br/>初始值：0x33182431。|

### func pathStrokeWidth(Length)

```cangjie
public func pathStrokeWidth(value: Length): This
```

**功能：** 设置连线的宽度。设置为0或负数时连线不显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|连线的宽度。<br/>初始值：12.vp。<br/>取值范围：[0, sideLength/3]，超过最大值按最大值处理。|

### func regularColor(Color)

```cangjie
public func regularColor(color: Color): This
```

**功能：** 设置宫格圆点在“未选中”状态的填充颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[Color](./cj-common-types.md#class-color)|是|-|宫格圆点在“未选中”状态的填充颜色。<br/>初始值：0xff182431。|

### func selectedColor(Color)

```cangjie
public func selectedColor(color: Color): This
```

**功能：** 设置宫格圆点在“选中“状态的填充颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[Color](./cj-common-types.md#class-color)|是|-|宫格圆点在“选中”状态的填充颜色。<br/>初始值：0xff182431。|