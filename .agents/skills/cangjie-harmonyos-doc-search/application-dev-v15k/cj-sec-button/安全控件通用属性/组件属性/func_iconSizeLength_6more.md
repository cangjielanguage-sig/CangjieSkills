### func iconSize(Length)

```cangjie
public open func iconSize(size: Length): This
```

**功能：** 设置安全控件上图标的尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|是|-|安全控件上图标的尺寸。<br/>初始值：16.vp。|

### func layoutDirection(SecurityComponentLayoutDirection)

```cangjie
public open func layoutDirection(value: SecurityComponentLayoutDirection): This
```

**功能：** 设置安全控件上图标和文字分布的方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[SecurityComponentLayoutDirection](#enum-securitycomponentlayoutdirection)|是|-|安全控件上图标和文字分布的方向。<br/>初始值：SecurityComponentLayoutDirection.Horizontal。|

### func position(Length, Length)

```cangjie
public open func position(x!: Length, y!: Length): This
```

**功能：** 设置绝对定位，设置安全控件的左上角相对于父容器左上角的偏移位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|[Length](./cj-common-types.md#interface-length)|是|-|安全控件的左上角相对于父容器左上角的偏移位置的x轴坐标。<br/>初始值：0.vp。|
|y|[Length](./cj-common-types.md#interface-length)|是|-|安全控件的左上角相对于父容器左上角的偏移位置的y轴坐标。<br/>初始值：0.vp。|

### func markAnchor(Length, Length)

```cangjie
public open func markAnchor(x!: Length, y!: Length): This
```

**功能：** 设置安全控件在位置定位时的锚点，以控件左上角作为基准点进行偏移。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|[Length](./cj-common-types.md#interface-length)|是|-|安全控件在位置定位时的锚点，以控件左上角作为基准点进行偏移的x轴坐标，单独使用时，效果类似offset。<br/>初始值：0.vp。|
|y|[Length](./cj-common-types.md#interface-length)|是|-|安全控件在位置定位时的锚点，以控件左上角作为基准点进行偏移的y轴坐标，单独使用时，效果类似offset。<br/>初始值：0.vp。|

### func offset(Length, Length)

```cangjie
public open func offset(x!: Length, y!: Length): This
```

**功能：** 设置安全控件相对于自身布局位置的坐标偏移。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|[Length](./cj-common-types.md#interface-length)|是|-|安全控件相对于自身布局位置的坐标偏移的x轴坐标。设置此属性不会影响父容器的布局，仅在绘制过程中调整位置。<br/>初始值：0.vp。|
|y|[Length](./cj-common-types.md#interface-length)|是|-|安全控件相对于自身布局位置的坐标偏移的y轴坐标。设置此属性不会影响父容器的布局，仅在绘制过程中调整位置。<br/>初始值：0.vp。|

### func fontSize(Length)

```cangjie
public open func fontSize(size: Length): This
```

**功能：** 设置安全控件上文字的尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|是|-|安全控件上文字的尺寸。<br/>初始值：16.fp。|