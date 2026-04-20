### func alignStyle(?IndexerAlign)

```cangjie
public func alignStyle(value: ?IndexerAlign): This
```

**功能：** 设置字母索引条弹框的对齐样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[IndexerAlign](./cj-common-types.md#enum-indexeralign)|是|-|字母索引条弹框的对齐样式，支持索引条显示在弹窗左侧和右侧。初始值: IndexerAlign.Right|

### func color(?ResourceColor)

```cangjie
public func color(value: ?ResourceColor): This
```

**功能：** 设置未选中项文本颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|未选中项文本颜色。初始值: Color(0x99182431)|

### func font(?Length, ?FontWeight, ?ResourceStr, ?FontStyle)

```cangjie
public func font(
    size!: ?Length = None,
    weight!: ?FontWeight = None,
    family!: ?ResourceStr = None,
    style!: ?FontStyle = None
): This
```

**功能：** 设置选中项文字样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 选中项文字大小。初始值: 10.vp|
|weight|?[FontWeight](./cj-common-types.md#enum-fontweight)|否|None|**命名参数。** 选中文字字体粗细。初始值: FontWeight.Normal|
|family|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None|**命名参数。** 选中文字字体家族。初始值: "HarmonyOS Sans"|
|style|?[FontStyle](./cj-common-types.md#enum-fontstyle)|否|None|**命名参数。** 选中文字样式。初始值: FontStyle.Normal|

### func itemSize(?Length)

```cangjie
public func itemSize(value: ?Length): This
```

**功能：** 设置索引项区域大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[Length](./cj-common-types.md#interface-length)|是|-|索引项区域大小，索引项区域为正方形，即正方形边长。<br>不支持设置为百分比。初始值: 16.vp|

### func popupBackground(?ResourceColor)

```cangjie
public func popupBackground(value: ?ResourceColor): This
```

**功能：** 设置提示弹窗背景颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|提示弹窗背景颜色。初始值: Color(0x66808080)|

### func popupColor(?ResourceColor)

```cangjie
public func popupColor(value: ?ResourceColor): This
```

**功能：** 设置提示弹窗一级索引项文本颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|提示弹窗一级索引项文本颜色。初始值: Color(0xFF007DFF)|