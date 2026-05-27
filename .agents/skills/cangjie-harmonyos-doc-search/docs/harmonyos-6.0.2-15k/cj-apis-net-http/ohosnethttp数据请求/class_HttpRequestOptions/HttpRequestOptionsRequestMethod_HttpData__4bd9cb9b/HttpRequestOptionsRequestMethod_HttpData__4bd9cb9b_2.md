|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|method|[RequestMethod](#enum-requestmethod)|否|RequestMethod.GET| **命名参数。** 请求方式，默认为GET。|
|extraData|?[HttpData](#enum-httpdata)|否|None| **命名参数。**  发送请求的额外数据，默认无此字段。<br>当HTTP请求为POST、PUT等方法时，此字段为HTTP请求的content，以UTF-8编码形式作为请求体。<br>当'content-Type'为'application/x-www-form-urlencoded'时，请求提交的信息主体数据应在key和value进行URL转码后按照键值对"key1=value1&key2=value2&key3=value3"的方式进行编码，该字段对应的类型通常为String；<br>当'content-Type'为'text/xml'时，该字段对应的类型通常为String；<br>当'content-Type'为'application/json'时，该字段对应的类型通常为Object；<br>当'content-Type'为'application/octet-stream'时，该字段对应的类型通常为ArrayBuffer；<br>当'content-Type'为'multipart/form-data'且需上传的字段为文件时，该字段对应的类型通常为ArrayBuffer。<br> 当HTTP请求为GET、OPTIONS、DELETE、TRACE、CONNECT等方法时，此字段为HTTP请求参数的补充。开发者需传入Encode编码后的string类型参数，Object类型的参数无需预编码，参数内容会拼接到URL中进行发送；<br>ArrayBuffer类型的参数不会做拼接处理。<br>以上信息仅供参考，并可能根据具体情况有所不同。 |
|expectDataType|?[HttpDataType](#enum-httpdatatype)|否|None| **命名参数。** 指定返回数据的类型，默认无此字段。如果设置了此参数，系统将优先返回指定的类型。|
|usingCache|Bool|否|true| **命名参数。** 是否使用缓存，默认为true，请求时优先读取缓存。 缓存跟随当前进程生效。新缓存会替换旧缓存。|
|priority|UInt32|否|1| **命名参数。** 优先级，范围[1,1000]，默认是1。若传参超出范围则使用默认值1。|
|header|?HashMap\<String,String>|否|None| **命名参数。** HTTP请求头字段。默认{'content-Type': 'application/json'}。|
|readTimeout|UInt32|否|60000| **命名参数。** 读取超时时间。单位为毫秒（ms），默认为60000ms。<br>设置为0表示不会出现超时情况。|
|connectTimeout|UInt32|否|60000| **命名参数。** 连接超时时间。单位为毫秒（ms），默认为60000ms。|
|usingProtocol|?[HttpProtocol](#enum-httpprotocol)|否|None| **命名参数。** 使用协议。默认值由系统自动指定。|
|usingProxy|[UsingProxy](#enum-usingproxy)|否|USE_DEFAULT| **命名参数。** 是否使用HTTP代理，默认为USE_DEFAULT，使用默认代理。<br> 当usingProxy为NOT_USE时，不使用网络代理。<br> 当usingProxy为USE_SPECIFIED类型时，使用指定网络代理。|
|caPath|?String|否|None| **命名参数。** 如果设置了此参数，系统将使用用户指定路径的CA证书，(开发者需保证该路径下CA证书的可访问性)，否则将使用系统预设CA证书，系统预设CA证书位置：/etc/ssl/certs/cacert.pem。证书路径为沙箱映射路径（开发者可通过Global.getContext().filesDir获取应用沙箱路径）。目前仅支持后缀名为.pem的文本格式证书。|
|resumeFrom|?Int64|否|None| **命名参数。** 用于设置上传或下载起始位置。HTTP标准（RFC 7233第3.1节）允许服务器忽略范围请求。<br>使用HTTP PUT时设置此参数，可能出现未知问题。<br>取值范围是:1~4294967296(4GB)，超出范围则不生效。无默认值。|
|resumeTo|?Int64|否|None| **命名参数。** 用于设置上传或下载结束位置。HTTP标准（RFC 7233第3.1节）允许服务器忽略范围请求。<br>使用HTTP PUT时设置此参数，可能出现未知问题。<br>取值范围是:1~4294967296(4GB)，超出范围则不生效。无默认值。|
|clientCert|?[ClientCert](#class-clientcert)|否|None| **命名参数。** 支持传输客户端证书。|
|dnsOverHttps|?String|否|None| **命名参数。** 设置使用HTTPS协议的服务器进行DNS解析。<br>参数必须以以下格式进行URL编码："https:// host:port/path"。|
|dnsServers|?Array\<String>|否|None| **命名参数。** 设置指定的DNS服务器进行DNS解析。<br>可以设置多个DNS解析服务器，最多3个服务器。如果有3个以上，只取前3个。<br>服务器必须是IPv4或者IPv6地址。|
|maxLimit|UInt32|否|5 * 1024 * 1024| **命名参数。** 响应消息的最大字节限制，默认值为5MB，以字节为单位。最大值为10MB，以字节为单位。|
|multiFormDataList|?Array\<[MultiFormData](#class-multiformdata)>|否|None| **命名参数。** 当'content-Type'为'multipart/form-data'时，则上传该字段定义的数据字段表单列表。|