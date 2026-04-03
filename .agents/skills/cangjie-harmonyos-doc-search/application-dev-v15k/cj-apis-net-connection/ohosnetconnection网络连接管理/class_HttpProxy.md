## class HttpProxy

```cangjie
public class HttpProxy {
    public HttpProxy(
        public let host!: ?String = None,
        public let port!: ?UInt16 = None,
        public let exclusionList!: ?Array<String> = None
    )
}
```

**功能：** 网络代理配置信息。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

### let exclusionList

```cangjie
public let exclusionList: ?Array<String> = None
```

**功能：** 不使用代理的主机名列表，主机名支持域名、IP地址以及通配符形式，详细匹配规则如下：

1. 域名匹配规则：

    （1）完全匹配：代理服务器主机名只要与列表中的任意一个主机名完全相同，就可以匹配。

    （2）包含匹配：代理服务器主机名只要包含列表中的任意一个主机名，就可以匹配。

    例如，如果在主机名列表中设置了“ample.com”，则“ample.com”、“www.ample.com”、“ample.com:80”都会被匹配，而“www.example.com”、“ample.com.org”则不会被匹配。

2. IP地址匹配规则：代理服务器主机名只要与列表中的任意一个IP地址完全相同，就可以匹配。

3. 域名跟IP地址可以同时添加到列表中进行匹配。

4. 单个“*”是唯一有效的通配符，当列表中只有通配符时，将与所有代理服务器主机名匹配，表示禁用代理。通配符只能单独添加，不可以与其他域名、IP地址一起添加到列表中，否则通配符将不生效。

5. 匹配规则不区分主机名大小写。

6. 匹配主机名时，不考虑http和https等协议前缀。

**类型：** ?Array\<String>

**读写能力：** 只读

**起始版本：** 12

### let host

```cangjie
public let host: ?String = None
```

**功能：** 代理服务器主机名。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 12

### let port

```cangjie
public let port: ?UInt16 = None
```

**功能：** 主机端口。

**类型：** ?UInt16

**读写能力：** 只读

**起始版本：** 12

### HttpProxy(?String, ?UInt16, ?Array\<String>)

```cangjie
public HttpProxy(
    public let host!: ?String = None,
    public let port!: ?UInt16 = None,
    public let exclusionList!: ?Array<String> = None
)
```

**功能：** 构造HttpProxy实例。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|host|?String|否|None| **命名参数。** 代理服务器主机名。|
|port|?UInt16|否|None| **命名参数。** 主机端口。|
|exclusionList|?Array\<String>|否|None| **命名参数。** 不使用代理的主机名列表，主机名支持域名、IP地址以及通配符形式，详细匹配规则如下：<br>1、域名匹配规则：<br>（1）完全匹配：代理服务器主机名只要与列表中的任意一个主机名完全相同，就可以匹配。<br>（2）包含匹配：代理服务器主机名只要包含列表中的任意一个主机名，就可以匹配。<br>例如，如果在主机名列表中设置了 “ample.com”，则 “ample.com”、“www.ample.com”、“ample.com:80”都会被匹配，而 “www.example.com”、“ample.com.org”则不会被匹配。<br>2、IP地址匹配规则：代理服务器主机名只要与列表中的任意一个IP地址完全相同，就可以匹配。<br>3、域名跟IP地址可以同时添加到列表中进行匹配。<br>4、单个“*”是唯一有效的通配符，当列表中只有通配符时，将与所有代理服务器主机名匹配，表示禁用代理。通配符只能单独添加，不可以与其他域名、IP地址一起添加到列表中，否则通配符将不生效。<br>5、匹配规则不区分主机名大小写。<br>6、匹配主机名时，不考虑http和https等协议前缀。|