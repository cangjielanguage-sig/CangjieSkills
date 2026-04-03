## enum OnOffType

```cangjie
public enum OnOffType <: Equatable<OnOffType> & ToString {
    | OPEN
    | MESSAGE
    | CLOSE
    | ERROR
    | DATAEND
    | HEADERRECEIVE
    | ...
}
```

**功能：** WebSocket的订阅事件类型。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**父类型：**

- Equatable\<OnOffType>
- ToString

### CLOSE

```cangjie
CLOSE
```

**功能：** 关闭事件类型。

**起始版本：** 19

### DATAEND

```cangjie
DATAEND
```

**功能：** 数据接收结束事件类型。

**起始版本：** 19

### ERROR

```cangjie
ERROR
```

**功能：** Error事件类型。

**起始版本：** 19

### HEADERRECEIVE

```cangjie
HEADERRECEIVE
```

**功能：** HTTP Response Header事件类型。

**起始版本：** 19

### MESSAGE

```cangjie
MESSAGE
```

**功能：** 服务器消息事件类型。

**起始版本：** 19

### OPEN

```cangjie
OPEN
```

**功能：** 打开事件类型。

**起始版本：** 19

### func !=(OnOffType)

```cangjie
public operator func !=(other: OnOffType): Bool
```

**功能：** 对WebSocket的订阅事件类型进行判不等。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[OnOffType](#enum-onofftype)|是|-|WebSocket的订阅事件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果订阅事件类型不同，返回 true，否则返回 false。|

### func ==(OnOffType)

```cangjie
public operator func ==(other: OnOffType): Bool
```

**功能：** 对WebSocket的订阅事件类型进行判等。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[OnOffType](#enum-onofftype)|是|-|WebSocket的订阅事件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果订阅事件类型相同，返回 true，否则返回 false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回字符串形式的[OnOffType](#enum-onofftype)。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|字符串。|