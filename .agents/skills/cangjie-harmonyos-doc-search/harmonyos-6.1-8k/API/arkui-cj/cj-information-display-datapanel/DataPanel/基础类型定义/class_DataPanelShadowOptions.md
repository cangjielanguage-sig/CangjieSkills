### class DataPanelShadowOptions

```cangjie
public class DataPanelShadowOptions <: MultiShadowOptions {
    public var colors: ?Array<LinearGradient>
    public init(radius!: ?Length = None, colors!: ?Array<LinearGradient> = None, offsetX!: ?Length = None, offsetY!: ?Length = None)
}
```

**功能：** 投影样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [MultiShadowOptions](./cj-common-types.md#class-multishadowoptions)

#### var colors

```cangjie
public var colors: ?Array<LinearGradient>
```

**功能：** 各数据段投影的颜色。

> **说明：**
>
> - 若设置的投影颜色的个数少于数据段个数时，则显示的投影颜色的个数和设置的投影颜色个数一致。
> - 若设置的投影颜色的个数多于数据段个数时，则显示的投影颜色的个数和数据段个数一致。

**类型：** ?Array\<[LinearGradient](#class-lineargradient)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?Length, ?Array\<LinearGradient>, ?Length, ?Length)

```cangjie
public init(radius!: ?Length = None, colors!: ?Array<LinearGradient> = None, offsetX!: ?Length = None, offsetY!: ?Length = None)
```

**功能：** 创建DataPanelShadowOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|radius|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 初始值: 20.vp 投影模糊半径。|
|colors|?Array\<[LinearGradient](#class-lineargradient)>|否|None|**命名参数。** 初始值: [] 各数据段投影的颜色。<br>若设置的投影颜色的个数少于数据段个数时，则显示的投影颜色的个数和设置的投影颜色个数一致。<br>若设置的投影颜色的个数多于数据段个数时，则显示的投影颜色的个数和数据段个数一致。|
|offsetX|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 初始值: 5.vp X轴的偏移量。|
|offsetY|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 初始值: 5.vp Y轴的偏移量。|