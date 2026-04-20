### init(String, String, String, String, UInt32, String, String, Array\<String>, String, HashMap\<String,WantValueType>, HashMap\<String,Int32>)

```cangjie
public init(
    deviceId!: String = "",
    bundleName!: String = "",
    abilityName!: String = "",
    moduleName!: String = "",
    flags!: UInt32 = 0,
    uri!: String = "",
    action!: String = "",
    entities!: Array<String> = [],
    dataType!: String = "",
    parameters!: HashMap<String, WantValueType> = HashMap<String, WantValueType>(),
    fds!: HashMap<String, Int32> = HashMap<String, Int32>()
)
```

**功能：** 构造函数，创建Want实例。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deviceId|String|否|""|**命名参数。** 设备ID。在应用启动场景中表示被拉起方的设备ID，如果未设置该字段，则表示指定当前设备。|
|bundleName|String|否|""|**命名参数。** 应用包名。在应用启动场景中表示被拉起方的应用包名。|
|abilityName|String|否|""|**命名参数。** 应用的Ability组件名。在应用启动场景中表示被拉起方的Ability组件名。如果在Want中该字段同时指定了BundleName和AbilityName，则Want可以直接匹配到指定的Ability。AbilityName需要在一个应用的范围内保证唯一。|
|moduleName|String|否|""|**命名参数。** 应用模块名。在应用启动场景中表示被拉起方的应用模块名。|
|flags|UInt32|否|0|**命名参数。** 表示处理Want的方式。值为枚举类型[Flags](./cj-apis-app-ability-want_constant.md#class-flags)，默认传数字。<br />例如取值为0x00000001（即Flags.FLAG_AUTH_READ_URI_PERMISSION）表示临时授予接收方读取该URI指向的数据的权限。|
|uri|String|否|""|**命名参数。** 统一资源标识符，一般在应用启动场景中配合type使用，指明待处理的数据类型。如果在Want中指定了uri，则Want将匹配指定的Uri信息，包括`scheme`、`schemeSpecificPart`、`authority`和`path`信息。|
|action|String|否|""|**命名参数。** 表示要执行的通用操作（如：查看、分享、应用详情）。在隐式Want中，开发者可以定义该字段，配合uri或parameters来表示对数据执行的操作。隐式Want定义及匹配规则请参见[显式Want与隐式Want匹配规则](../../application-models/cj-explicit-implicit-want-mappings.md)。|
|entities|Array\<String>|否|[]|**命名参数。** 表示目标Ability额外的类别信息（如：浏览器、视频播放器）。在隐式Want中是对action字段的补充。在隐式Want中，开发者可以定义该字段，来过滤匹配Ability类型。|
|dataType|String|否|""|**命名参数。** 表示MIME type类型描述，打开文件的类型，主要用于文管打开文件。比如：'text/xml' 、 'image/*'等，MIME定义请参见[Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml?utm_source=ld246.com)。|
|parameters|HashMap\<String,[WantValueType](#enum-wantvaluetype)>|否|HashMap<String, WantValueType>()|**命名参数。** 表示WantParams描述。|
|fds|HashMap\<String,Int32>|否|HashMap<String, Int32>()|**命名参数。** 表示文件描述符，在启动场景中拉起方写入的FD，会设置到该参数中。|

**异常：**

- BusinessException：对应错误码如下表，详见[元能力子系统错误码](./cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 16000050 | Internal error. |