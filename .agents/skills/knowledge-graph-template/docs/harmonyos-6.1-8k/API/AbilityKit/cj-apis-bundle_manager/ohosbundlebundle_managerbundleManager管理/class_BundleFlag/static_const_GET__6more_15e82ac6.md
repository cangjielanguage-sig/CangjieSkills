### static const GET_BUNDLE_INFO_WITH_MENU

```cangjie
public static const GET_BUNDLE_INFO_WITH_MENU: Int32 = 0x00000100
```

**功能：** 用于获取包含fileContextMenuConfig的bundleInfo。单独使用不生效，需要与GET_BUNDLE_INFO_WITH_HAP_MODULE一起使用。

**类型：** Int32

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### static const GET_BUNDLE_INFO_WITH_METADATA

```cangjie
public static const GET_BUNDLE_INFO_WITH_METADATA: Int32 = 0x00000020
```

**功能：** 用于获取applicationInfo、moduleInfo、abilityInfo和extensionAbilityInfo中包含的metadata。

单独使用时无效，必须与以下权限配合使用：GET_BUNDLE_INFO_WITH_APPLICATION、GET_BUNDLE_INFO_WITH_HAP_MODULE、GET_BUNDLE_INFO_WITH_ABILITY、GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY。其中：

- 获取applicationInfo中包含的metadata，需要与GET_BUNDLE_INFO_WITH_APPLICATION一起使用。

- 获取moduleInfo中包含的metadata，需要与GET_BUNDLE_INFO_WITH_HAP_MODULE一起使用。

- 获取abilityInfo中包含的metadata，需要与GET_BUNDLE_INFO_WITH_HAP_MODULE、GET_BUNDLE_INFO_WITH_ABILITY一起使用。

- 获取extensionAbilityInfo中包含的metadata，需要与GET_BUNDLE_INFO_WITH_HAP_MODULE、GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY一起使用。

**类型：** Int32

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### static const GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION

```cangjie
public static const GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION: Int32 = 0x00000010
```

**功能：** 用于获取包含permission的bundleInfo。获取的bundleInfo不包含signatureInfo、applicationInfo、hapModuleInfo、extensionAbility和ability的信息。

**类型：** Int32

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### static const GET_BUNDLE_INFO_WITH_ROUTER_MAP

```cangjie
public static const GET_BUNDLE_INFO_WITH_ROUTER_MAP: Int32 = 0x00000200
```

**功能：** 用于获取包含routerMap的bundleInfo。单独使用不生效，需要与GET_BUNDLE_INFO_WITH_HAP_MODULE一起使用。

**类型：** Int32

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### static const GET_BUNDLE_INFO_WITH_SIGNATURE_INFO

```cangjie
public static const GET_BUNDLE_INFO_WITH_SIGNATURE_INFO: Int32 = 0x00000080
```

**功能：** 用于获取包含signatureInfo的bundleInfo。获取的bundleInfo不包含applicationInfo、hapModuleInfo、extensionAbility、ability和permission的信息。

**类型：** Int32

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### static const GET_BUNDLE_INFO_WITH_SKILL

```cangjie
public static const GET_BUNDLE_INFO_WITH_SKILL: Int32 = 0x00000800
```

**功能：** 用于获取包含skills的bundleInfo。单独使用不生效，需要与GET_BUNDLE_INFO_WITH_HAP_MODULE、GET_BUNDLE_INFO_WITH_ABILITY、GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY一起使用。

**类型：** Int32

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22