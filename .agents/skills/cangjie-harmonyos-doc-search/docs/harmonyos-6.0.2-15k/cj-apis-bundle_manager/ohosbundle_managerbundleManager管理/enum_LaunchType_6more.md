## enum LaunchType

```cangjie
public enum LaunchType {
    | SINGLETON
    | MULTITON
    | SPECIFIED
    | ...
}
```

**功能：** 一个能力拥有一种启动类型，该枚举用于标明该能力的启动类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### MULTITON

```cangjie
MULTITON
```

**功能：** 能力以普通多实例的方式启动。

**起始版本：** 12

### SINGLETON

```cangjie
SINGLETON
```

**功能：** 能力以单实例的方式启动。

**起始版本：** 12

### SPECIFIED

```cangjie
SPECIFIED
```

**功能：** 能力以自定义多实例的方式启动。

**起始版本：** 12

## enum ModuleType

```cangjie
public enum ModuleType {
    | ENTRY
    | FEATURE
    | SHARED
    | ...
}
```

**功能：** 标识模块类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### ENTRY

```cangjie
ENTRY
```

**功能：** 应用的主模块。

**起始版本：** 12

### FEATURE

```cangjie
FEATURE
```

**功能：** 应用的动态特性模块。

**起始版本：** 12

### SHARED

```cangjie
SHARED
```

**功能：** 应用的动态共享库模块。

**起始版本：** 12

## enum MultiAppModeType

```cangjie
public enum MultiAppModeType {
    | UNSPECIFIED
    | MULTI_INSTANCE
    | APP_CLONE
    | ...
}
```

**功能：** 标识应用多开的模式类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 19

### APP_CLONE

```cangjie
APP_CLONE
```

**功能：** 分身模式。

**起始版本：** 19

### MULTI_INSTANCE

```cangjie
MULTI_INSTANCE
```

**功能：** 多实例模式。

**起始版本：** 19

### UNSPECIFIED

```cangjie
UNSPECIFIED
```

**功能：** 未指定类型。

**起始版本：** 19

## enum PermissionGrantState

```cangjie
public enum PermissionGrantState {
    | PERMISSION_DENIED
    | PERMISSION_GRANTED
    | ...
}
```

**功能：** 指示权限授予状态。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### PERMISSION_DENIED

```cangjie
PERMISSION_DENIED
```

**功能：** 拒绝授予权限。

**起始版本：** 12

### PERMISSION_GRANTED

```cangjie
PERMISSION_GRANTED
```

**功能：** 授予权限。

**起始版本：** 12

## enum ProfileType

```cangjie
public enum ProfileType {
    | INTENT_PROFILE
    | ...
}
```

**功能：** 标识配置文件类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### INTENT_PROFILE

```cangjie
INTENT_PROFILE
```

**功能：** 意图框架配置文件。

**起始版本：** 12

## enum SupportWindowMode

```cangjie
public enum SupportWindowMode {
    | FULL_SCREEN
    | SPLIT
    | FLOATING
    | ...
}
```

**功能：** 一个能力（Ability）可以支持若干个窗口模式，该枚举用于标明某个能力所支持的窗口模式。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### FLOATING

```cangjie
FLOATING
```

**功能：** 支持窗口化显示。

**起始版本：** 12

### FULL_SCREEN

```cangjie
FULL_SCREEN
```

**功能：** 窗口支持全屏显示。

**起始版本：** 12

### SPLIT

```cangjie
SPLIT
```

**功能：** 窗口支持分屏显示。

**起始版本：** 12