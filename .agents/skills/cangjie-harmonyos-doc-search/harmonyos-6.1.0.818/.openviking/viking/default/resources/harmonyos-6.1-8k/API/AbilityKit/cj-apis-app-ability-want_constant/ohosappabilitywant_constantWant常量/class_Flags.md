## class Flags

```cangjie
public class Flags {
    public static const FLAG_AUTH_READ_URI_PERMISSION: UInt32 = 0x00000001
    public static const FLAG_AUTH_WRITE_URI_PERMISSION: UInt32 = 0x00000002
    public static const FLAG_AUTH_PERSISTABLE_URI_PERMISSION: UInt32 = 0x00000040
    public static const FLAG_INSTALL_ON_DEMAND: UInt32 = 0x00000800
    public static const FLAG_START_WITHOUT_TIPS: UInt32 = 0x40000000
}
```

**功能：** [Want.flags](./cj-apis-app-ability-want.md#class-want)字段常用的系统预置关键字。开发者可以通过这些预置关键字设置或获取应用跳转等场景中额外携带的标志位信息。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### static const FLAG_AUTH_PERSISTABLE_URI_PERMISSION

```cangjie
public static const FLAG_AUTH_PERSISTABLE_URI_PERMISSION: UInt32 = 0x00000040
```

**功能：** 表示该URI可被接收方持久化。该字段仅在Tablet设备上生效。

**类型：** UInt32

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### static const FLAG_AUTH_READ_URI_PERMISSION

```cangjie
public static const FLAG_AUTH_READ_URI_PERMISSION: UInt32 = 0x00000001
```

**功能：** 表示临时授予接收方读取该URI指向的数据的权限。

**类型：** UInt32

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### static const FLAG_AUTH_WRITE_URI_PERMISSION

```cangjie
public static const FLAG_AUTH_WRITE_URI_PERMISSION: UInt32 = 0x00000002
```

**功能：** 表示临时授予接收方写入该URI指向的数据的权限。

**类型：** UInt32

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### static const FLAG_INSTALL_ON_DEMAND

```cangjie
public static const FLAG_INSTALL_ON_DEMAND: UInt32 = 0x00000800
```

**功能：** 表示拉起原子化服务时开启免安装功能。

- 如果开启了免安装功能，当系统检测到被拉起的原子化服务未安装时，会自动安装原子化服务，再进行拉起。

- 如果未开启免安装功能，当原子化服务未安装时，将拉起失败。

**类型：** UInt32

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### static const FLAG_START_WITHOUT_TIPS

```cangjie
public static const FLAG_START_WITHOUT_TIPS: UInt32 = 0x40000000
```

**功能：** 表示是否关闭匹配失败弹窗功能。

通过隐式方式拉起应用时，如果没有能够匹配的应用，默认会弹出提示弹窗“暂无可用打开方式”。开发者可以通过该字段屏蔽该弹窗。

**类型：** UInt32

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22