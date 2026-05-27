## class SetPropertiesOptions

```cangjie
public class SetPropertiesOptions {
    public SetPropertiesOptions (
        public var properties!: HashMap<String, AppAccountValueType>= HashMap<String, AppAccountValueType>(),
        public var parameters!: HashMap<String, AppAccountValueType>= HashMap<String, AppAccountValueType>()
    )
}
```

**功能：** 表示用于设置属性的选项。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

### var parameters

```cangjie
public var parameters: HashMap<String, AppAccountValueType> = HashMap<String, AppAccountValueType>()
```

**功能：** 自定义参数对象，默认为空。

**类型：** HashMap\<String, [AppAccountValueType](#enum-appaccountvaluetype)>

**读写能力：** 可读写

**起始版本：** 19

### var properties

```cangjie
public var properties: HashMap<String, AppAccountValueType> = HashMap<String, AppAccountValueType>()
```

**功能：** 属性对象，默认为空。

**类型：** HashMap\<String, [AppAccountValueType](#enum-appaccountvaluetype)>

**读写能力：** 可读写

**起始版本：** 19

### SetPropertiesOptions(HashMap\<String, AppAccountValueType>, HashMap\<String, AppAccountValueType>)

```cangjie
public SetPropertiesOptions (
    public var properties!: HashMap<String, AppAccountValueType> = HashMap<String, AppAccountValueType>(),
    public var parameters!: HashMap<String, AppAccountValueType> = HashMap<String, AppAccountValueType>()
)
```

**功能：** 构建SetPropertiesOptions实例。

**系统能力：** SystemCapability.Account.AppAccount。

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|properties|HashMap\<String, [AppAccountValueType](#enum-appaccountvaluetype)>|否|HashMap\<String, AppAccountValueType>()| **命名参数。** 属性对象，默认为空。|
|parameters|HashMap\<String, [AppAccountValueType](#enum-appaccountvaluetype)>|否|HashMap\<String, AppAccountValueType>()| **命名参数。** 自定义参数对象，默认为空。|