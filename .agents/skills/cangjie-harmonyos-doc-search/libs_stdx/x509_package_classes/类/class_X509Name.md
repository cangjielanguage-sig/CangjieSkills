## class X509Name

```cangjie
public class X509Name <: ToString {
    public init(
        countryName!: ?String = None,
        provinceName!: ?String = None,
        localityName!: ?String = None,
        organizationName!: ?String = None,
        organizationalUnitName!: ?String = None,
        commonName!: ?String = None,
        email!: ?String = None
    )
}
```

功能：证书实体可辨识名称（Distinguished Name）是数字证书中的一个重要组成部分，作用是确保证书的持有者身份的真实性和可信度，同时也是数字证书验证的重要依据之一。

[X509Name](x509_package_classes.md#class-x509name) 通常包含证书实体的国家或地区名称（Country Name）、州或省名称（State or Province Name）、城市名称（Locality Name）、组织名称（Organization Name）、组织单位名称（Organizational Unit Name）、通用名称（Common Name）。有时也会包含 email 地址。

父类型：

- ToString

### prop commonName

```cangjie
public prop commonName: ?String
```

功能：返回证书实体的通用名称。

类型：?String

### prop countryName

```cangjie
public prop countryName: ?String
```

功能：返回证书实体的国家或地区名称。

类型：?String

### prop email

```cangjie
public prop email: ?String
```

功能：返回证书实体的 email 地址。

类型：?String

### prop localityName

```cangjie
public prop localityName: ?String
```

功能：返回证书实体的城市名称。

类型：?String

### prop organizationName

```cangjie
public prop organizationName: ?String
```

功能：返回证书实体的组织名称。

类型：?String

### prop organizationalUnitName

```cangjie
public prop organizationalUnitName: ?String
```

功能：返回证书实体的组织单位名称。

类型：?String

### prop provinceName

```cangjie
public prop provinceName: ?String
```

功能：返回证书实体的州或省名称。

类型：?String

### init(?String, ?String, ?String, ?String, ?String, ?String, ?String)

```cangjie
    public init(
        countryName!: ?String = None,
        provinceName!: ?String = None,
        localityName!: ?String = None,
        organizationName!: ?String = None,
        organizationalUnitName!: ?String = None,
        commonName!: ?String = None,
        email!: ?String = None
    )
```

功能：构造 [X509Name](x509_package_classes.md#class-x509name) 对象。

参数：

- countryName!: ?String - 国家或地区名称，默认值为 None。
- provinceName!: ?String - 州或省名称，默认值为 None。
- localityName!: ?String - 城市名称，默认值为 None。
- organizationName!: ?String - 组织名称，默认值为 None。
- organizationalUnitName!: ?String - 组织单位名称，默认值为 None。
- commonName!: ?String - 通用名称，默认值为 None。
- email!: ?String - email 地址，默认值为 None。

异常：

- [X509Exception](./x509_package_exceptions.md#class-x509exception) - 设置证书实体可辨识名称时失败，比如内存分配异常等内部错误，则抛出异常。

### func toString()

```cangjie
public override func toString(): String
```

功能：生成证书实体名称字符串。

返回值：

- String - 证书实体名称字符串，包含实体名称中存在的字段信息。