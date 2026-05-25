### var resumeFrom

```cangjie
public var resumeFrom: Int64
```

**功能：** 用于设置下载起始位置，该参数只能用于GET方法，不能用于其他。HTTP标准（RFC 7233第3.1节）允许服务器忽略范围请求。<br />- 使用HTTP PUT时，不能使用该选项，因为该选项可能与其他选项冲突。<br />- 取值范围是：[1，4294967296（4GB）]，超出范围则不生效。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var resumeTo

```cangjie
public var resumeTo: Int64
```

**功能：** 用于设置下载结束位置，该参数只能用于GET方法，不能用于其他。HTTP标准（RFC 7233第3.1节）允许服务器忽略范围请求。<br />- 使用HTTP PUT时，不能使用该选项，因为该选项可能与其他选项冲突。<br />- 取值范围是：[1，4294967296（4GB）]，超出范围则不生效。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var usingCache

```cangjie
public var usingCache: Bool
```

**功能：** 是否使用缓存，true表示请求时优先读取缓存，false表示不使用缓存；请求时优先读取缓存。缓存跟随当前进程生效，新缓存会替换旧缓存。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var usingProtocol

```cangjie
public var usingProtocol: ?HttpProtocol
```

**功能：** 使用协议。

**类型：** ?[HttpProtocol](#enum-httpprotocol)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var usingProxy

```cangjie
public var usingProxy: UsingProxy
```

**功能：** HTTP代理配置，该项不配置时表示不使用代理。<br />- 当usingProxy为布尔类型true时，使用默认网络代理，为false时，不使用代理。<br />- 当usingProxy为HttpProxy类型时，使用指定网络代理。当前HttpProxy不支持指定username和password字段。

**类型：** [UsingProxy](#enum-usingproxy)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22