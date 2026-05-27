## struct Portrait

```cangjie
public struct Portrait {
    public Portrait(
        public let uri: String)
}
```

**功能：** 联系人的头像类。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

### let uri

```cangjie
public let uri: String
```

**功能：** 联系人的头像。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### Portrait(String)

```cangjie
public Portrait(
    public let uri: String)
```

**功能：** 创建Portrait实例。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|uri|String|是|-|联系人的头像。|