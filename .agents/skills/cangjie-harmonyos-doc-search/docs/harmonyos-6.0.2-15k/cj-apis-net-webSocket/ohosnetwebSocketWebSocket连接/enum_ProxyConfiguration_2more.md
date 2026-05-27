## enum ProxyConfiguration

```cangjie
public enum ProxyConfiguration {
    | NO_PROXY
    | SYSTEM
    | HTTPPROXY(WebSocketHttpProxy)
    | ...
}
```

**功能：** 网络代理配置信息。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

### HTTPPROXY(WebSocketHttpProxy)

```cangjie
HTTPPROXY(WebSocketHttpProxy)
```

**功能：** 使用指定的网络代理。

**起始版本：** 19

### NO_PROXY

```cangjie
NO_PROXY
```

**功能：** 不使用网络代理。

**起始版本：** 19

### SYSTEM

```cangjie
SYSTEM
```

**功能：** 使用系统默认网络代理。

**起始版本：** 19

## enum ResponseHeaders

```cangjie
public enum ResponseHeaders {
    | MAP_DATA(HashMap<String, String>)
    | ARRAY_STRING_DATA(Array<String>)
    | UNDEFINED_DATA
    | ...
}
```

**功能：** 服务器发送的响应头。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

### ARRAY_STRING_DATA(Array\<String>)

```cangjie
ARRAY_STRING_DATA(Array<String>)
```

**功能：** header数据类型为字符串数组。

**起始版本：** 19

### MAP_DATA(HashMap\<String, String>)

```cangjie
MAP_DATA(HashMap<String, String>)
```

**功能：** header数据类型为键值对。

**起始版本：** 19

### UNDEFINED_DATA

```cangjie
UNDEFINED_DATA
```

**功能：** header数据类型为undefined。

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回字符串形式的[ResponseHeaders](#enum-responseheaders)。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|字符串。|