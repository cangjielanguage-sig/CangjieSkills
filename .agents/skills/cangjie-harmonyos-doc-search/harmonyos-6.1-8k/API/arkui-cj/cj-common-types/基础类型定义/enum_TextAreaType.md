## enum TextAreaType

```cangjie
public enum TextAreaType <: Equatable<TextAreaType> {
    | Normal
    | Number
    | PhoneNumber
    | Email
    | NumberDecimal
    | Url
    | ...
}
```

**功能：** 表示输入框类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[TextAreaType](#enum-textareatype)>

### Normal

```cangjie
Normal
```

**功能：** 表示基本输入模式。支持输入数字、字母、下划线、空格、特殊字符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Number

```cangjie
Number
```

**功能：** 表示纯数字输入模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### PhoneNumber

```cangjie
PhoneNumber
```

**功能：** 表示电话号码输入模式。支持输入数字、空格、+ 、-、*、#、(、)，长度不限。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Email

```cangjie
Email
```

**功能：** 表示邮箱地址输入模式。支持数字，字母，下划线、小数点、!、#、$、%、&、'、*、+、-、/、=、?、^、`、{、|、}、~，以及@字符（只能存在一个@字符）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### NumberDecimal

```cangjie
NumberDecimal
```

**功能：** 表示带小数点的数字输入模式。支持数字、小数点（只能存在一个小数点）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Url

```cangjie
Url
```

**功能：** 表示带URL的输入模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(TextAreaType)

```cangjie
public operator func ==(other: TextAreaType): Bool
```

**功能：** 判断两个TextAreaType枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TextAreaType](#enum-textareatype)|是|-|要比较的另一个TextAreaType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(TextAreaType)

```cangjie
public operator func !=(other: TextAreaType): Bool
```

**功能：** 判断两个TextAreaType枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TextAreaType](#enum-textareatype)|是|-|要比较的另一个TextAreaType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|