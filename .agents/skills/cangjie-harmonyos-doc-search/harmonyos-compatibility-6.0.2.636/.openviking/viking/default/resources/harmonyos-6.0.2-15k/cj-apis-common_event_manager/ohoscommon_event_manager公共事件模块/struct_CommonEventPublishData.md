## struct CommonEventPublishData

```cangjie
public struct CommonEventPublishData {
    public CommonEventPublishData (
        public let bundleName: String,
        public let data: String,
        public let code: Int32,
        public let subscriberPermissions!: Array<String> = Array<String>(),
        public let isOrdered!: Bool = false,
        public let isSticky!: Bool = false,
        public let parameters!: HashMap<String, ValueType> = HashMap<String, ValueType>()
    )
}
```

**功能：** 包含公共事件内容和属性。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 12

### let bundleName

```cangjie
public let bundleName: String
```

**功能：** 表示订阅者包名称，只有包名为bundleName的订阅者才能收到该公共事件。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let code

```cangjie
public let code: Int32
```

**功能：** 表示公共事件的结果代码。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let data

```cangjie
public let data: String
```

**功能：** 表示公共事件的自定义结果数据。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let isOrdered

```cangjie
public let isOrdered: Bool = false
```

**功能：** 表示是否是有序事件。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let isSticky

```cangjie
public let isSticky: Bool = false
```

**功能：** 表示是否是粘性事件。仅系统应用或系统服务允许发送粘性事件。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let parameters

```cangjie
public let parameters: HashMap<String, ValueType> = HashMap<String, ValueType>()
```

**功能：** 表示公共事件的附加信息。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** HashMap\<String, [ValueType](#enum-valuetype)>

**读写能力：** 只读

**起始版本：** 12

### let subscriberPermissions

```cangjie
public let subscriberPermissions: Array<String> = Array<String>()
```

**功能：** 表示订阅者的权限。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 12

### CommonEventPublishData(String, String, Int32, Array\<String>, Bool, Bool, HashMap\<String, ValueType>)

```cangjie
public CommonEventPublishData (
    let bundleName: String,
        let data: String,
        let code: Int32,
        let subscriberPermissions!: Array<String> = Array<String>(),
        let isOrdered!: Bool = false,
        let isSticky!: Bool = false,
        let parameters!: HashMap<String, ValueType> = HashMap<String, ValueType>()
)
```

**功能：** 构造CommonEventPublishData对象。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bundleName|String|是|-|表示订阅者包名称，只有包名为bundleName的订阅者才能收到该公共事件。|
|data|String|是|-|表示公共事件的自定义结果数据。|
|code|Int32|是|-|表示公共事件的结果代码。|
|subscriberPermissions|Array\<String>|否|Array\<String>()| **命名参数。** 表示订阅者的权限。|
|isOrdered|Bool|否|false| **命名参数。** 表示是否是有序事件。|
|isSticky|Bool|否|false| **命名参数。** 表示是否是粘性事件。仅系统应用或系统服务允许发送粘性事件。|
|parameters|HashMap\<String, [ValueType](#enum-valuetype)>|否|HashMap\<String, ValueType>()| **命名参数。** 表示公共事件的附加信息。|