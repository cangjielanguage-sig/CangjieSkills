## class SendMessageOptions

```cangjie
public class SendMessageOptions {
    public SendMessageOptions(
        public let slotId: Int32,
        public let destinationHost: String,
        public let content: ContentType,
        public let serviceCenter!: String = "",
        public let destinationPort!: UInt16 = 0,
        public let sendCallback!: ?ISendShortMessageCallback = None,
        public let deliveryCallback!: ?IDeliveryShortMessageCallback = None
    )
}
```

**功能：** 发送短信的参数和回调。根据SendMessageOptions中的参数content的值判断短信类型。

**系统能力：** SystemCapability.Telephony.SmsMms

**起始版本：** 19

### let content

```cangjie
public let content: ContentType
```

**功能：** 如果内容是字符串，则这是一条文本短信。如果内容是字节数组，则这是一条数据短信。

**类型：** [ContentType](#enum-contenttype)

**读写能力：** 只读

**起始版本：** 19

### let deliveryCallback

```cangjie
public let deliveryCallback: ?IDeliveryShortMessageCallback = None
```

**功能：** 短信送达结果回调，返回短信递送报告。

**类型：** ?[IDeliveryShortMessageCallback](#type-ideliveryshortmessagecallback)

**读写能力：** 只读

**起始版本：** 19

### let destinationHost

```cangjie
public let destinationHost: String
```

**功能：** 短信的发送地址。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let destinationPort

```cangjie
public let destinationPort: UInt16 = 0
```

**功能：** 如果发送数据消息，destinationPort 是必需的。否则是可选的。

**类型：** UInt16

**读写能力：** 只读

**起始版本：** 19

### let sendCallback

```cangjie
public let sendCallback: ?ISendShortMessageCallback = None
```

**功能：** 短信发送结果回调，返回短信发送的结果。

**类型：** ?[ISendShortMessageCallback](#type-isendshortmessagecallback)

**读写能力：** 只读

**起始版本：** 19

### let serviceCenter

```cangjie
public let serviceCenter: String = ""
```

**功能：** 短信中心地址。默认使用SIM卡中的短信中心地址。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let slotId

```cangjie
public let slotId: Int32
```

**功能：** 用于发送短信的SIM卡槽ID：<br/>- 0：卡槽1。<br/>- 1：卡槽2。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### SendMessageOptions(Int32, String, ContentType, String, UInt16, ?ISendShortMessageCallback, ?IDeliveryShortMessageCallback)

```cangjie
public SendMessageOptions(
    public let slotId: Int32,
    public let destinationHost: String,
    public let content: ContentType,
    public let serviceCenter!: String = "",
    public let destinationPort!: UInt16 = 0,
    public let sendCallback!: ?ISendShortMessageCallback = None,
    public let deliveryCallback!: ?IDeliveryShortMessageCallback = None
)
```

**功能：** 构造函数。

**系统能力：** SystemCapability.Telephony.SmsMms

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotId|Int32|是|-|用于发送短信的SIM卡槽ID：<br/>- 0：卡槽1。<br/>- 1：卡槽2。|
|destinationHost|String|是|-|短信的发送地址。|
|content|[ContentType](#enum-contenttype)|是|-|如果内容是字符串，则这是一条文本短信。如果内容是字节数组，则这是一条数据短信。|
|serviceCenter|String|否|""| **命名参数。** 短信中心地址。默认使用SIM卡中的短信中心地址。|
|destinationPort|UInt16|否|0| **命名参数。** 如果发送数据消息，destinationPort 是必需的。否则是可选的。|
|sendCallback|?[ISendShortMessageCallback](#type-isendshortmessagecallback)|否|None| **命名参数。** 短信发送结果回调，返回短信发送的结果。|
|deliveryCallback|?[IDeliveryShortMessageCallback](#type-ideliveryshortmessagecallback)|否|None| **命名参数。** 短信送达结果回调，返回短信递送报告。|