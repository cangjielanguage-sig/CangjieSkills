### let usingProtocol

```cangjie
public let usingProtocol: ?HttpProtocol = None
```

**功能：** 使用协议。默认值由系统自动指定。

**类型：** ?[HttpProtocol](#enum-httpprotocol)

**读写能力：** 只读

**起始版本：** 12

### let usingProxy

```cangjie
public let usingProxy: UsingProxy = USE_DEFAULT
```

**功能：** 是否使用HTTP代理，默认为USE_DEFAULT，使用默认代理。<br /> 当usingProxy为NOT_USE时，不使用网络代理。<br /> 当usingProxy为USE_SPECIFIED类型时，使用指定网络代理。

**类型：** [UsingProxy](#enum-usingproxy)

**读写能力：** 只读

**起始版本：** 12