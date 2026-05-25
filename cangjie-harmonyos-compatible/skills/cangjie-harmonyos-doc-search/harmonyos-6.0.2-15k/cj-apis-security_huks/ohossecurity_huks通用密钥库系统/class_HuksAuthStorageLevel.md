## class HuksAuthStorageLevel

```cangjie
public class HuksAuthStorageLevel {
    public static const HUKS_AUTH_STORAGE_LEVEL_DE: HuksParamValue = HuksParamValue.uint32(0)
    public static const HUKS_AUTH_STORAGE_LEVEL_CE: HuksParamValue = HuksParamValue.uint32(1)
    public static const HUKS_AUTH_STORAGE_LEVEL_ECE: HuksParamValue = HuksParamValue.uint32(2)
}
```

**功能：** 表示生成或导入密钥时，指定该密钥的存储安全等级。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

### static const HUKS_AUTH_STORAGE_LEVEL_CE

```cangjie
public static const HUKS_AUTH_STORAGE_LEVEL_CE: HuksParamValue = HuksParamValue.uint32(1)
```

**功能：** 表示密钥仅在首次解锁后可访问。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_AUTH_STORAGE_LEVEL_DE

```cangjie
public static const HUKS_AUTH_STORAGE_LEVEL_DE: HuksParamValue = HuksParamValue.uint32(0)
```

**功能：** 表示密钥仅在开机后可访问。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_AUTH_STORAGE_LEVEL_ECE

```cangjie
public static const HUKS_AUTH_STORAGE_LEVEL_ECE: HuksParamValue = HuksParamValue.uint32(2)
```

**功能：** 表示密钥仅在解锁状态时可访问。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15