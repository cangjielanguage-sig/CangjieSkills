## enum BundleFlag

```cangjie
public enum BundleFlag {
    | GET_BUNDLE_INFO_DEFAULT
    | GET_BUNDLE_INFO_WITH_APPLICATION
    | GET_BUNDLE_INFO_WITH_HAP_MODULE
    | GET_BUNDLE_INFO_WITH_ABILITY
    | GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY
    | GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION
    | GET_BUNDLE_INFO_WITH_METADATA
    | GET_BUNDLE_INFO_WITH_DISABLE
    | GET_BUNDLE_INFO_WITH_SIGNATURE
    | GET_BUNDLE_INFO_WITH_MENU
    | GET_BUNDLE_INFO_WITH_ROUTER_MAP
    | GET_BUNDLE_INFO_WITH_SKILL
    | ...
}
```

**功能：** 包信息标志，指示需要获取的包信息的内容。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### GET_BUNDLE_INFO_DEFAULT

```cangjie
GET_BUNDLE_INFO_DEFAULT
```

**功能：** 只获取最基础的应用包信息。获取到的应用包信息中不包含HAP模块信息、应用信息、签名信息和权限申请信息。

**起始版本：** 12

### GET_BUNDLE_INFO_WITH_ABILITY

```cangjie
GET_BUNDLE_INFO_WITH_ABILITY
```

**功能：** 必须与`GET_BUNDLE_INFO_WITH_HAP_MODULE`同时指定，使得获取到的HAP模块信息中包含能力信息，但不包含能力信息中的元数据。

**起始版本：** 12

### GET_BUNDLE_INFO_WITH_APPLICATION

```cangjie
GET_BUNDLE_INFO_WITH_APPLICATION
```

**功能：** 在最基础的应用包信息的基础上，附带上应用信息，但不包含应用信息中的元数据。

**起始版本：** 12

### GET_BUNDLE_INFO_WITH_DISABLE

```cangjie
GET_BUNDLE_INFO_WITH_DISABLE
```

**功能：** 用于获取application被禁用的BundleInfo和被禁用的Ability信息。获取的bundleInfo不包含signatureInfo、applicationInfo、hapModuleInfo、ability、extensionAbility和permission的信息。

**起始版本：** 12

### GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY

```cangjie
GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY
```

**功能：** 必须与`GET_BUNDLE_INFO_WITH_HAP_MODULE`同时指定，使得获取到的HAP模块信息中包含拓展能力信息，但不包含拓展能力信息中的元数据。

**起始版本：** 12

### GET_BUNDLE_INFO_WITH_HAP_MODULE

```cangjie
GET_BUNDLE_INFO_WITH_HAP_MODULE
```

**功能：** 在最基础的应用包信息的基础上，附带上HAP模块信息，但不包含HAP模块信息中的能力信息、拓展能力信息和元数据。

**起始版本：** 12

### GET_BUNDLE_INFO_WITH_MENU

```cangjie
GET_BUNDLE_INFO_WITH_MENU
```

**功能：** 用于获取包含fileContextMenuConfig的bundleInfo。它不能单独使用，需要与GET_BUNDLE_INFO_WITH_HAP_MODULE一起使用。

**起始版本：** 12

### GET_BUNDLE_INFO_WITH_METADATA

```cangjie
GET_BUNDLE_INFO_WITH_METADATA
```

**功能：** 获取所有的元数据，包括HAP模块信息、能力信息、拓展能力信息和应用信息中的元数据，因此必须与`GET_BUNDLE_INFO_WITH_HAP_MODULE`、`GET_BUNDLE_INFO_WITH_ABILITY`、`GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY`和`GET_BUNDLE_INFO_WITH_APPLICATION`同时指定。

**起始版本：** 12

### GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION

```cangjie
GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION
```

**功能：** 在最基础的应用包信息的基础上，附带上权限申请信息。

**起始版本：** 12

### GET_BUNDLE_INFO_WITH_ROUTER_MAP

```cangjie
GET_BUNDLE_INFO_WITH_ROUTER_MAP
```

**功能：** 用于获取包含routerMap的bundleInfo。它不能单独使用，需要与GET_BUNDLE_INFO_WITH_HAP_MODULE一起使用。

**起始版本：** 19

### GET_BUNDLE_INFO_WITH_SIGNATURE

```cangjie
GET_BUNDLE_INFO_WITH_SIGNATURE
```

**功能：** 在最基础的应用包信息的基础上，附带上签名信息。

**起始版本：** 12

### GET_BUNDLE_INFO_WITH_SKILL

```cangjie
GET_BUNDLE_INFO_WITH_SKILL
```

**功能：** 用于获取包含skills的bundleInfo。它不能单独使用，需要与GET_BUNDLE_INFO_WITH_HAP_MODULE、GET_BUNDLE_INFO_WITH_ABILITY、GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY一起使用。

**起始版本：** 19