#### init(?ResourceColor, ?Length, ?Length, ?ResourceColor, ?ResourceColor, ?Length, ?FontWeight)

```cangjie
public init(color!: ?ResourceColor = None, fontSize!: ?Length = None, badgeSize!: ?Length = None,
    badgeColor!: ?ResourceColor = None, borderColor!: ?ResourceColor = None,
    borderWidth!: ?Length = None, fontWeight!: ?FontWeight = None)
```

**功能：** 创建一个BadgeStyle对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None|**命名参数。** 文本颜色。初始值：Color.White|
|fontSize|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 文本大小。初始值：10.fp|
|badgeSize|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** badge的大小。初始值：16.vp|
|badgeColor|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None|**命名参数。** badge的颜色。初始值：Color.Red|
|borderColor|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None|**命名参数。** 底板描边颜色。初始值：Color.Red|
|borderWidth|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 底板描边粗细。初始值：1.vp|
|fontWeight|?[FontWeight](./cj-common-types.md#enum-fontweight)|否|None|**命名参数。** 设置文本的字体粗细。初始值：FontWeight.Normal|