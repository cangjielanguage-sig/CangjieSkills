## class ShortMessage

```cangjie
public class ShortMessage {
    public let hasReplyPath: Bool
    public let isReplaceMessage: Bool
    public let isSmsStatusReportMessage: Bool
    public let messageClass: ShortMessageClass
    public let pdu: Array<Int32>
    public let protocolId: Int32
    public let scAddress: String
    public let scTimestamp: Int64
    public let status: Int32
    public let visibleMessageBody: String
    public let visibleRawAddress: String
}
```

**功能：** 短信实例。

**系统能力：** SystemCapability.Telephony.SmsMms

**起始版本：** 19

### let hasReplyPath

```cangjie
public let hasReplyPath: Bool
```

**功能：** 收到的短信是否包含“TP-Reply-Path”，默认为false。<br/>“TP-Reply-Path”：设备根据发送SMS消息的短消息中心进行回复。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let isReplaceMessage

```cangjie
public let isReplaceMessage: Bool
```

**功能：** 收到的短信是否为“替换短信”，默认为false。<br/>“替换短信”有关详细信息，参见[“3GPP TS 23.040 9.2.3.9”](https://www.3gpp.org/ftp/specs/archive/23_series/23.040)。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let isSmsStatusReportMessage

```cangjie
public let isSmsStatusReportMessage: Bool
```

**功能：** 当前消息是否为“短信状态报告”，默认为false。<br/>“短信状态报告”是一种特定格式的短信，被用来从Service Center到Mobile Station传送状态报告。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let messageClass

```cangjie
public let messageClass: ShortMessageClass
```

**功能：** 短信类型。

**类型：** [ShortMessageClass](#enum-shortmessageclass)

**读写能力：** 只读

**起始版本：** 19

### let pdu

```cangjie
public let pdu: Array<Int32>
```

**功能：** SMS消息中的协议数据单元 （PDU）。

**类型：** Array\<Int32>

**读写能力：** 只读

**起始版本：** 19

### let protocolId

```cangjie
public let protocolId: Int32
```

**功能：** 发送短信时使用的协议标识。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let scAddress

```cangjie
public let scAddress: String
```

**功能：** 短消息服务中心（SMSC）地址。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let scTimestamp

```cangjie
public let scTimestamp: Int64
```

**功能：** SMSC时间戳。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 19

### let status

```cangjie
public let status: Int32
```

**功能：** SMS-STATUS-REPORT消息中的短信状态指示短信服务中心（SMSC）发送的短信状态。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let visibleMessageBody

```cangjie
public let visibleMessageBody: String
```

**功能：** 短信正文。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let visibleRawAddress

```cangjie
public let visibleRawAddress: String
```

**功能：** 发送者地址。

**类型：** String

**读写能力：** 只读

**起始版本：** 19