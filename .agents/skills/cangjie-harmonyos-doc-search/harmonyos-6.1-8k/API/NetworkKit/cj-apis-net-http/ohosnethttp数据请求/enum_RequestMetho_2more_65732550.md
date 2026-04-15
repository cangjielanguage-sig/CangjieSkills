## enum RequestMethod

```cangjie
public enum RequestMethod {
    | Options
    | Get
    | Head
    | Post
    | Put
    | Delete
    | Trace
    | Connect
    | ...
}
```

**功能：** HTTP请求方法。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### Connect

```cangjie
Connect
```

**功能：** Connect方法建立到由目标资源标识的服务器的隧道。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### Delete

```cangjie
Delete
```

**功能：** Delete方法用于删除指定的资源。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### Get

```cangjie
Get
```

**功能：** Get方法请求指定资源的表示。使用Get的请求应该只检索数据，不应该包含请求内容。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### Head

```cangjie
Head
```

**功能：** Head方法请求与Get请求相同的响应，但没有响应主体。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### Options

```cangjie
Options
```

**功能：** Options方法描述了目标资源的通信选项。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### Post

```cangjie
Post
```

**功能：** Post方法将实体提交给指定的资源，通常会导致服务器上的状态更改。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### Put

```cangjie
Put
```

**功能：** Put方法将目标资源的所有当前表示替换为请求内容。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### Trace

```cangjie
Trace
```

**功能：** Trace方法沿到达目标资源的路径执行消息环回测试。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

## enum UsingProxy

```cangjie
public enum UsingProxy {
    | NotUse
    | UseDefault
    | UseSpecified(HttpProxy)
    | ...
}
```

**功能：** 使用代理的类型。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### NotUse

```cangjie
NotUse
```

**功能：** 不使用代理。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### UseDefault

```cangjie
UseDefault
```

**功能：** 使用默认代理。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### UseSpecified(HttpProxy)

```cangjie
UseSpecified(HttpProxy)
```

**功能：** 使用指定类型代理。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22