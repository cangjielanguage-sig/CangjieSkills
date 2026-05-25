## class VerifyCredentialOptions

```cangjie
public class VerifyCredentialOptions {
    public VerifyCredentialOptions (
        public var credentialType!: String = "",
        public var credential!: String = "",
        public var parameters!: HashMap<String, AppAccountValueType>= HashMap<String, AppAccountValueType>()
    )
}
```

**功能：** 表示用于验证凭据的选项。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

### var credential

```cangjie
public var credential: String = ""
```

**功能：** 凭据取值，默认为空。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var credentialType

```cangjie
public var credentialType: String = ""
```

**功能：** 凭据类型，默认为空。

**类型：** String

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

### VerifyCredentialOptions(String, String, HashMap\<String, AppAccountValueType>)

```cangjie
public VerifyCredentialOptions (
    public var credentialType!: String = "",
    public var credential!: String = "",
    public var parameters!: HashMap<String, AppAccountValueType> = HashMap<String, AppAccountValueType>()
)
```

**功能：** 构建VerifyCredentialOptions实例。

**系统能力：** SystemCapability.Account.AppAccount。

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|credentialType|String|否|""| **命名参数。** 凭据类型，默认为空。|
|credential|String|否|""| **命名参数。** 凭据取值，默认为空。|
|parameters|HashMap\<String, [AppAccountValueType](#enum-appaccountvaluetype)>|否|HashMap\<String, AppAccountValueType>()| **命名参数。** 自定义参数对象，默认为空。|

## enum AppAccountValueType

```cangjie
public enum AppAccountValueType {
    | INT(Int32)
    | FLOAT64(Float64)
    | STRING(String)
    | BOOL(Bool)
    | FD(Int32)
    | ARRSTRING(Array<String>)
    | ARRAYI32(Array<Int32>)
    | ARRAYI64(Array<Int64>)
    | ARRAYBOOL(Array<Bool>)
    | ARRAYF64(Array<Float64>)
    | ARRAYFD(Array<Int32>)
    | ...
}
```

**功能：** 包含公共事件附加信息的类型取值。

**系统能力：** SystemCapability.Account.AppAccount。

**起始版本：** 19

### ARRAYBOOL(Array\<Bool>)

```cangjie
ARRAYBOOL(Array<Bool>)
```

**功能：** 表示Bool数组类型数据。

**起始版本：** 19

### ARRAYF64(Array\<Float64>)

```cangjie
ARRAYF64(Array<Float64>)
```

**功能：** 表示Int64数组类型数据。

**起始版本：** 19

### ARRAYFD(Array\<Int32>)

```cangjie
ARRAYFD(Array<Int32>)
```

**功能：** 表示文件描述符数组数据。

**起始版本：** 19

### ARRAYI32(Array\<Int32>)

```cangjie
ARRAYI32(Array<Int32>)
```

**功能：** 表示Int32数组类型数据。

**起始版本：** 19

### ARRAYI64(Array\<Int64>)

```cangjie
ARRAYI64(Array<Int64>)
```

**功能：** 表示Int64数组类型数据。

**起始版本：** 19

### ARRSTRING(Array\<String>)

```cangjie
ARRSTRING(Array<String>)
```

**功能：** 表示String数组类型数据。

**起始版本：** 19

### BOOL(Bool)

```cangjie
BOOL(Bool)
```

**功能：** 表示Bool类型数据。

**起始版本：** 19

### FD(Int32)

```cangjie
FD(Int32)
```

**功能：** 表示文件描述符数据。

**起始版本：** 19

### FLOAT64(Float64)

```cangjie
FLOAT64(Float64)
```

**功能：** 表示Float64类型数据。

**起始版本：** 19

### INT(Int32)

```cangjie
INT(Int32)
```

**功能：** 表示Int32类型数据。

**起始版本：** 19

### STRING(String)

```cangjie
STRING(String)
```

**功能：** 表示String类型数据。

**起始版本：** 19