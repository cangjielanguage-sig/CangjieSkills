## struct CommonEventData

```cangjie
public struct CommonEventData {
    public let event: String
    public let bundleName: String
    public let code: Int32
    public let data: String
    public let parameters: HashMap<String, ValueType>
}
```

**功能：** 公共事件的数据。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 12

### let bundleName

```cangjie
public let bundleName: String
```

**功能：** 表示包名称，当前默认为空。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let code

```cangjie
public let code: Int32
```

**功能：** 表示订阅者接收到的公共事件数据（Int32类型）。该字段取值与发布者使用[commonEventManager.publish](#static-func-publishstring)发布公共事件时，通过[CommonEventPublishData](#struct-commoneventpublishdata)中的`code`字段传递的数据一致。默认值为0。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let data

```cangjie
public let data: String
```

**功能：** 表示订阅者接收到的公共事件数据（string类型）。该字段取值与发布者使用[commonEventManager.publish](#static-func-publishstring)发布公共事件时，通过[CommonEventPublishData](#struct-commoneventpublishdata)中的`data`字段传递的数据一致。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let event

```cangjie
public let event: String
```

**功能：** 表示当前接收的公共事件名称。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let parameters

```cangjie
public let parameters: HashMap<String, ValueType>
```

**功能：** 表示订阅者接收到的公共事件的附加信息。该字段取值与发布者使用[commonEventManager.publish](#static-func-publishstring)发布公共事件时，通过[CommonEventPublishData](#struct-commoneventpublishdata)中的`parameters`字段传递的数据一致。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** HashMap\<String, [ValueType](#enum-valuetype)>

**读写能力：** 只读

**起始版本：** 12