## enum GeneralNameType

```cangjie
public enum GeneralNameType <: Equatable<GeneralNameType> & ToString {
    | GENERAL_NAME_TYPE_OTHER_NAME
    | GENERAL_NAME_TYPE_RFC822_NAME
    | GENERAL_NAME_TYPE_DNS_NAME
    | GENERAL_NAME_TYPE_X400_ADDRESS
    | GENERAL_NAME_TYPE_DIRECTORY_NAME
    | GENERAL_NAME_TYPE_EDI_PARTY_NAME
    | GENERAL_NAME_TYPE_UNIFORM_RESOURCE_ID
    | GENERAL_NAME_TYPE_IP_ADDRESS
    | GENERAL_NAME_TYPE_REGISTERED_ID
    | ...
}
```

**功能：** 表示证书主体用途 。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**父类型：**

- Equatable\<GeneralNameType>
- ToString

### GENERAL_NAME_TYPE_DIRECTORY_NAME

```cangjie
GENERAL_NAME_TYPE_DIRECTORY_NAME
```

**功能：** 表示一个目录名称。

**起始版本：** 19

### GENERAL_NAME_TYPE_DNS_NAME

```cangjie
GENERAL_NAME_TYPE_DNS_NAME
```

**功能：** 表示一个DNS名称。

**起始版本：** 19

### GENERAL_NAME_TYPE_EDI_PARTY_NAME

```cangjie
GENERAL_NAME_TYPE_EDI_PARTY_NAME
```

**功能：** 表示特定的EDI实体。

**起始版本：** 19

### GENERAL_NAME_TYPE_IP_ADDRESS

```cangjie
GENERAL_NAME_TYPE_IP_ADDRESS
```

**功能：** 表示一个IP地址。

**起始版本：** 19

### GENERAL_NAME_TYPE_OTHER_NAME

```cangjie
GENERAL_NAME_TYPE_OTHER_NAME
```

**功能：** 表示其他名称。

**起始版本：** 19

### GENERAL_NAME_TYPE_REGISTERED_ID

```cangjie
GENERAL_NAME_TYPE_REGISTERED_ID
```

**功能：** 表示一个已注册的对象标识符。

**起始版本：** 19

### GENERAL_NAME_TYPE_RFC822_NAME

```cangjie
GENERAL_NAME_TYPE_RFC822_NAME
```

**功能：** 表示电子邮件地址。

**起始版本：** 19

### GENERAL_NAME_TYPE_UNIFORM_RESOURCE_ID

```cangjie
GENERAL_NAME_TYPE_UNIFORM_RESOURCE_ID
```

**功能：** 表示一个统一资源标识符。

**起始版本：** 19

### GENERAL_NAME_TYPE_X400_ADDRESS

```cangjie
GENERAL_NAME_TYPE_X400_ADDRESS
```

**功能：** 表示X.400地址。

**起始版本：** 19

### func !=(GeneralNameType)

```cangjie
public operator func !=(other: GeneralNameType): Bool
```

**功能：** 对证书主体用途进行判不等。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[GeneralNameType](#enum-generalnametype)|是|证书主体用途。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果证书主体用途不同，返回true，否则返回false。|

### func ==(GeneralNameType)

```cangjie
public operator func ==(other: GeneralNameType): Bool
```

**功能：** 对证书主体用途进行判等。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[GeneralNameType](#enum-generalnametype)|是|证书主体用途。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果证书主体用途相同，返回true，否则返回false。|

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取当前枚举的所表示的值。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|当前枚举所表示的值。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回证书主体用途的字符串表示。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|证书主体用途的字符串表示。|