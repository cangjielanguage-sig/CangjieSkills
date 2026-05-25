## enum ResponseCode

```cangjie
public enum ResponseCode {
    | OK
    | CREATED
    | ACCEPTED
    | NOT_AUTHORITATIVE
    | NO_CONTENT
    | RESET
    | PARTIAL
    | MULT_CHOICE
    | MOVED_PERM
    | MOVED_TEMP
    | SEE_OTHER
    | NOT_MODIFIED
    | USE_PROXY
    | BAD_REQUEST
    | UNAUTHORIZED
    | PAYMENT_REQUIRED
    | FORBIDDEN
    | NOT_FOUND
    | BAD_METHOD
    | NOT_ACCEPTABLE
    | PROXY_AUTH
    | CLIENT_TIMEOUT
    | CONFLICT
    | GONE
    | LENGTH_REQUIRED
    | PRECON_FAILED
    | ENTITY_TOO_LARGE
    | REQ_TOO_LONG
    | UNSUPPORTED_TYPE
    | REQUESTED_RANGE_NOT_SATISFIABLE
    | EXPECTATION_FAILED
    | TEAPOT
    | MISDIRECTED_REQUEST
    | UNPROCESSABLE_ENTITY
    | LOCKED
    | FAILED_DEPENDENCY
    | TOO_EARLY
    | UPGRADE_REQUIRED
    | PRECONDITION_REQUIRED
    | TOO_MANY_REQUESTS
    | REQUEST_HEADER_FIELDS_TOO_LARGE
    | UNAVAILABLE_FOR_LEGAL_REASONS
    | INTERNAL_ERROR
    | NOT_IMPLEMENTED
    | BAD_GATEWAY
    | UNAVAILABLE
    | GATEWAY_TIMEOUT
    | VERSION
    | VARIANT_ALSO_NEGOTIATES
    | INSUFFICIENT_STORAGE
    | LOOP_DETECTED
    | NOT_EXTENDED
    | NETWORK_AUTHENTICATION_REQUIRED
    | ...
}
```

**功能：** 发起请求返回的响应码。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

### ACCEPTED

```cangjie
ACCEPTED
```

**功能：** 已经接受请求，但未处理完成。

**起始版本：** 12

### BAD_GATEWAY

```cangjie
BAD_GATEWAY
```

**功能：** 充当网关或代理的服务器，从远端服务器接收到了一个无效的请求。

**起始版本：** 12

### BAD_METHOD

```cangjie
BAD_METHOD
```

**功能：** 客户端请求中的方法被禁止。

**起始版本：** 12

### BAD_REQUEST

```cangjie
BAD_REQUEST
```

**功能：** 客户端请求的语法错误，服务器无法理解。

**起始版本：** 12

### CLIENT_TIMEOUT

```cangjie
CLIENT_TIMEOUT
```

**功能：** 请求时间过长，超时。

**起始版本：** 12

### CONFLICT

```cangjie
CONFLICT
```

**功能：** 服务器完成客户端的PUT请求是可能返回此代码，服务器处理请求时发生了冲突。

**起始版本：** 12

### CREATED

```cangjie
CREATED
```

**功能：** 成功请求并创建了新的资源。

**起始版本：** 12

### ENTITY_TOO_LARGE

```cangjie
ENTITY_TOO_LARGE
```

**功能：** 由于请求的实体过大，服务器无法处理，因此拒绝请求。

**起始版本：** 12

### EXPECTATION_FAILED

```cangjie
EXPECTATION_FAILED
```

**功能：** 此响应代码表示服务器无法满足Expect请求标头字段所指示的期望。

**起始版本：** 12

### FAILED_DEPENDENCY

```cangjie
FAILED_DEPENDENCY
```

**功能：** 由于前一个请求失败，本次请求失败。

**起始版本：** 12

### FORBIDDEN

```cangjie
FORBIDDEN
```

**功能：** 服务器理解请求客户端的请求，但是拒绝执行此请求。

**起始版本：** 12

### GATEWAY_TIMEOUT

```cangjie
GATEWAY_TIMEOUT
```

**功能：** 充当网关或代理的服务器，未及时从远端服务器获取请求。

**起始版本：** 12

### GONE

```cangjie
GONE
```

**功能：** 客户端请求的资源已经不存在。

**起始版本：** 12

### INSUFFICIENT_STORAGE

```cangjie
INSUFFICIENT_STORAGE
```

**功能：** 无法在资源上执行该方法，因为服务器无法存储成功完成请求所需的表示。

**起始版本：** 12

### INTERNAL_ERROR

```cangjie
INTERNAL_ERROR
```

**功能：** 服务器内部错误，无法完成请求。

**起始版本：** 12

### LENGTH_REQUIRED

```cangjie
LENGTH_REQUIRED
```

**功能：** 服务器无法处理客户端发送的不带Content-Length的请求信息。

**起始版本：** 12

### LOCKED

```cangjie
LOCKED
```

**功能：** 正在访问的资源已锁定。

**起始版本：** 12

### LOOP_DETECTED

```cangjie
LOOP_DETECTED
```

**功能：** 服务器在处理请求时检测到无限循环。

**起始版本：** 12

### MISDIRECTED_REQUEST

```cangjie
MISDIRECTED_REQUEST
```

**功能：** 请求被定向到无法生成响应的服务器。这可以由未配置为针对请求 URI 中包含的方案和权限组合生成响应的服务器发送。

**起始版本：** 12

### MOVED_PERM

```cangjie
MOVED_PERM
```

**功能：** 永久移动。请求的资源已被永久的移动到新URI，返回信息会包括新的URI，浏览器会自动定向到新URI。

**起始版本：** 12