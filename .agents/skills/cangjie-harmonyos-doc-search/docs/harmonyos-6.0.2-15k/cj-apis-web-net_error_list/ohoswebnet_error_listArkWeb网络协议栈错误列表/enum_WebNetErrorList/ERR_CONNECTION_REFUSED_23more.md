### ERR_CONNECTION_REFUSED

```cangjie
ERR_CONNECTION_REFUSED
```

**功能：** 连接被拒绝。

**起始版本：** 19

### ERR_CONNECTION_RESET

```cangjie
ERR_CONNECTION_RESET
```

**功能：** 连接被重置（对应于TCP RST）。

**起始版本：** 19

### ERR_CONNECTION_TIMED_OUT

```cangjie
ERR_CONNECTION_TIMED_OUT
```

**功能：** 连接超时。

**起始版本：** 19

### ERR_CONTENT_DECODING_FAILED

```cangjie
ERR_CONTENT_DECODING_FAILED
```

**功能：** 响应正文的内容解码失败。

**起始版本：** 19

### ERR_CONTENT_DECODING_INIT_FAILED

```cangjie
ERR_CONTENT_DECODING_INIT_FAILED
```

**功能：** 内容解码初始化失败。

**起始版本：** 19

### ERR_CONTENT_LENGTH_MISMATCH

```cangjie
ERR_CONTENT_LENGTH_MISMATCH
```

**功能：** 当连接关闭时，HTTP 响应主体传输的字节数少于 Content-Length 头中公布的字节数。

**起始版本：** 19

### ERR_CONTEXT_SHUT_DOWN

```cangjie
ERR_CONTEXT_SHUT_DOWN
```

**功能：** 因为上下文已关闭导致请求失败。

**起始版本：** 19

### ERR_CT_CONSISTENCY_PROOF_PARSING_FAILED

```cangjie
ERR_CT_CONSISTENCY_PROOF_PARSING_FAILED
```

**功能：** Certificate Transparency：一致性验证解析失败。

**起始版本：** 19

### ERR_CT_STH_INCOMPLETE

```cangjie
ERR_CT_STH_INCOMPLETE
```

**功能：** Certificate Transparency：解析signed tree head成功，但是缺少了一些信息。

**起始版本：** 19

### ERR_CT_STH_PARSING_FAILED

```cangjie
ERR_CT_STH_PARSING_FAILED
```

**功能：** Certificate Transparency：解析signed tree head失败。

**起始版本：** 19

### ERR_DISALLOWED_URL_SCHEME

```cangjie
ERR_DISALLOWED_URL_SCHEME
```

**功能：** 不允许使用的URL scheme。

**起始版本：** 19

### ERR_DNS_CACHE_MISS

```cangjie
ERR_DNS_CACHE_MISS
```

**功能：** 对于只查询本地源的查找，在缓存或其他本地源中未找到该条目。

**起始版本：** 19

### ERR_DNS_MALFORMED_RESPONSE

```cangjie
ERR_DNS_MALFORMED_RESPONSE
```

**功能：** DNS解析程序收到格式错误的响应。

**起始版本：** 19

### ERR_DNS_NAME_HTTPS_ONLY

```cangjie
ERR_DNS_NAME_HTTPS_ONLY
```

**功能：** DNS已识别请求因不安全的连接（http/ws）而被禁止。应用程序应该像处理HTTP重定向一样处理这个错误，将连接重定向到安全的https或wss。

**起始版本：** 19

### ERR_DNS_NO_MATCHING_SUPPORTED_ALPN

```cangjie
ERR_DNS_NO_MATCHING_SUPPORTED_ALPN
```

**功能：** HTTPS记录的主机名解析预期未能使用受支持协议的ALPN值进行解析。

**起始版本：** 19

### ERR_DNS_REQUEST_CANCELED

```cangjie
ERR_DNS_REQUEST_CANCELED
```

**功能：** 与此任务相关的所有 DNS 请求已被取消。

**起始版本：** 19

### ERR_DNS_SEARCH_EMPTY

```cangjie
ERR_DNS_SEARCH_EMPTY
```

**功能：** 后缀搜索列表规则阻止了给定主机名的解析。

**起始版本：** 19

### ERR_DNS_SECURE_RESOLVER_HOSTNAME_RESOLUTION_FAILED

```cangjie
ERR_DNS_SECURE_RESOLVER_HOSTNAME_RESOLUTION_FAILED
```

**功能：** 未能解析DNS-over-HTTPS服务器的主机名。

**起始版本：** 19

### ERR_DNS_SERVER_FAILED

```cangjie
ERR_DNS_SERVER_FAILED
```

**功能：** DNS服务器失败。对于以下所有错误情况，都会返回此错误。1-格式错误-名称服务器无法解释查询。2-服务器故障-名称服务器由于自身问题无法处理这个查询。3-未实现-名称服务器不支持请求的查询类型。4-拒绝-名称服务器出于策略原因拒绝执行指定的操作。

**起始版本：** 19

### ERR_DNS_SERVER_REQUIRES_TCP

```cangjie
ERR_DNS_SERVER_REQUIRES_TCP
```

**功能：** DNS服务器需要TCP。

**起始版本：** 19

### ERR_DNS_SORT_ERROR

```cangjie
ERR_DNS_SORT_ERROR
```

**功能：** 未能根据RFC3484对地址进行排序。

**起始版本：** 19

### ERR_DNS_TIMED_OUT

```cangjie
ERR_DNS_TIMED_OUT
```

**功能：** DNS事务超时。

**起始版本：** 19

### ERR_EARLY_DATA_REJECTED

```cangjie
ERR_EARLY_DATA_REJECTED
```

**功能：** TLS 1.3 early data 被服务器拒绝。

**起始版本：** 19