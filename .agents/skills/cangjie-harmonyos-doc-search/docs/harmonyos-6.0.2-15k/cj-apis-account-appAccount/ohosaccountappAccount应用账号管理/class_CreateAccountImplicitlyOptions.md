## class CreateAccountImplicitlyOptions

```cangjie
public class CreateAccountImplicitlyOptions {
    public CreateAccountImplicitlyOptions (
        public var requiredLabels!: ?Array<String>= None,
        public var authType!: ?String = None,
        public var parameters!: HashMap<String, AppAccountValueType>= HashMap<String, AppAccountValueType>()
    )
}
```

**功能：** 表示隐式创建账号的选项。

**系统能力：** SystemCapability.Account.AppAccount。

**起始版本：** 19

### var requiredLabels

```cangjie
public var requiredLabels: ?Array<String> = None
```

**功能：** 所需的标签，默认为空。

**类型：** ?Array\<String>

**读写能力：** 可读写

**起始版本：** 19

### var authType

```cangjie
public var authType: ?String = None
```

**功能：** 鉴权类型，默认为空。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var parameters

```cangjie
public var parameters: HashMap<String, AppAccountValueType> = HashMap<String, AppAccountValueType>()
```

**功能：** 自定义参数对象，默认为空。

**类型：** HashMap\<String, [AppAccountValueType](#enum-appaccountvaluetype)>

**读写能力：** 可读写

**起始版本：** 19

### CreateAccountImplicitlyOptions(?Array\<String>, ?String, HashMap\<String, AppAccountValueType>)

```cangjie
public CreateAccountImplicitlyOptions (
    public var requiredLabels!: ?Array<String>= None,
    public var authType!: ?String = None,
    public var parameters!: HashMap<String, AppAccountValueType>= HashMap<String, AppAccountValueType>()
)
```

**功能：** 构建CreateAccountImplicitlyOptions实例。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|requiredLabels|?Array\<String>|否|None| **命名参数。** 所需的标签，默认为空。|
|authType|?String|否|None| **命名参数。** 鉴权类型，默认为空。|
|parameters|HashMap\<String, [AppAccountValueType](#enum-appaccountvaluetype)>|否|HashMap\<String, AppAccountValueType>()| **命名参数。** 自定义参数对象，默认为空。|