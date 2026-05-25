### enum InputType

```cangjie
public enum InputType {
    | Normal
    | Number
    | Email
    | Password
    | PhoneNumber
    | USER_NAME
    | NEW_PASSWORD
    | NUMBER_PASSWORD
    | NUMBER_DECIMAL
    | URL
}
```

**功能：** 表示输入框的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Email

```cangjie
Email
```

**功能：** 表示e-mail地址输入模式，仅能输入标准邮箱格式支持的字符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### NEW_PASSWORD

```cangjie
NEW_PASSWORD
```

**功能：** 表示新密码输入模式。密码显示小眼睛图标，默认输入文字短暂显示后变成圆点，特定设备上输入文字直接显示为圆点。在已启用密码保险箱的情况下，支持自动生成新密码。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Normal

```cangjie
Normal
```

**功能：** 表示基本输入模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Number

```cangjie
Number
```

**功能：** 表示纯数字输入模式，仅能输入表示数字的字符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### NUMBER_DECIMAL

```cangjie
NUMBER_DECIMAL
```

**功能：** 表示带小数点的数字输入模式。支持数字、小数点（只能存在一个小数点）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### NUMBER_PASSWORD

```cangjie
NUMBER_PASSWORD
```

**功能：** 表示纯数字密码输入模式。密码显示小眼睛图标，默认输入文字短暂显示后变成圆点，特定设备上输入文字直接显示为圆点。密码输入模式不支持下划线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Password

```cangjie
Password
```

**功能：** 表示密码输入模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### PhoneNumber

```cangjie
PhoneNumber
```

**功能：** 表示电话号码输入模式。支持输入数字、空格、+ 、-、*、#、(、)，长度不限。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### URL

```cangjie
URL
```

**功能：** 表示带URL的输入模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### USER_NAME

```cangjie
USER_NAME
```

**功能：** 表示用户名输入模式。在已启用密码保险箱的情况下，支持用户名、密码的自动保存和自动填充。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19