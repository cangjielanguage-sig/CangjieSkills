### MOVED_TEMP

```cangjie
MOVED_TEMP
```

**功能：** 临时移动。

**起始版本：** 12

### MULT_CHOICE

```cangjie
MULT_CHOICE
```

**功能：** 多种选择。

**起始版本：** 12

### NETWORK_AUTHENTICATION_REQUIRED

```cangjie
NETWORK_AUTHENTICATION_REQUIRED
```

**功能：** 指示客户端需要进行身份验证才能获得网络访问权限。

**起始版本：** 12

### NOT_ACCEPTABLE

```cangjie
NOT_ACCEPTABLE
```

**功能：** 服务器无法根据客户端请求的内容特性完成请求。

**起始版本：** 12

### NOT_AUTHORITATIVE

```cangjie
NOT_AUTHORITATIVE
```

**功能：** 非授权信息。请求成功。

**起始版本：** 12

### NOT_EXTENDED

```cangjie
NOT_EXTENDED
```

**功能：** 服务器需要对请求进行进一步扩展才能完成请求。

**起始版本：** 12

### NOT_FOUND

```cangjie
NOT_FOUND
```

**功能：** 服务器无法根据客户端的请求找到资源（网页）。

**起始版本：** 12

### NOT_IMPLEMENTED

```cangjie
NOT_IMPLEMENTED
```

**功能：** 服务器不支持请求的功能，无法完成请求。

**起始版本：** 12

### NOT_MODIFIED

```cangjie
NOT_MODIFIED
```

**功能：** 未修改。

**起始版本：** 12

### NO_CONTENT

```cangjie
NO_CONTENT
```

**功能：** 无内容。服务器成功处理，但未返回内容。

**起始版本：** 12

### OK

```cangjie
OK
```

**功能：** 请求成功。一般用于GET与POST请求。

**起始版本：** 12

### PARTIAL

```cangjie
PARTIAL
```

**功能：** 部分内容。服务器成功处理了部分GET请求。

**起始版本：** 12

### PAYMENT_REQUIRED

```cangjie
PAYMENT_REQUIRED
```

**功能：** 保留，将来使用。

**起始版本：** 12

### PRECONDITION_REQUIRED

```cangjie
PRECONDITION_REQUIRED
```

**功能：** 源服务器要求请求是有条件的。此响应旨在防止'丢失更新'问题，即当第三方修改服务器上的状态时，客户端GET获取资源的状态，对其进行修改并将其PUT放回服务器，从而导致冲突。

**起始版本：** 12

### PRECON_FAILED

```cangjie
PRECON_FAILED
```

**功能：** 客户端请求信息的先决条件错误。

**起始版本：** 12

### PROXY_AUTH

```cangjie
PROXY_AUTH
```

**功能：** 请求要求代理的身份认证。

**起始版本：** 12

### REQUESTED_RANGE_NOT_SATISFIABLE

```cangjie
REQUESTED_RANGE_NOT_SATISFIABLE
```

**功能：** 无法满足请求中Range标头字段指定的范围。该范围可能超出了目标URI数据的大小。

**起始版本：** 12

### REQUEST_HEADER_FIELDS_TOO_LARGE

```cangjie
REQUEST_HEADER_FIELDS_TOO_LARGE
```

**功能：** 服务器不愿意处理请求，因为其头字段太大。在减小请求头字段的大小后，可以重新提交请求。

**起始版本：** 12

### REQ_TOO_LONG

```cangjie
REQ_TOO_LONG
```

**功能：** 请求的URI过长（URI通常为网址），服务器无法处理。

**起始版本：** 12

### RESET

```cangjie
RESET
```

**功能：** 重置内容。

**起始版本：** 12

### SEE_OTHER

```cangjie
SEE_OTHER
```

**功能：** 查看其它地址。

**起始版本：** 12

### TEAPOT

```cangjie
TEAPOT
```

**功能：** 服务端拒绝用茶壶煮咖啡。

**起始版本：** 12

### TOO_EARLY

```cangjie
TOO_EARLY
```

**功能：** 表示服务器不愿意冒险处理可能被重播的请求。

**起始版本：** 12

### TOO_MANY_REQUESTS

```cangjie
TOO_MANY_REQUESTS
```

**功能：** 表示用户在给定的时间内发送了太多请求，应限制请求速率。

**起始版本：** 12

### UNAUTHORIZED

```cangjie
UNAUTHORIZED
```

**功能：** 请求要求用户的身份认证。

**起始版本：** 12

### UNAVAILABLE

```cangjie
UNAVAILABLE
```

**功能：** 由于超载或系统维护，服务器暂时的无法处理客户端的请求。

**起始版本：** 12

### UNAVAILABLE_FOR_LEGAL_REASONS

```cangjie
UNAVAILABLE_FOR_LEGAL_REASONS
```

**功能：** 用户代理请求了无法合法提供的资源，例如政府审查的网页。

**起始版本：** 12

### UNPROCESSABLE_ENTITY

```cangjie
UNPROCESSABLE_ENTITY
```

**功能：** 请求格式正确，但由于语义错误而无法遵循。

**起始版本：** 12

### UNSUPPORTED_TYPE

```cangjie
UNSUPPORTED_TYPE
```

**功能：** 服务器无法处理请求的格式。

**起始版本：** 12