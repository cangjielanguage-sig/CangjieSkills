### func alignStyle(IndexerAlign)

```cangjie
public func alignStyle(align: IndexerAlign): This
```

**功能：** 设置字母索引条弹框的对齐样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|align|[IndexerAlign](#enum-indexeralign)|是|-|字母索引条弹框的对齐样式，支持索引条显示在弹窗左侧和右侧。<br>初始值：IndexerAlign.END。|

### func autoCollapse(Bool)

```cangjie
public func autoCollapse(value: Bool): This
```

**功能：** 设置是否使用自适应折叠模式。

> **说明：**
>
> - 如果字符串首字符为“#”，除去首字符。当剩余字符数 ≤ 9时，选择全显示模式。当9 < 剩余字符数 ≤ 13时，根据索引条高度自适应选择全显示模式或者短折叠模式。当剩余字符数 > 13时，根据索引条高度自适应选择短折叠模式或者长折叠模式。
> - 如果字符串首字符不为“#”。当所有字符数 ≤ 9时，选择全显示模式。当9 < 所有字符数 ≤ 13时，根据索引条高度自适应选择全显示模式或者短折叠模式。当所有字符数 > 13时，根据索引条高度自适应选择短折叠模式或者长折叠模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否使用自适应折叠模式。<br>初始值：true。|

### func color(ResourceColor)

```cangjie
public func color(value: ResourceColor): This
```

**功能：** 设置未选中项文本颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|未选中项文本颜色。<br>初始值：0x99182431。|

### func enableHapticFeedback(Bool)

```cangjie
public func enableHapticFeedback(value: Bool): This
```

**功能：** 设置支持触控反馈。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|支持触控反馈。<br>初始值：true。|

### func font(Length, FontWeight, String, FontStyle)

```cangjie
public func font(
    size!: Length = 10.vp,
    weight!: FontWeight = FontWeight.Normal,
    family!: String = "HarmonyOS Sans",
    style!: FontStyle = FontStyle.Normal
): This
```

**功能：** 设置选中项文字样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|否|10.vp| **命名参数。** 选中项文字大小。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Normal| **命名参数。** 选中项文字字体粗细。|
|family|String|否|"HarmonyOS Sans"| **命名参数。** 选中项文字字体家族。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 选中项文字样式。|