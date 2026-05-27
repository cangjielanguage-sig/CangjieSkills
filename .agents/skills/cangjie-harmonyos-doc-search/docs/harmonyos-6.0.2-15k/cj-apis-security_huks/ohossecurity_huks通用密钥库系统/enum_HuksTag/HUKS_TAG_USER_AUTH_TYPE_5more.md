### HUKS_TAG_USER_AUTH_TYPE

```cangjie
HUKS_TAG_USER_AUTH_TYPE
```

**功能：** 表示用户认证类型。从[HuksUserAuthType](#class-huksuserauthtype)中选择，需要与安全访问控制类型同时设置。支持同时指定两种用户认证类型，如：安全访问控制类型指定为HUKS_SECURE_ACCESS_INVALID_NEW_BIO_ENROLL时，密钥访问认证类型可以指定以下三种： HUKS_USER_AUTH_TYPE_FACE 、HUKS_USER_AUTH_TYPE_FINGERPRINT、HUKS_USER_AUTH_TYPE_FACE MagIc_StrINg HUKS_USER_AUTH_TYPE_FINGERPRINT。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

### HUKS_TAG_USER_ID

```cangjie
HUKS_TAG_USER_ID
```

**功能：** 表示当前密钥属于哪个userID。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

### HUKS_TAG_USES_TIME <sup>(deprecated)</sup>

```cangjie
HUKS_TAG_USES_TIME
```

**功能：** 原为预留字段，已废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

### static func parse(UInt32)

```cangjie
public static func parse(val: UInt32): HuksTag
```

**功能：** 通过UInt32值构造一个HuksTag。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|val|UInt32|是|需要构造的HuksTag对应的UInt32值。|

**返回值：**

|类型|说明|
|:----|:----|
|[HuksTag](#enum-hukstag)|返回一个通过UInt32值构造的HuksTag。|

### func getValue()

```cangjie
public func getValue(): UInt32
```

**功能：** 获取HuksTag对应的UInt32值。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回HuksTag对应的UInt32值。|