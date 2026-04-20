## class ProxyData

```cangjie
public class ProxyData {
    public ProxyData (
        public var key: String,
        public var subscriberId!: ?String = None
    )
}
```

**功能：** 卡片代理刷新订阅数据信息。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 19

### var key

```cangjie
public var key: String
```

**功能：** 卡片代理刷新的订阅标识，与数据发布者保持一致。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var subscriberId

```cangjie
public var subscriberId: ?String = None
```

**功能：** 卡片代理刷新的订阅条件，默认值为当前卡片的formId。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### ProxyData(String, ?String)

```cangjie
public ProxyData (
    public var key: String,
    public var subscriberId!: ?String = None
)
```

**功能：** 构造ProxyData的对象。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|卡片代理刷新的订阅标识，与数据发布者保持一致。|
|subscriberId|?String|否|None| **命名参数。** 卡片代理刷新的订阅条件，默认值为当前卡片的formId。|