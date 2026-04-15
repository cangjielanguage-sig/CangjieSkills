## class Font

```cangjie
public class Font {
    public var size: ?Length
    public var weight: ?FontWeight
    public var family: ?ResourceStr
    public var style: ?FontStyle
    public init(size!: ?Length = None, weight!: ?FontWeight = None, family!: ?ResourceStr = None, style!: ?FontStyle = None)
}
```

**功能：** 字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var size

```cangjie
public var size: ?Length
```

**功能：** 设置文本尺寸，使用fp单位。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var weight

```cangjie
public var weight: ?FontWeight
```

**功能：** 设置文本的字体粗细。

**类型：** ?[FontWeight](#enum-fontweight)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var family

```cangjie
public var family: ?ResourceStr
```

**功能：** 设置文本的字体列表。

**类型：** ?[ResourceStr](#interface-resourcestr)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var style

```cangjie
public var style: ?FontStyle
```

**功能：** 设置文本的字体样式。

**类型：** ?[FontStyle](#enum-fontstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?Length, ?FontWeight, ?ResourceStr, ?FontStyle)

```cangjie
public init(size!: ?Length = None, weight!: ?FontWeight = None, family!: ?ResourceStr = None, style!: ?FontStyle = None)
```

**功能：** 构造一个Font对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 设置文本尺寸，Length为Int64、Float64类型时，使用fp单位。不支持百分比设置。初始值为16.fp。|
|weight|?[FontWeight](./cj-common-types.md#enum-fontweight)|否|None|**命名参数。** 设置文本的字体粗细。初始值为FontWeight.Normal。|
|family|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None|**命名参数。**设置文本的字体列表。使用多个字体，使用','进行分割，优先级按顺序生效。例如：'Arial, HarmonyOS Sans'。初始值为"HarmonyOS Sans"。|
|style|?[FontStyle](./cj-common-types.md#enum-fontstyle)|否|None|**命名参数。** 设置文本的字体样式。初始值为FontStyle.Normal。|