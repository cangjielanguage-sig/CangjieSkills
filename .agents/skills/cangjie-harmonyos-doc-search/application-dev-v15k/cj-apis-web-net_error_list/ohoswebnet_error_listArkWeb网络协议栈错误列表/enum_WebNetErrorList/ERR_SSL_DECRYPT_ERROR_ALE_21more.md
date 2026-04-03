### ERR_SSL_DECRYPT_ERROR_ALERT

```cangjie
ERR_SSL_DECRYPT_ERROR_ALERT
```

**功能：** SSL对等端向本端发送了致命的decrypt_error警报。当对等方无法正确验证签名（在CertificateVerify或ServerKeyExchange中）或验证Finished消息时，通常会发生这种情况。

**起始版本：** 19

### ERR_SSL_HANDSHAKE_NOT_COMPLETED

```cangjie
ERR_SSL_HANDSHAKE_NOT_COMPLETED
```

**功能：** 由于SSL握手尚未完成，操作失败。

**起始版本：** 19

### ERR_SSL_KEY_USAGE_INCOMPATIBLE

```cangjie
ERR_SSL_KEY_USAGE_INCOMPATIBLE
```

**功能：** 服务器的证书具有与协商的TLS密钥交换方法不兼容的keyUsage扩展。

**起始版本：** 19

### ERR_SSL_NO_RENEGOTIATION

```cangjie
ERR_SSL_NO_RENEGOTIATION
```

**功能：** 对方发送了SSL no_regregation警报消息。

**起始版本：** 19

### ERR_SSL_OBSOLETE_CIPHER

```cangjie
ERR_SSL_OBSOLETE_CIPHER
```

**功能：** SSL服务器需要一个不受支持的密码套件，该套件已被删除。此错误将在密码套件删除后立即在一个或两个版本的回退中临时发出信号，之后回退将被删除。

**起始版本：** 19

### ERR_SSL_OBSOLETE_VERSION_OR_CIPHER

```cangjie
ERR_SSL_OBSOLETE_VERSION_OR_CIPHER
```

**功能：** 连接使用过时版本的 SSL/TLS 或密码。

**起始版本：** 19

### ERR_SSL_PINNED_KEY_NOT_IN_CERT_CHAIN

```cangjie
ERR_SSL_PINNED_KEY_NOT_IN_CERT_CHAIN
```

**功能：** 收到的证书与内置域名指定的公钥不匹配。

**起始版本：** 19

### ERR_SSL_PROTOCOL_ERROR

```cangjie
ERR_SSL_PROTOCOL_ERROR
```

**功能：** SSL 协议错误。

**起始版本：** 19

### ERR_SSL_RENEGOTIATION_REQUESTED

```cangjie
ERR_SSL_RENEGOTIATION_REQUESTED
```

**功能：** 服务器请求重新协商（rehandshake）。

**起始版本：** 19

### ERR_SSL_SERVER_CERT_BAD_FORMAT

```cangjie
ERR_SSL_SERVER_CERT_BAD_FORMAT
```

**功能：** SSL服务器提供了一个无法解码的证书。

**起始版本：** 19

### ERR_SSL_SERVER_CERT_CHANGED

```cangjie
ERR_SSL_SERVER_CERT_CHANGED
```

**功能：** SSL服务器证书在重新协商中更改。

**起始版本：** 19

### ERR_SSL_UNRECOGNIZED_NAME_ALERT

```cangjie
ERR_SSL_UNRECOGNIZED_NAME_ALERT
```

**功能：** SSL服务器向本端发送了致命的未识别名称警报。

**起始版本：** 19

### ERR_SSL_VERSION_OR_CIPHER_MISMATCH

```cangjie
ERR_SSL_VERSION_OR_CIPHER_MISMATCH
```

**功能：** 客户端和服务器不支持通用的SSL协议版本或密码套件。

**起始版本：** 19

### ERR_SYN_REPLY_NOT_RECEIVED

```cangjie
ERR_SYN_REPLY_NOT_RECEIVED
```

**功能：** 在流上未接收到SYN_REPLY的情况下接收到的FLIP数据。

**起始版本：** 19

### ERR_TEMPORARILY_THROTTLED

```cangjie
ERR_TEMPORARILY_THROTTLED
```

**功能：** 因节流而取消了此请求以避免DDOS。

**起始版本：** 19

### ERR_TIMED_OUT

```cangjie
ERR_TIMED_OUT
```

**功能：** 操作超时。

**起始版本：** 19

### ERR_TLS13_DOWNGRADE_DETECTED

```cangjie
ERR_TLS13_DOWNGRADE_DETECTED
```

**功能：** TLS 1.3已启用，但已协商更低的版本，服务器返回一个值，表示它支持TLS 1.3。这是TLS 1.3中安全检查的一部分，但也可能表明用户使用了一个有问题的TLS-terminating代理。

**起始版本：** 19

### ERR_TOO_MANY_ACCEPT_CH_RESTARTS

```cangjie
ERR_TOO_MANY_ACCEPT_CH_RESTARTS
```

**功能：** ACCEPT_CH 重启已被触发太多次。

**起始版本：** 19

### ERR_TOO_MANY_REDIRECTS

```cangjie
ERR_TOO_MANY_REDIRECTS
```

**功能：** 重定向过多。

**起始版本：** 19

### ERR_TOO_MANY_RETRIES

```cangjie
ERR_TOO_MANY_RETRIES
```

**功能：** 由于身份验证或证书无效，HTTP事务重试次数过多。

**起始版本：** 19

### ERR_TRUST_TOKEN_OPERATION_FAILED

```cangjie
ERR_TRUST_TOKEN_OPERATION_FAILED
```

**功能：** 执行Trust Tokens协议操作的请求失败（原因包括：预置条件失败、内部错误、不良响应）。

**起始版本：** 19