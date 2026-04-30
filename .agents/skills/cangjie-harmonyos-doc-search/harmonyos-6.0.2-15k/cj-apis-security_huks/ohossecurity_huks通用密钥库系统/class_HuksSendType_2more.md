## class HuksSendType

```cangjie
public class HuksSendType {
    public static const HUKS_SEND_TYPE_ASYNC: HuksParamValue = HuksParamValue.uint32(0)
    public static const HUKS_SEND_TYPE_SYNC: HuksParamValue = HuksParamValue.uint32(1)
}
```

**功能：** 表示发送Tag的方式。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

### static const HUKS_SEND_TYPE_ASYNC

```cangjie
public static const HUKS_SEND_TYPE_ASYNC: HuksParamValue = HuksParamValue.uint32(0)
```

**功能：** 表示异步发送Tag。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_SEND_TYPE_SYNC

```cangjie
public static const HUKS_SEND_TYPE_SYNC: HuksParamValue = HuksParamValue.uint32(1)
```

**功能：** 表示同步发送Tag。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

## class HuksSessionHandle

```cangjie
public class HuksSessionHandle {
    public HuksSessionHandle(
        public let handle: HuksHandle,
        public let challenge: Option<Array<UInt8>>
    )
}
```

**功能：** huks Handle结构体。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

### let challenge

```cangjie
public let challenge: Option<Array<UInt8>>
```

**功能：** 表示[initSession](#func-initsessionstring-huksoptions)操作之后获取到的challenge信息。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** Option\<Array\<UInt8>>

**读写能力：** 只读

**起始版本：** 15

### let handle

```cangjie
public let handle: HuksHandle
```

**功能：** 表示handle值。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksHandle](#class-hukshandle)

**读写能力：** 只读

**起始版本：** 15

### HuksSessionHandle(HuksHandle, Option\<Array\<UInt8>>)

```cangjie
public HuksSessionHandle(
    public let handle: HuksHandle,
    public let challenge: Option<Array<UInt8>>
)
```

**功能：** 构建HuksSessionHandle实例。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|handle|[HuksHandle](#class-hukshandle)|是|表示handle值。|
|challenge|Option\<Array\<UInt8>>|是|表示[initSession](#func-initsessionstring-huksoptions)操作之后获取到的challenge信息。|