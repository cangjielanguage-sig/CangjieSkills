## class SqlOption

```cangjie
public class SqlOption {
    public static const URL: String = "url"
    public static const Host: String = "host"
    public static const Username: String = "username"
    public static const Password: String = "password"
    public static const Driver: String = "driver"
    public static const Database: String = "database"
    public static const Encoding: String = "encoding"
    public static const ConnectionTimeout: String = "connection_timeout"
    public static const UpdateTimeout: String = "update_timeout"
    public static const QueryTimeout: String = "query_timeout"
    public static const FetchRows: String = "fetch_rows"
    public static const SSLMode: String = "ssl.mode"
    public static const SSLModePreferred: String = "ssl.mode.preferred"
    public static const SSLModeDisabled: String = "ssl.mode.disabled"
    public static const SSLModeRequired: String = "ssl.mode.required"
    public static const SSLModeVerifyCA: String = "ssl.mode.verify_ca"
    public static const SSLModeVerifyFull: String = "ssl.mode.verify_full"
    public static const SSLCA: String = "ssl.ca"
    public static const SSLCert: String = "ssl.cert"
    public static const SSLKey: String = "ssl.key"
    public static const SSLKeyPassword: String = "ssl.key.password"
    public static const SSLSni: String = "ssl.sni"
    public static const Tls12Ciphersuites: String = "tls1.2.ciphersuites"
    public static const Tls13Ciphersuites: String = "tls1.3.ciphersuites"
    public static const TlsVersion: String = "tls.version"
}
```

功能：预定义的 sql 选项名称和值。如果需要扩展，请不要与这些名称和值冲突。

### static const ConnectionTimeout

```cangjie
public static const ConnectionTimeout: String = "connection_timeout"
```

功能：获取 connect 操作的超时时间，单位 ms。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const Database

```cangjie
public static const Database: String = "database"
```

功能：获取数据库名称。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const Driver

```cangjie
public static const Driver: String = "driver"
```

功能：获取数据库驱动名称，比如 postgres，opengauss。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const Encoding

```cangjie
public static const Encoding: String = "encoding"
```

功能：获取数据库字符集编码类型。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const FetchRows

```cangjie
public static const FetchRows: String = "fetch_rows"
```

功能：获取每次获取额外数据时从数据库中提取的行数。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const Host

```cangjie
public static const Host: String = "host"
```

功能：获取数据库服务器主机名或者 IP 地址。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const Password

```cangjie
public static const Password: String = "password"
```

功能：获取连接数据库的密码。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const QueryTimeout

```cangjie
public static const QueryTimeout: String = "query_timeout"
```

功能：获取 query 操作的超时时间，单位 ms。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const SSLCA

```cangjie
public static const SSLCA: String = "ssl.ca"
```

功能：证书颁发机构（ CA ）证书文件的路径名。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)