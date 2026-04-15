## enum ShadowStyle

```cangjie
public enum ShadowStyle <: Equatable<ShadowStyle> {
    | OuterDefaultXS
    | OuterDefaultSM
    | OuterDefaultMD
    | OuterDefaultLG
    | OuterFloatingSM
    | OuterFloatingMD
    | ...
}
```

**功能：** 阴影样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ShadowStyle](#enum-shadowstyle)>

### OuterDefaultXS

```cangjie
OuterDefaultXS
```

**功能：** 超小阴影。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### OuterDefaultSM

```cangjie
OuterDefaultSM
```

**功能：** 小阴影。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### OuterDefaultMD

```cangjie
OuterDefaultMD
```

**功能：** 中阴影。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### OuterDefaultLG

```cangjie
OuterDefaultLG
```

**功能：** 大阴影。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### OuterFloatingSM

```cangjie
OuterFloatingSM
```

**功能：** 浮动小阴影。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### OuterFloatingMD

```cangjie
OuterFloatingMD
```

**功能：** 浮动中阴影。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ShadowStyle)

```cangjie
public operator func ==(other: ShadowStyle): Bool
```

**功能：** 判断两个ShadowStyle枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ShadowStyle](#enum-shadowstyle)|是|-|要比较的另一个ShadowStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ShadowStyle)

```cangjie
public operator func !=(other: ShadowStyle): Bool
```

**功能：** 判断两个ShadowStyle枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ShadowStyle](#enum-shadowstyle)|是|-|要比较的另一个ShadowStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|