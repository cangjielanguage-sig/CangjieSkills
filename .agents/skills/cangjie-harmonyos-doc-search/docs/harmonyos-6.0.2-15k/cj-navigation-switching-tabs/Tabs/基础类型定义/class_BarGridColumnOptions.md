### class BarGridColumnOptions

```cangjie
public class BarGridColumnOptions {
    public let margin: Length
    public let gutter: Length
    public let sm: Int32
    public let md: Int32
    public let lg: Int32
    public init(margin!: Length = 24.0.vp, gutter!: Length = 24.0.vp, sm!: Int32 = -1, md!: Int32 = -1, lg!: Int32 = -1)
}
```

**功能：** TabBar栅格化方式设置的对象，包括栅格模式下的column边距和间隔，以及小、中、大屏下，页签占用的columns数量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let gutter

```cangjie
public let gutter: Length
```

**功能：** 栅格模式下的column间隔（不支持百分比设置）。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let lg

```cangjie
public let lg: Int32
```

**功能：** 大屏下，页签占用的columns数量，必须是非负偶数。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let margin

```cangjie
public let margin: Length
```

**功能：** 栅格模式下的column边距（不支持百分比设置）。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let md

```cangjie
public let md: Int32
```

**功能：** 中屏下，页签占用的columns数量，必须是非负偶数。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let sm

```cangjie
public let sm: Int32
```

**功能：** 小屏下，页签占用的columns数量，必须是非负偶数。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Length, Length, Int32, Int32, Int32)

```cangjie
public init(margin!: Length = 24.0.vp, gutter!: Length = 24.0.vp, sm!: Int32 = -1, md!: Int32 = -1, lg!: Int32 = -1)
```

**功能：** 构造一个BarGridColumnOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|margin|[Length](cj-common-types.md#interface-length)|否|24.0.vp| **命名参数。** 栅格模式下的column边距（不支持百分比设置）。|
|gutter|[Length](cj-common-types.md#interface-length)|否|24.0.vp| **命名参数。** 栅格模式下的column间隔（不支持百分比设置）。|
|sm|Int32|否|- 1| **命名参数。** 小屏下，页签占用的columns数量，必须是非负偶数。小屏为大于等于320.vp但小于600.vp。<br> 初始值为-1，代表页签占用TabBar全部宽度。|
|md|Int32|否|- 1| **命名参数。** 中屏下，页签占用的columns数量，必须是非负偶数。中屏为大于等于600.vp但小于800.vp。<br> 初始值为-1，代表页签占用TabBar全部宽度。|
|lg|Int32|否|- 1| **命名参数。** 大屏下，页签占用的columns数量，必须是非负偶数。大屏为大于等于840.vp但小于1024.vp。<br> 初始值为-1，代表页签占用TabBar全部宽度。|