|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|method|[RequestMethod](#enum-requestmethod)|否|RequestMethod.Get|**命名参数。** 请求方式，默认为RequestMethod.Get。|
|extraData|[HttpData](#enum-httpdata)|否|HttpData.StringData("")|**命名参数。** 发送请求的额外数据，默认无此字段。|
|expectDataType|?[HttpDataType](#enum-httpdatatype)|否|None|**命名参数。** 指定返回数据的类型，默认无此字段。如果设置了此参数，系统将优先返回指定的类型。|
|usingCache|Bool|否|true|**命名参数。** 是否使用缓存，true表示请求时优先读取缓存，false表示不使用缓存；默认为true，请求时优先读取缓存。缓存跟随当前进程生效，新缓存会替换旧缓存。|
|priority|UInt32|否|1|**命名参数。** HTTP/HTTPS请求并发优先级，值越大优先级越高，范围[1,1000]，默认为1。|
|header|HashMap\<String,String>|否|HashMap<String,String>()|**命名参数。** HTTP请求头字段。当请求方式为"POST" "PUT" "DELETE" 或者""时，默认{'content-Type': 'application/json'}， 否则默认{'content-Type': 'application/x-www-form-urlencoded'}。<br />如果head中包含number类型的字段，最大支持int64的整数。|
|readTimeout|UInt32|否|60000|**命名参数。** 读取超时时间。单位为毫秒（ms），默认为60000ms。传入值需为uint32_t范围内的整数。<br />设置为0表示不会出现超时情况。|
|connectTimeout|UInt32|否|60000|**命名参数。** 连接超时时间。单位为毫秒（ms），默认为60000ms。传入值需为uint32_t范围内的整数。|
|usingProtocol|?[HttpProtocol](#enum-httpprotocol)|否|None|**命名参数。** 使用协议，默认值由系统自动指定为None。|
|usingProxy|[UsingProxy](#enum-usingproxy)|否|UsingProxy.UseDefault|**命名参数。** HTTP代理配置，该项不配置时表示不使用代理。<br />- 当usingProxy为布尔类型true时，使用默认网络代理，为false时，不使用代理。<br />- 当usingProxy为HttpProxy类型时，使用指定网络代理。当前HttpProxy不支持指定username和password字段。|
|caPath|String|否|""|**命名参数。** 如果设置了此参数，系统将使用用户指定路径的CA证书（开发者需保证该路径下CA证书的可访问性），否则将使用系统预设CA证书。<br />系统预设CA证书位置：/etc/ssl/certs/cacert.pem。证书路径为沙箱映射路径（开发者可通过UIAbilityContext提供的能力获取应用沙箱路径）。目前仅支持后缀名为.pem的文本格式证书。|
|resumeFrom|Int64|否|0|**命名参数。** 用于设置下载起始位置，该参数只能用于GET方法，不能用于其他。HTTP标准（RFC 7233第3.1节）允许服务器忽略范围请求。<br />- 使用HTTP PUT时，不能使用该选项，因为该选项可能与其他选项冲突。<br />- 取值范围是：[1，4294967296（4GB）]，超出范围则不生效。|
|resumeTo|Int64|否|0|**命名参数。** 用于设置下载结束位置，该参数只能用于GET方法，不能用于其他。HTTP标准（RFC 7233第3.1节）允许服务器忽略范围请求。<br />- 使用HTTP PUT时，不能使用该选项，因为该选项可能与其他选项冲突。<br />- 取值范围是：[1，4294967296（4GB）]，超出范围则不生效。|
|clientCert|[ClientCert](#class-clientcert)|否|ClientCert("", "")|**命名参数。** 支持传输客户端证书。|
|dnsOverHttps|String|否|""|**命名参数。** 设置使用HTTPS协议的服务器进行DNS解析。<br />- 参数必须根据以下格式进行URL编码："https:// host:port/path"。|
|dnsServers|Array\<String>|否|Array\<String>()|**命名参数。** 设置指定的DNS服务器进行DNS解析。<br />- 最多可以设置3个DNS解析服务器。如果有3个以上，只取前3个。<br />- 服务器必须是IPV4或者IPV6地址。|
|maxLimit|UInt32|否|5 * 1024 * 1024|**命名参数。** 响应消息的最大字节限制。<br />默认值为5\*1024\*1024，以字节为单位。最大值为100\*1024\*1024，以字节为单位。|
|multiFormDataList|Array\<[MultiFormData](#class-multiformdata)>|否|Array\<MultiFormData>()|**命名参数。** 当'content-Type'为'multipart/form-data'时，则上传该字段定义的数据字段表单列表。|