## class DomainAccountInfo

```cangjie
public class DomainAccountInfo {
    public DomainAccountInfo(
        public let domain: String,
        public let accountName: String
    )
}
```

**功能：** 表示域账号信息。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

### let accountName

```cangjie
public let accountName: String
```

**功能：** 域账号名。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let domain

```cangjie
public let domain: String
```

**功能：** 域名。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### DomainAccountInfo(String, String)

```cangjie
public DomainAccountInfo(
    public let domain: String,
    public let accountName: String
)
```

**功能：** 构造DomainAccountInfo对象。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|domain|String|是|-|域名。|
|accountName|String|是|-|域账号名。|