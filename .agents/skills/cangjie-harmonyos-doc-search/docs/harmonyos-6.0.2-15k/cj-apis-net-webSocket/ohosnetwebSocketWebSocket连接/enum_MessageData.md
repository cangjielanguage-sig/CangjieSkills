## enum MessageData

```cangjie
public enum MessageData <: ToString {
    | STRING_DATA(String)
    | ARRAY_DATA(Array<Byte>)
    | ...
}
```

**功能：** 服务器消息事件的数据。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**父类型：**

- ToString

### ARRAY_DATA(Array\<Byte>)

```cangjie
ARRAY_DATA(Array<Byte>)
```

**功能：** 二进制数组。

**起始版本：** 19

### STRING_DATA(String)

```cangjie
STRING_DATA(String)
```

**功能：** 字符串。

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回字符串形式的[MessageData](#enum-messagedata)。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|字符串。|