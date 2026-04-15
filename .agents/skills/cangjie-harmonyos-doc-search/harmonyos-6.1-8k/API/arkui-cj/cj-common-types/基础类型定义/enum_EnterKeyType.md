## enum EnterKeyType

```cangjie
public enum EnterKeyType <: Equatable<EnterKeyType> {
    | Go
    | Search
    | Send
    | Next
    | Done
    | Previous
    | NewLine
    | ...
}
```

**功能：** 表示键盘操作按钮的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[EnterKeyType](#enum-enterkeytype)>

### Go

```cangjie
Go
```

**功能：** 显示为开始样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Search

```cangjie
Search
```

**功能：** 显示为搜索样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Send

```cangjie
Send
```

**功能：** c

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Next

```cangjie
Next
```

**功能：** 显示为下一步样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Done

```cangjie
Done
```

**功能：** 显示为完成样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Previous

```cangjie
Previous
```

**功能：** 显示为上一步样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### NewLine

```cangjie
NewLine
```

**功能：** 显示为换行样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(EnterKeyType)

```cangjie
public operator func ==(other: EnterKeyType): Bool
```

**功能：** 判断两个EnterKeyType枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[EnterKeyType](#enum-enterkeytype)|是|-|要比较的另一个EnterKeyType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(EnterKeyType)

```cangjie
public operator func !=(other: EnterKeyType): Bool
```

**功能：** 判断两个EnterKeyType枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[EnterKeyType](#enum-enterkeytype)|是|-|要比较的另一个EnterKeyType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|