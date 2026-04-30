### WifiEapConfig(EapMethod, Phase2Method, String, String, String, String, String, String, Array\<UInt8>, String, String, String, String, String, Int32)

```cangjie
public WifiEapConfig(
    public let eapMethod: EapMethod,
    public let phase2Method: Phase2Method,
    public let identity: String,
    public let anonymousIdentity: String,
    public let password: String,
    public let caCertAlias: String,
    public let caPath: String,
    public let clientCertAlias: String,
    public let certEntry: Array<UInt8>,
    public let certPassword: String,
    public let altSubjectMatch: String,
    public let domainSuffixMatch: String,
    public let realm: String,
    public let plmn: String,
    public let eapSubId: Int32
)
```

**功能：** 构造WifiEapConfig实例。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|eapMethod|[EapMethod](#enum-eapmethod)|是|EAP认证方式。|
|phase2Method|[Phase2Method](#enum-phase2method)|是|第二阶段认证方式。只有eapMethod为EAP_PEAP或EAP_TTLS时需要填写。|
|identity|String|是|身份信息。当eapMethod为EAP_PEAP、EAP_TLS或EAP_PWD时，该字段不能为空串。|
|anonymousIdentity|String|是|匿名身份。暂未使用。|
|password|String|是|密码。当eapMethod为EAP_PEAP或EAP_PWD时，该字段不能为空串。|
|caCertAlias|String|是|CA 证书别名。|
|caPath|String|是|CA 证书路径。|
|clientCertAlias|String|是|客户端证书别名。|
|certEntry|Array\<UInt8>|是|CA证书内容。当eapMethod为EAP_TLS时，如果该字段为空，则clientCertAlias不能为空。|
|certPassword|String|是|CA证书密码。|
|altSubjectMatch|String|是|替代主题匹配。|
|domainSuffixMatch|String|是|域后缀匹配。|
|realm|String|是|通行证凭证的领域。|
|plmn|String|是|公共陆地移动网的直通凭证提供商。|
|eapSubId|Int32|是|SIM卡的子ID。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前类的字符串表示。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前类的字符串表示。|