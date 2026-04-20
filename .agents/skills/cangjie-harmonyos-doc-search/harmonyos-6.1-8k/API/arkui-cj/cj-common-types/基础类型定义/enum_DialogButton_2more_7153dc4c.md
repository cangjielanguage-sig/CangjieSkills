## enum DialogButtonStyle

```cangjie
public enum DialogButtonStyle <: Equatable<DialogButtonStyle> {
    | Default
    | Highlight
    | ...
}
```

**功能：** 对话框按钮样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[DialogButtonStyle](#enum-dialogbuttonstyle)>

### Default

```cangjie
Default
```

**功能：** 白底蓝字（深色主题：白底=黑底）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Highlight

```cangjie
Highlight
```

**功能：** 蓝底白字。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(DialogButtonStyle)

```cangjie
public operator func ==(other: DialogButtonStyle): Bool
```

**功能：** 判断两个DialogButtonStyle枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DialogButtonStyle](#enum-dialogbuttonstyle)|是|-|要比较的另一个DialogButtonStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(DialogButtonStyle)

```cangjie
public operator func !=(other: DialogButtonStyle): Bool
```

**功能：** 判断两个DialogButtonStyle枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DialogButtonStyle](#enum-dialogbuttonstyle)|是|-|要比较的另一个DialogButtonStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum LengthMetricsUnit

```cangjie
public enum LengthMetricsUnit <: Equatable<LengthMetricsUnit> {
    | Default
    | Px
    | ...
}
```

**功能：** 长度度量单位枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[LengthMetricsUnit](#enum-lengthmetricsunit)>

### Default

```cangjie
Default
```

**功能：** 长度类型，用于描述以默认的vp像素单位为单位的长度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Px

```cangjie
Px
```

**功能：** 长度类型，用于描述以px像素单位为单位的长度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(LengthMetricsUnit)

```cangjie
public operator func ==(other: LengthMetricsUnit): Bool
```

**功能：** 判断两个LengthMetricsUnit枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[LengthMetricsUnit](#enum-lengthmetricsunit)|是|-|要比较的另一个LengthMetricsUnit枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(LengthMetricsUnit)

```cangjie
public operator func !=(other: LengthMetricsUnit): Bool
```

**功能：** 判断两个LengthMetricsUnit枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[LengthMetricsUnit](#enum-lengthmetricsunit)|是|-|要比较的另一个LengthMetricsUnit枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|