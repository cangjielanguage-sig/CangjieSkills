## enum EncodingType

```cangjie
public enum EncodingType <: Equatable<EncodingType> & ToString {
    | ENCODING_UTF8
    | ...
}
```

**功能：** 表示获取X509证书主体名称编码格式。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**父类型：**

- Equatable\<EncodingType>
- ToString

### ENCODING_UTF8

```cangjie
ENCODING_UTF8
```

**功能：** UTF8编码格式。

**起始版本：** 19

### func !=(EncodingType)

```cangjie
public operator func !=(other: EncodingType): Bool
```

**功能：** 对X509证书主体名称编码格式进行判不等。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[EncodingType](#enum-encodingtype)|是|X509证书主体名称编码格式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果X509证书主体名称编码格式不同，返回true，否则返回false。|

### func ==(EncodingType)

```cangjie
public operator func ==(other: EncodingType): Bool
```

**功能：** 对X509证书主体名称编码格式进行判等。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[EncodingType](#enum-encodingtype)|是|X509证书主体名称编码格式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果X509证书主体名称编码格式相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回X509证书主体名称编码格式的字符串表示。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|X509证书主体名称编码格式的字符串表示。|