### class DataPanelShadowOptions

```cangjie
public class DataPanelShadowOptions {
    public var radius: Length
    public var offsetX: Length
    public var offsetY: Length
    public var colors: Array<LinearGradient>
    public init(radius!: Length, colors!: Array<LinearGradient>, offsetX!: Length, offsetY!: Length)
}
```

**功能：** 投影样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var colors

```cangjie
public var colors: Array<LinearGradient>
```

**功能：** 各数据段投影的颜色。

> **说明：**
>
> - 若设置的投影颜色的个数少于数据段个数时，则显示的投影颜色的个数和设置的投影颜色个数一致。
> - 若设置的投影颜色的个数多于数据段个数时，则显示的投影颜色的个数和数据段个数一致。

**类型：** Array\<[LinearGradient](#class-lineargradient)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var offsetX

```cangjie
public var offsetX: Length
```

**功能：** X轴的偏移量。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var offsetY

```cangjie
public var offsetY: Length
```

**功能：** Y轴的偏移量。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var radius

```cangjie
public var radius: Length
```

**功能：** 投影模糊半径。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(Length, Array\<LinearGradient>, Length, Length)

```cangjie
public init(radius!: Length, colors!: Array<LinearGradient>, offsetX!: Length, offsetY!: Length)
```

**功能：** 投影样式描述。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|radius|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 投影模糊半径。|
|colors|Array\<[LinearGradient](#class-lineargradient)>|是|-| **命名参数。** 各数据段投影的颜色。<br>若设置的投影颜色的个数少于数据段个数时，则显示的投影颜色的个数和设置的投影颜色个数一致。<br>若设置的投影颜色的个数多于数据段个数时，则显示的投影颜色的个数和数据段个数一致。|
|offsetX|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** X轴的偏移量。|
|offsetY|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** Y轴的偏移量。|