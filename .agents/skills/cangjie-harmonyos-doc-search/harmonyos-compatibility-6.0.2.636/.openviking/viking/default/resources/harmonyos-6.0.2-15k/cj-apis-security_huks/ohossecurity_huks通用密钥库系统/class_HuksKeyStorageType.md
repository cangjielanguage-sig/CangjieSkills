## class HuksKeyStorageType

```cangjie
public class HuksKeyStorageType {
    public static const HUKS_STORAGE_TEMP: HuksParamValue = HuksParamValue.uint32(0)
    public static const HUKS_STORAGE_PERSISTENT: HuksParamValue = HuksParamValue.uint32(1)
    public static const HUKS_STORAGE_ONLY_USED_IN_HUKS: HuksParamValue = HuksParamValue.uint32(2)
    public static const HUKS_STORAGE_KEY_EXPORT_ALLOWED: HuksParamValue = HuksParamValue.uint32(3)
}
```

**功能：** 表示密钥存储方式。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

### static const HUKS_STORAGE_KEY_EXPORT_ALLOWED

```cangjie
public static const HUKS_STORAGE_KEY_EXPORT_ALLOWED: HuksParamValue = HuksParamValue.uint32(3)
```

**功能：** 表示主密钥派生的密钥直接导出给业务方，HUKS不对其进行托管服务。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_STORAGE_ONLY_USED_IN_HUKS

```cangjie
public static const HUKS_STORAGE_ONLY_USED_IN_HUKS: HuksParamValue = HuksParamValue.uint32(2)
```

**功能：** 表示主密钥派生的密钥存储于huks中，由HUKS进行托管。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_STORAGE_PERSISTENT <sup>(deprecated)</sup>

```cangjie
public static const HUKS_STORAGE_PERSISTENT: HuksParamValue = HuksParamValue.uint32(1)
```

**功能：** 表示通过HUKS service管理密钥。

**说明：** 已废弃，由于开发者正常使用密钥管理过程中并不需要使用此Tag，故无替代接口。针对密钥派生场景，可使用HUKS_STORAGE_ONLY_USED_IN_HUKS 与 HUKS_STORAGE_KEY_EXPORT_ALLOWED。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_STORAGE_TEMP <sup>(deprecated)</sup>

```cangjie
public static const HUKS_STORAGE_TEMP: HuksParamValue = HuksParamValue.uint32(0)
```

**功能：** 表示通过本地直接管理密钥。

**说明：** 已废弃，由于开发者正常使用密钥管理过程中并不需要使用此Tag，故无替代接口。针对密钥派生场景，可使用HUKS_STORAGE_ONLY_USED_IN_HUKS 与 HUKS_STORAGE_KEY_EXPORT_ALLOWED。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15