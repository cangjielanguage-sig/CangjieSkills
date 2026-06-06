### class SelectionOptions

```cangjie
public class SelectionOptions {
    public init(menuPolicy!: MenuPolicy = MenuPolicy.Default)
}
```

**功能：** 选中文字时的配置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(MenuPolicy)

```cangjie
public init(menuPolicy!: MenuPolicy = MenuPolicy.Default)
```

**功能：** 创建SelectionOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|menuPolicy|[MenuPolicy](./cj-common-types.md#enum-menupolicy)|否|MenuPolicy.Default| **命名参数。** 菜单弹出的策略。|

### enum TextAreaType

```cangjie
public enum TextAreaType {
    | NORMAL
    | NUMBER
    | PHONE_NUMBER
    | EMAIL
    | NUMBER_DECIMAL
    | URL
}
```

**功能：** 表示输入框类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### EMAIL

```cangjie
EMAIL
```

**功能：** 表示邮箱地址输入模式。支持数字，字母，下划线、小数点、!、#、$、%、&、'、*、+、-、/、=、?、^、`、{、|、}、~，以及@字符（只能存在一个@字符）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### NORMAL

```cangjie
NORMAL
```

**功能：** 表示基本输入模式。支持输入数字、字母、下划线、空格、特殊字符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### NUMBER

```cangjie
NUMBER
```

**功能：** 表示纯数字输入模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### NUMBER_DECIMAL

```cangjie
NUMBER_DECIMAL
```

**功能：** 表示带小数点的数字输入模式。支持数字、小数点（只能存在一个小数点）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### PHONE_NUMBER

```cangjie
PHONE_NUMBER
```

**功能：** 表示电话号码输入模式。支持输入数字、空格、+ 、-、*、#、(、)，长度不限。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### URL

```cangjie
URL
```

**功能：** 表示带URL的输入模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19