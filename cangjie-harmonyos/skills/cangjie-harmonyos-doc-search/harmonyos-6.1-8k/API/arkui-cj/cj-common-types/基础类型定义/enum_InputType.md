## enum InputType

```cangjie
public enum InputType <: Equatable<InputType> {
    | Normal
    | Number
    | Email
    | Password
    | PhoneNumber
    | ...
}
```

**功能：** 表示输入框的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[InputType](#enum-inputtype)>

### Normal

```cangjie
Normal
```

**功能：** 表示基本输入模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Number

```cangjie
Number
```

**功能：** 表示纯数字输入模式，仅能输入表示数字的字符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Email

```cangjie
Email
```

**功能：** mail地址输入模式，仅能输入标准邮箱格式支持的字符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Password

```cangjie
Password
```

**功能：** 表示密码输入模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### PhoneNumber

```cangjie
PhoneNumber
```

**功能：** 表示电话号码输入模式。支持输入数字、空格、+ 、-、*、#、(、)，长度不限。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(InputType)

```cangjie
public operator func ==(other: InputType): Bool
```

**功能：** 判断两个InputType枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[InputType](#enum-inputtype)|是|-|要比较的另一个InputType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(InputType)

```cangjie
public operator func !=(other: InputType): Bool
```

**功能：** 判断两个InputType枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[InputType](#enum-inputtype)|是|-|要比较的另一个InputType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|