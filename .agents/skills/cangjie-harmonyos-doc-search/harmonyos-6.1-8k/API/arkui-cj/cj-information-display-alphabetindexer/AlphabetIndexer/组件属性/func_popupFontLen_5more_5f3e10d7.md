### func popupFont(?Length, ?FontWeight, ?ResourceStr, ?FontStyle)

```cangjie
public func popupFont(
    size!: ?Length = None,
    weight!: ?FontWeight = None,
    family!: ?ResourceStr = None,
    style!: ?FontStyle = None
): This
```

**功能：** 设置提示弹窗字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 提示弹窗文字大小。初始值: 24.vp|
|weight|?[FontWeight](./cj-common-types.md#enum-fontweight)|否|None|**命名参数。** 提示弹窗文字字体粗细。初始值: FontWeight.Normal|
|family|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None|**命名参数。** 提示弹窗文字字体家族。初始值: "HarmonyOS Sans"|
|style|?[FontStyle](./cj-common-types.md#enum-fontstyle)|否|None|**命名参数。** 提示弹窗文字样式。初始值: FontStyle.Normal|

### func popupPosition(?Length, ?Length)

```cangjie
public func popupPosition(x!: ?Length = None, y!: ?Length = None): This
```

**功能：** 设置弹出窗口相对于索引条上边框中点的位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 弹出窗口相对于索引条上边框中点的x坐标。初始值: 60.vp|
|y|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 弹出窗口相对于索引条上边框中点的y坐标。初始值: 48.vp|

### func selected(?Int32)

```cangjie
public func selected(index: ?Int32): This
```

**功能：** 设置选中项索引值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|?Int32|是|-|选中项索引值。初始值: 0|

### func selectedBackgroundColor(?ResourceColor)

```cangjie
public func selectedBackgroundColor(value: ?ResourceColor): This
```

**功能：** 设置选中项背景颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|选中项背景颜色。初始值: Color(0x1A007DFF)|

### func selectedColor(?ResourceColor)

```cangjie
public func selectedColor(value: ?ResourceColor): This
```

**功能：** 设置选中项文字颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|选中项文字颜色。初始值: Color(0xFF007DFF)|