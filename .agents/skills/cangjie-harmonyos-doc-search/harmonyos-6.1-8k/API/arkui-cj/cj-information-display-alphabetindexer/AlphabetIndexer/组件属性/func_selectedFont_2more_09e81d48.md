### func selectedFont(?Length, ?FontWeight, ?ResourceStr, ?FontStyle)

```cangjie
public func selectedFont(
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
|weight|?[FontWeight](./cj-common-types.md#enum-fontweight)|否|None|**命名参数。** 选中项文字字体粗细。初始值: FontWeight.Normal|
|family|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None|**命名参数。** 选中项文字字体家族。初始值: "HarmonyOS Sans"|
|style|?[FontStyle](./cj-common-types.md#enum-fontstyle)|否|None|**命名参数。** 选中项文字样式。初始值: FontStyle.Normal|

### func usingPopup(?Bool)

```cangjie
public func usingPopup(value: ?Bool): This
```

**功能：** 设置是否使用提示弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-|是否使用提示弹窗。<br/>初始值: false|