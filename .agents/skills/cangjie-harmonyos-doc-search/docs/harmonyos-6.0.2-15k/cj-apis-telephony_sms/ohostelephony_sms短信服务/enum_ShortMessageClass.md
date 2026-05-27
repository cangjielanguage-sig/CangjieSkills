## enum ShortMessageClass

```cangjie
public enum ShortMessageClass <: Equatable<ShortMessageClass> & ToString {
    | UNKNOWN
    | INSTANT_MESSAGE
    | OPTIONAL_MESSAGE
    | SIM_MESSAGE
    | FORWARD_MESSAGE
    | ...
}
```

**功能：** 短信类型。

**系统能力：** SystemCapability.Telephony.SmsMms

**起始版本：** 19

**父类型：**

- Equatable\<[ShortMessageClass](#enum-shortmessageclass)>
- ToString

### FORWARD_MESSAGE

```cangjie
FORWARD_MESSAGE
```

**功能：** 要转发到另一台设备的短信。

**起始版本：** 19

### INSTANT_MESSAGE

```cangjie
INSTANT_MESSAGE
```

**功能：** 即时消息，收到后立即显示。

**起始版本：** 19

### OPTIONAL_MESSAGE

```cangjie
OPTIONAL_MESSAGE
```

**功能：** 存储在设备或SIM卡上的短信。

**起始版本：** 19

### SIM_MESSAGE

```cangjie
SIM_MESSAGE
```

**功能：** 包含SIM卡信息的短信，需要存储在SIM卡中。

**起始版本：** 19

### UNKNOWN

```cangjie
UNKNOWN
```

**功能：** 未知类型。

**起始版本：** 19

### func !=(ShortMessageClass)

```cangjie
public operator func !=(other: ShortMessageClass): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Telephony.SmsMms

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ShortMessageClass](#enum-shortmessageclass)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值是否不相等。|

### func ==(ShortMessageClass)

```cangjie
public operator func ==(other: ShortMessageClass): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Telephony.SmsMms

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ShortMessageClass](#enum-shortmessageclass)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值是否相等。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回字符串值。

**系统能力：** SystemCapability.Telephony.SmsMms

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回字符串值。|