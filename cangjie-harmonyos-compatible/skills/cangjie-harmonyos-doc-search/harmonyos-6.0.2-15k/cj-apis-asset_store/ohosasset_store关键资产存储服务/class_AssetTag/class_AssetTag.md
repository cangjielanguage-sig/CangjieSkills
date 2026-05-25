## class AssetTag

```cangjie
public class AssetTag {
    public static const SECRET: UInt32 = AssetTagType.BYTES | 0x01
    public static const ALIAS: UInt32 = AssetTagType.BYTES | 0x02
    public static const ACCESSIBILITY: UInt32 = AssetTagType.NUMBER | 0x03
    public static const REQUIRE_PASSWORD_SET: UInt32 = AssetTagType.BOOL | 0x04
    public static const AUTH_TYPE: UInt32 = AssetTagType.NUMBER | 0x05
    public static const AUTH_VALIDITY_PERIOD: UInt32 = AssetTagType.NUMBER | 0x06
    public static const AUTH_CHALLENGE: UInt32 = AssetTagType.BYTES | 0x07
    public static const AUTH_TOKEN: UInt32 = AssetTagType.BYTES | 0x08
    public static const SYNC_TYPE: UInt32 = AssetTagType.NUMBER | 0x10
    public static const IS_PERSISTENT: UInt32 = AssetTagType.BOOL | 0x11
    public static const DATA_LABEL_CRITICAL_1: UInt32 = AssetTagType.BYTES | 0x20
    public static const DATA_LABEL_CRITICAL_2: UInt32 = AssetTagType.BYTES | 0x21
    public static const DATA_LABEL_CRITICAL_3: UInt32 = AssetTagType.BYTES | 0x22
    public static const DATA_LABEL_CRITICAL_4: UInt32 = AssetTagType.BYTES | 0x23
    public static const DATA_LABEL_NORMAL_1: UInt32 = AssetTagType.BYTES | 0x30
    public static const DATA_LABEL_NORMAL_2: UInt32 = AssetTagType.BYTES | 0x31
    public static const DATA_LABEL_NORMAL_3: UInt32 = AssetTagType.BYTES | 0x32
    public static const DATA_LABEL_NORMAL_4: UInt32 = AssetTagType.BYTES | 0x33
    public static const DATA_LABEL_NORMAL_LOCAL_1: UInt32 = AssetTagType.BYTES | 0x34
    public static const DATA_LABEL_NORMAL_LOCAL_2: UInt32 = AssetTagType.BYTES | 0x35
    public static const DATA_LABEL_NORMAL_LOCAL_3: UInt32 = AssetTagType.BYTES | 0x36
    public static const DATA_LABEL_NORMAL_LOCAL_4: UInt32 = AssetTagType.BYTES | 0x37
    public static const RETURN_TYPE: UInt32 = AssetTagType.NUMBER | 0x40
    public static const RETURN_LIMIT: UInt32 = AssetTagType.NUMBER | 0x41
    public static const RETURN_OFFSET: UInt32 = AssetTagType.NUMBER | 0x42
    public static const RETURN_ORDERED_BY: UInt32 = AssetTagType.NUMBER | 0x43
    public static const CONFLICT_RESOLUTION: UInt32 = AssetTagType.NUMBER | 0x44
    public static const UPDATE_TIME: UInt32 = AssetTagType.BYTES | 0x45
    public static const OPERATION_TYPE: UInt32 = AssetTagType.NUMBER | 0x46
}
```

**功能：** 关键资产支持的属性名称类型，用作Asset_Attr的键。

以下为Tag类型的全量枚举值，每个接口可传的Tag及对应的值取值范围不同。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19