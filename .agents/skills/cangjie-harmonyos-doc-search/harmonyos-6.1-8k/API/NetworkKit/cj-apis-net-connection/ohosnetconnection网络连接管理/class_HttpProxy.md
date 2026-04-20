## class HttpProxy

```cangjie
public class HttpProxy {
    public var host: String
    public var port: UInt32
    public var exclusionList: Array<String>
    public var username: String
    public var password: String
    public init(host: String,  port: UInt32, exclusionList: Array<String>,
        username!: String = "", password!: String = "")
}
```

**功能：** 网络代理配置信息。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var exclusionList

```cangjie
public var exclusionList: Array<String>
```

**功能：** 不使用代理的主机名列表，主机名支持域名、IP地址以及通配符形式，详细匹配规则如下：

1、域名匹配规则：

（1）完全匹配：代理服务器主机名只要与列表中的任意一个主机名完全相同，就可以匹配。

（2）包含匹配：代理服务器主机名只要包含列表中的任意一个主机名，就可以匹配。

例如，如果在主机名列表中设置了 “ample.com”，则  “ample.com”、“www.ample.com”、“ample.com:80”都会被匹配，而 “www.example.com”、“ample.com.org”则不会被匹配。

2、IP地址匹配规则：代理服务器主机名只要与列表中的任意一个IP地址完全相同，就可以匹配。

3、域名跟IP地址可以同时添加到列表中进行匹配。

4、单个“\*”是唯一有效的通配符，当列表中只有通配符时，将与所有代理服务器主机名匹配，表示禁用代理。通配符只能单独添加，不可以与其他域名、IP地址一起添加到列表中，否则通配符将不生效。

5、匹配规则不区分主机名大小写。

6、匹配主机名时，不考虑http和https等协议前缀。

**类型：** Array\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var host

```cangjie
public var host: String
```

**功能：** 代理服务器主机名。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var password

```cangjie
public var password: String
```

**功能：** 使用代理的用户密码。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var port

```cangjie
public var port: UInt32
```

**功能：** 主机端口。取值范围[0,65535]。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var username

```cangjie
public var username: String
```

**功能：** 使用代理的用户名。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### init(String, UInt32, Array\<String>, String, String)

```cangjie
public init(host: String,  port: UInt32, exclusionList: Array<String>,
    username!: String = "", password!: String = "")
```

**功能：** 构造HttpProxy实例。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|host|String|是|-|代理服务器主机名。|
|port|UInt32|是|-|主机端口。取值范围[0,65535]。|
|exclusionList|Array\<String>|是|-|不使用代理的主机名列表。|
|username|String|否|""|**命名参数。** 使用代理的用户名。|
|password|String|否|""|**命名参数。** 使用代理的用户密码。|