## class BundleFlag

```cangjie
public class BundleFlag {
    public static const GET_BUNDLE_INFO_DEFAULT: Int32 = 0x00000000
    public static const GET_BUNDLE_INFO_WITH_APPLICATION: Int32 = 0x00000001
    public static const GET_BUNDLE_INFO_WITH_HAP_MODULE: Int32 = 0x00000002
    public static const GET_BUNDLE_INFO_WITH_ABILITY: Int32 = 0x00000004
    public static const GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY: Int32 = 0x00000008
    public static const GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION: Int32 = 0x00000010
    public static const GET_BUNDLE_INFO_WITH_METADATA: Int32 = 0x00000020
    public static const GET_BUNDLE_INFO_WITH_DISABLE: Int32 = 0x00000040
    public static const GET_BUNDLE_INFO_WITH_SIGNATURE_INFO: Int32 = 0x00000080
    public static const GET_BUNDLE_INFO_WITH_MENU: Int32 = 0x00000100
    public static const GET_BUNDLE_INFO_WITH_ROUTER_MAP: Int32 = 0x00000200
    public static const GET_BUNDLE_INFO_WITH_SKILL: Int32 = 0x00000800
}
```

**功能：** 包信息标志，指示需要获取的包信息的内容。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### static const GET_BUNDLE_INFO_DEFAULT

```cangjie
public static const GET_BUNDLE_INFO_DEFAULT: Int32 = 0x00000000
```

**功能：** 获取默认包信息，不包含signatureInfo、applicationInfo、hapModuleInfo、ability、extensionAbility和permission的信息。

**类型：** Int32

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### static const GET_BUNDLE_INFO_WITH_ABILITY

```cangjie
public static const GET_BUNDLE_INFO_WITH_ABILITY: Int32 = 0x00000004
```

**功能：** 用于获取包含ability的bundleInfo，获取的bundleInfo不包含signatureInfo、applicationInfo、extensionAbility和permission的信息。单独使用不生效，需要与GET_BUNDLE_INFO_WITH_HAP_MODULE一起使用。

**类型：** Int32

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### static const GET_BUNDLE_INFO_WITH_APPLICATION

```cangjie
public static const GET_BUNDLE_INFO_WITH_APPLICATION: Int32 = 0x00000001
```

**功能：** 用于获取包含applicationInfo的bundleInfo，获取的bundleInfo不包含signatureInfo、hapModuleInfo、ability、extensionAbility和permission的信息。

**类型：** Int32

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### static const GET_BUNDLE_INFO_WITH_DISABLE

```cangjie
public static const GET_BUNDLE_INFO_WITH_DISABLE: Int32 = 0x00000040
```

**功能：** 用于获取application被禁用的BundleInfo和被禁用的Ability信息。获取的bundleInfo不包含signatureInfo、applicationInfo、hapModuleInfo、ability、extensionAbility和permission的信息。

**类型：** Int32

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### static const GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY

```cangjie
public static const GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY: Int32 = 0x00000008
```

**功能：** 用于获取包含extensionAbility的bundleInfo，获取的bundleInfo不包含signatureInfo、applicationInfo、ability 和permission的信息。单独使用不生效，需要与GET_BUNDLE_INFO_WITH_HAP_MODULE一起使用。

**类型：** Int32

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### static const GET_BUNDLE_INFO_WITH_HAP_MODULE

```cangjie
public static const GET_BUNDLE_INFO_WITH_HAP_MODULE: Int32 = 0x00000002
```

**功能：** 用于获取包含hapModuleInfo的bundleInfo，获取的bundleInfo不包含signatureInfo、applicationInfo、ability、extensionAbility和permission的信息。

**类型：** Int32

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22