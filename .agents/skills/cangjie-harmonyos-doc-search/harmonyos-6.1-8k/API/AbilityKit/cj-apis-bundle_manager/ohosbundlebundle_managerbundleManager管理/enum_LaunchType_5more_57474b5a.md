## enum LaunchType

```cangjie
public enum LaunchType {
    | Singleton
    | Multiton
    | Specified
    | ...
}
```

**功能：** 标识组件的启动模式。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### Multiton

```cangjie
Multiton
```

**功能：** UIAbility的启动模式，表示普通多实例。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### Singleton

```cangjie
Singleton
```

**功能：** UIAbility的启动模式，表示单实例。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### Specified

```cangjie
Specified
```

**功能：** UIAbility的启动模式，表示该UIAbility内部根据业务自己指定多实例。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

## enum ModuleType

```cangjie
public enum ModuleType {
    | Entry
    | Feature
    | Shared
    | ...
}
```

**功能：** 标识模块类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### Entry

```cangjie
Entry
```

**功能：** 应用的主模块，作为应用的入口，提供了应用的基础功能。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### Feature

```cangjie
Feature
```

**功能：** 应用的动态特性模块，作为应用能力的扩展，可以根据用户的需求和设备类型进行选择性安装。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### Shared

```cangjie
Shared
```

**功能：** 应用的动态共享库模块。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

## enum MultiAppModeType

```cangjie
public enum MultiAppModeType {
    | Unspecified
    | MultiInstance
    | AppClone
    | ...
}
```

**功能：** 标识应用多开的模式类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### AppClone

```cangjie
AppClone
```

**功能：** 分身模式。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### MultiInstance

```cangjie
MultiInstance
```

**功能：** 多实例模式。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### Unspecified

```cangjie
Unspecified
```

**功能：** 未指定类型，表示multiAppMode配置未配置时的默认状态。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

## enum PermissionGrantState

```cangjie
public enum PermissionGrantState {
    | PermissionDenied
    | PermissionGranted
    | ...
}
```

**功能：** 权限授予状态。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### PermissionDenied

```cangjie
PermissionDenied
```

**功能：** 拒绝授予权限。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### PermissionGranted

```cangjie
PermissionGranted
```

**功能：** 授予权限。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

## enum SupportedWindowMode

```cangjie
public enum SupportedWindowMode {
    | FullScreen
    | Split
    | Floating
    | ...
}
```

**功能：** 支持窗口模式。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### FullScreen

```cangjie
FullScreen
```

**功能：** 表示支持全屏模式的窗口模式。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### Split

```cangjie
Split
```

**功能：**表示支持分屏模式的窗口模式。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### Floating

```cangjie
Floating
```

**功能：** 表示支持浮动模式的窗口模式。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22