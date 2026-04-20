### init(String, String, Int32, Array\<String>, Bool, Bool, HashMap\<String,CommonEventValueType>)

```cangjie
public init(
    bundleName!: String = "",
    data!: String = "",
    code!: Int32 = 0,
    subscriberPermissions!: Array<String> = Array<String>(),
    isOrdered!: Bool = false,
    isSticky!: Bool = false,
    parameters!: HashMap<String, CommonEventValueType> = HashMap<String, CommonEventValueType>()
)
```

**功能：** 构造CommonEventPublishData对象。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bundleName|String|否|""| **命名参数。** 表示订阅者包名称，只有包名为bundleName的订阅者才能收到该公共事件。|
|data|String|否|""| **命名参数。** 表示发布方传递的公共事件数据（String类型）。数据大小不超过64KB。|
|code|Int32|否|0| **命名参数。** 表示发布方传递的公共事件数据（Int32类型）。默认值为0。|
|subscriberPermissions|Array\<String>|否|Array\<String>()| **命名参数。** 表示订阅者的权限。|
|isOrdered|Bool|否|false| **命名参数。** 表示是否是有序事件。默认为false。|
|isSticky|Bool|否|false| **命名参数。** 表示是否是粘性事件。默认为false。|
|parameters|HashMap\<String, CommonEventValueType>|否|HashMap<String, CommonEventValueType>()| **命名参数。** 表示发布方传递的公共事件的附加信息。|