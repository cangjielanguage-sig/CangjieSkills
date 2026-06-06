### init(String, Bool, String, String, Bool, Bool, Int64, Int64, Array\<String>, Array\<String>, Array\<AppEventReportConfig>)

```cangjie
public init(name: String, debugMode!: Bool = false, routeInfo!: String = "", appId!: String = "",
        onStartReport!: Bool = false, onBackgroundReport!: Bool = false, periodReport!: Int64 = 0, batchReport!: Int64 = 0,
        userIds!: Array<String> = [], userProperties!: Array<String> = [], eventConfigs!: Array<AppEventReportConfig> = [])
```

**功能：** 创建[Processor](#class-processor)实例。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|数据处理者的名称。名称只能包含大小写字母、数字、下划线和$，不能以数字开头，长度非空且不超过256个字符。|
|debugMode|Bool|否|false| **命名参数。** 是否开启debug模式，默认值为false。配置值为true表示开启debug模式，false表示不开启debug模式。|
|routeInfo|String|否|""| **命名参数。** 服务器位置信息，默认为空字符串。传入字符串长度不能超过8KB，超过时会被置为默认值。|
|appId|String|否|""| **命名参数。** 应用id，默认为空字符串。传入字符串长度不能超过8KB，超过时会被置为默认值。|
|onStartReport|Bool|否|false| **命名参数。** 数据处理者在启动时是否上报事件，默认值为false。配置值为true表示上报事件，false表示不上报事件。|
|onBackgroundReport|Bool|否|false| **命名参数。** 当应用程序进入后台时是否上报事件，默认值为false。配置值为true表示上报事件，false表示不上报事件。|
|periodReport|Int64|否|0| **命名参数。** 事件定时上报时间周期，单位为秒。传入数值必须大于或等于0，小于0时会被置为默认值0，不进行定时上报。|
|batchReport|Int64|否|0| **命名参数。** 事件上报阈值，当事件条数达到阈值时上报事件。传入数值必须大于0且小于1000，不在数值范围内会被置为默认值0，不进行上报。|
|userIds|Array\<String>|否|[]| **命名参数。** 数据处理者可以上报的用户ID的name数组。name对应[setUserId](#static-func-setuseridstring-string)接口的name参数。|
|userProperties|Array\<String>|否|[]| **命名参数。** 数据处理者可以上报的用户属性的name数组。name对应[setUserProperty](#static-func-setuserpropertystring-string)接口的name参数。|
|eventConfigs|Array\<[AppEventReportConfig](#struct-appeventreportconfig)>|否|[]| **命名参数。** 数据处理者可以上报的事件数组。|