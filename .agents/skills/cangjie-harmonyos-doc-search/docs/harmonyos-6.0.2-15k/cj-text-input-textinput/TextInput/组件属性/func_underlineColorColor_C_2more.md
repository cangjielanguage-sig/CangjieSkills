### func underlineColor(?Color, ?Color, ?Color, ?Color)

```cangjie
public func underlineColor(typing!: ?Color = None, normal!: ?Color = None,error!: ?Color = None, disable!: ?Color = None): This
```

**功能：** 开启下划线时，支持配置下划线颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|typing|?[Color](./cj-common-types.md#class-color)|否|None| **命名参数。** 键入时下划线颜色。不填写、无效值时恢复默认。|
|normal|?[Color](./cj-common-types.md#class-color)|否|None| **命名参数。** 非特殊状态时下划线颜色。不填写、无效值时恢复默认。|
|error|?[Color](./cj-common-types.md#class-color)|否|None|错误时下划线颜色。不填写、无效值时恢复默认。此选项会修改[showCounter](#func-showcounterbool-float64-bool)属性中达到最大字符数时的颜色。|
|disable|?[Color](./cj-common-types.md#class-color)|否|None| **命名参数。** 禁用时下划线颜色。不填写、无效值时恢复默认。|

### func wordBreak(WordBreak)

```cangjie
public func wordBreak(value: WordBreak): This
```

**功能：** 设置文本断行规则。该属性在组件设置内联模式时样式生效，但对placeholder文本无效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[WordBreak](./cj-common-types.md#enum-wordbreak)|是|-|内联输入风格编辑态时断行规则。<br>初始值：WordBreak.BREAK_WORD。|