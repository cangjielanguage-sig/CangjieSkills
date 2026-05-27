### class DigitIndicator

```cangjie
public class DigitIndicator <: Indicator {
    public init()
}
```

**功能：** 构造数字指示器的样式。

> **说明：**
>
> 按组翻页时，数字导航点显示的子节点数量，不包括占位节点。数字导航点文本最大的字体缩放倍数[maxFontScale](./cj-text-input-text.md#func-maxfontscalefloat32)为2。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [Indicator](#class-indicator)

#### init()

```cangjie
public init()
```

**功能：** DigitIndicator的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### func digitFont(FontOptions)

```cangjie
public func digitFont(value: FontOptions): This
```

**功能：** Swiper组件数字导航点的字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[FontOptions](#class-fontoptions)|是|-|置Swiper组件数字导航点的字体样式。|

#### func fontColor(ResourceColor)

```cangjie
public func fontColor(value: ResourceColor): This
```

**功能：** Swiper组件数字导航点的字体颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|设置Swiper组件数字导航点的字体颜色。<br>初始值：0xFF182431。|

#### func selectedDigitFont(FontOptions)

```cangjie
public func selectedDigitFont(value: FontOptions): This
```

**功能：** 选中Swiper组件数字导航点的字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[FontOptions](#class-fontoptions)|是|-|设置选中Swiper组件数字导航点的字体样式。<br>初始值：FontOptions(size: 14, weight: FontWeight.Normal)。|

#### func selectedFontColor(ResourceColor)

```cangjie
public func selectedFontColor(value: ResourceColor): This
```

**功能：** 选中Swiper组件数字导航点的字体颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|设置选中Swiper组件数字导航点的字体颜色。<br>初始值：0xFF182431。|