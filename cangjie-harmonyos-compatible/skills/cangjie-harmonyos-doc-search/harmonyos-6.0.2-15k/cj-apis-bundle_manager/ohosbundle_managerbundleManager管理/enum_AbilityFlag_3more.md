## enum AbilityFlag

```cangjie
public enum AbilityFlag {
    | GET_ABILITY_INFO_DEFAULT
    | GET_ABILITY_INFO_WITH_PERMISSION
    | GET_ABILITY_INFO_WITH_APPLICATION
    | GET_ABILITY_INFO_WITH_METADATA
    | GET_ABILITY_INFO_WITH_DISABLE
    | GET_ABILITY_INFO_ONLY_SYSTEM_APP
    | ...
}
```

**功能：** UIAbility组件信息标志，指示需要获取的UIAbility组件信息的内容。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### GET_ABILITY_INFO_DEFAULT

```cangjie
GET_ABILITY_INFO_DEFAULT
```

**功能：** 用于获取默认abilityInfo，获取的abilityInfo不包含permission、metadata和禁用的abilityInfo。

**起始版本：** 12

### GET_ABILITY_INFO_ONLY_SYSTEM_APP

```cangjie
GET_ABILITY_INFO_ONLY_SYSTEM_APP
```

**功能：** 用于仅为系统应用程序获取abilityInfo。

**起始版本：** 12

### GET_ABILITY_INFO_WITH_APPLICATION

```cangjie
GET_ABILITY_INFO_WITH_APPLICATION
```

**功能：** 用于获取包含applicationInfo的abilityInfo。

**起始版本：** 12

### GET_ABILITY_INFO_WITH_DISABLE

```cangjie
GET_ABILITY_INFO_WITH_DISABLE
```

**功能：** 用于获取包含禁用的abilityInfo的abilityInfo。

**起始版本：** 12

### GET_ABILITY_INFO_WITH_METADATA

```cangjie
GET_ABILITY_INFO_WITH_METADATA
```

**功能：** 用于获取包含metadata的abilityInfo。

**起始版本：** 12

### GET_ABILITY_INFO_WITH_PERMISSION

```cangjie
GET_ABILITY_INFO_WITH_PERMISSION
```

**功能：** 用于获取包含permission的abilityInfo。

**起始版本：** 12

## enum AbilityType

```cangjie
public enum AbilityType {
    | PAGE
    | SERVICE
    | DATA
    | ...
}
```

**功能：** 指示Ability组件的类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### DATA

```cangjie
DATA
```

**功能：** 表示基于Data模板开发的PA，用于对外部提供统一的数据访问对象。

**起始版本：** 12

### PAGE

```cangjie
PAGE
```

**功能：** UI界面类型的Ability。表示基于Page模板开发的FA，用于提供与用户交互的能力。

**起始版本：** 12

### SERVICE

```cangjie
SERVICE
```

**功能：** 后台服务类型的Ability，无UI界面。表示基于Service模板开发的PA，用于提供后台运行任务的能力。

**起始版本：** 12

## enum ApplicationFlag

```cangjie
public enum ApplicationFlag {
    | GET_APPLICATION_INFO_DEFAULT
    | GET_APPLICATION_INFO_WITH_PERMISSION
    | GET_APPLICATION_INFO_WITH_METADATA
    | GET_APPLICATION_INFO_WITH_DISABLE
    | ...
}
```

**功能：** 应用信息标志，指示需要获取的应用信息的内容。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### GET_APPLICATION_INFO_DEFAULT

```cangjie
GET_APPLICATION_INFO_DEFAULT
```

**功能：** 用于获取默认的applicationInfo，获取的applicationInfo不包含permission和metadata信息。

**起始版本：** 12

### GET_APPLICATION_INFO_WITH_DISABLE

```cangjie
GET_APPLICATION_INFO_WITH_DISABLE
```

**功能：** 用于获取包含禁用应用程序的applicationInfo。

**起始版本：** 12

### GET_APPLICATION_INFO_WITH_METADATA

```cangjie
GET_APPLICATION_INFO_WITH_METADATA
```

**功能：** 用于获取包含metadata的applicationInfo。

**起始版本：** 12

### GET_APPLICATION_INFO_WITH_PERMISSION

```cangjie
GET_APPLICATION_INFO_WITH_PERMISSION
```

**功能：** 用于获取包含permission的applicationInfo。

**起始版本：** 12