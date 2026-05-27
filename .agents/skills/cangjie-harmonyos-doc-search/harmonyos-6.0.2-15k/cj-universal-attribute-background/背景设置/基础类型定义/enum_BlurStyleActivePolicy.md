### enum BlurStyleActivePolicy

```cangjie
public enum BlurStyleActivePolicy {
    | ALWAYS_ACTIVE
    | ALWAYS_INACTIVE
    | FOLLOWS_WINDOW_ACTIVE_STATE
}
```

**功能：** 模糊效果设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### ALWAYS_ACTIVE

```cangjie
ALWAYS_ACTIVE
```

**功能：** 一直有模糊效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### ALWAYS_INACTIVE

```cangjie
ALWAYS_INACTIVE
```

**功能：** 一直无模糊效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### FOLLOWS_WINDOW_ACTIVE_STATE

```cangjie
FOLLOWS_WINDOW_ACTIVE_STATE
```

**功能：** 模糊效果跟随窗口焦点状态变化，非焦点不模糊，焦点模糊。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### getValue

```cangjie
public getValue(): Int32
```

**功能：** 获取枚举的数值类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
| :-------   | :---------- |
| Int32   |  枚举的数值。  |