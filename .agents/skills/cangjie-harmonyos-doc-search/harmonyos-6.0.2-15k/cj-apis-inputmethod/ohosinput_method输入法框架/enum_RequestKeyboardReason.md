## enum RequestKeyboardReason

```cangjie
public enum RequestKeyboardReason {
    | None
    | Mouse
    | Touch
    | Other
    | ...
}
```

**功能：** 请求键盘输入原因。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 20

### None

```cangjie
None
```

**功能：** 表示没有特定的原因触发键盘请求。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 20

**父类型：**

- Equatable\<RequestKeyboardReason>
- ToString

### Mouse

```cangjie
Mouse
```

**功能：** 表示键盘请求是由鼠标操作触发的。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 20

### Touch

```cangjie
Touch
```

**功能：** 表示键盘请求是由触摸操作触发的。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 20

### Other

```cangjie
Other
```

**功能：** 表示键盘请求是由其他原因触发的。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 20

### func !=(RequestKeyboardReason)

```cangjie
public operator func !=(other: RequestKeyboardReason): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[RequestKeyboardReason](#enum-requestkeyboardreason)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(RequestKeyboardReason)

```cangjie
public operator func ==(other: RequestKeyboardReason): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[RequestKeyboardReason](#enum-requestkeyboardreason)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取请求键盘输入原因的信息，以字符串表示。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|请求键盘输入原因的信息。|