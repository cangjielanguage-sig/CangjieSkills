## enum ExtensionAbilityFlag

```cangjie
public enum ExtensionAbilityFlag {
    | GET_EXTENSION_ABILITY_INFO_DEFAULT
    | GET_EXTENSION_ABILITY_INFO_WITH_PERMISSION
    | GET_EXTENSION_ABILITY_INFO_WITH_APPLICATION
    | GET_EXTENSION_ABILITY_INFO_WITH_METADATA
    | ...
}
```

**功能：** 扩展组件信息标志，指示需要获取的扩展组件信息的内容。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### GET_EXTENSION_ABILITY_INFO_DEFAULT

```cangjie
GET_EXTENSION_ABILITY_INFO_DEFAULT
```

**功能：** 用于获取默认extensionAbilityInfo。获取的extensionAbilityInfo不包含permission、metadata和禁用的abilityInfo。

**起始版本：** 12

### GET_EXTENSION_ABILITY_INFO_WITH_APPLICATION

```cangjie
GET_EXTENSION_ABILITY_INFO_WITH_APPLICATION
```

**功能：** 用于获取包含applicationInfo的extensionAbilityInfo。

**起始版本：** 12

### GET_EXTENSION_ABILITY_INFO_WITH_METADATA

```cangjie
GET_EXTENSION_ABILITY_INFO_WITH_METADATA
```

**功能：** 用于获取包含metadata的extensionAbilityInfo。

**起始版本：** 12

### GET_EXTENSION_ABILITY_INFO_WITH_PERMISSION

```cangjie
GET_EXTENSION_ABILITY_INFO_WITH_PERMISSION
```

**功能：** 用于获取包含permission的extensionAbilityInfo。

**起始版本：** 12