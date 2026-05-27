### class TabBarIconStyle

```cangjie
public class TabBarIconStyle {
    public let unselectedColor: UInt32
    public let selectedColor: UInt32
    public TabBarIconStyle(
        unselectedColor!: ResourceColor = 0x33182431,
        selectedColor!: ResourceColor = 0xFF007DFF
    )
}
```

**功能：** Label图标样式对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let selectedColor

```cangjie
public let selectedColor: UInt32
```

**功能：** 设置Label图标选中时的颜色。

**类型：** UInt32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let unselectedColor

```cangjie
public let unselectedColor: UInt32
```

**功能：** 设置Label图标未选中时的颜色。

**类型：** UInt32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### TabBarIconStyle(ResourceColor, ResourceColor)

```cangjie
public TabBarIconStyle(
    unselectedColor!: ResourceColor = 0x33182431,
    selectedColor!: ResourceColor = 0xFF007DFF
)
```

**功能：** 构造一个TabBarIconStyle对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|unselectedColor|[ResourceColor](cj-common-types.md#interface-resourcecolor)|否|0x33182431| **命名参数。** 设置Label图标未选中时的颜色。<br> **说明：** <br> 仅对svg图源生效，设置后会替换svg图片的填充颜色。|
|selectedColor|[ResourceColor](cj-common-types.md#interface-resourcecolor)|否|0xFF007DFF| **命名参数。** 设置Label图标选中时的颜色。<br> **说明：** <br> 仅对svg图源生效，设置后会替换svg图片的填充颜色。|

### enum LayoutMode

```cangjie
public enum LayoutMode {
    | AUTO
    | VERTICAL
    | HORIZONTAL
}
```

**功能：** 页签内容排布方式枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### AUTO

```cangjie
AUTO
```

**功能：** 若页签宽度大于104.vp，页签内容为左右排布，否则页签内容为上下排布。仅TabBar为垂直模式或Fixed水平模式时有效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### HORIZONTAL

```cangjie
HORIZONTAL
```

**功能：** 页签内容左右排布。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### VERTICAL

```cangjie
VERTICAL
```

**功能：** 页签内容上下排布。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum SelectedMode

```cangjie
public enum SelectedMode {
    | INDICATOR
    | BOARD
}
```

**功能：** 选中子页签的显示模式枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### BOARD

```cangjie
BOARD
```

**功能：** 使用背板模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### INDICATOR

```cangjie
INDICATOR
```

**功能：** 使用下划线模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19