## enum ExtensionAbilityType

```cangjie
public enum ExtensionAbilityType {
    | WorkScheduler
    | InputMethod
    | Service
    | Accessibility
    | DataShare
    | FileShare
    | StaticSubscriber
    | Wallpaper
    | Backup
    | Window
    | EnterpriseAdmin
    | Thumbnail
    | Preview
    | Print
    | Share
    | Push
    | Driver
    | Action
    | AdsService
    | EmbeddedUI
    | InsightIntentUI
    | Unspecified
    | ...
}
```

**功能：** 扩展组件的类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### Accessibility

```cangjie
Accessibility
```

**功能：** 无障碍服务扩展能力，支持访问与操作前台界面。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### Action

```cangjie
Action
```

**功能：** 自定义服务扩展能力，为开发者提供基于UIExtension的自定义操作业务模板。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### AdsService

```cangjie
AdsService
```

**功能：** 广告服务扩展能力，对外提供后台自定义广告业务服务，仅系统应用支持。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### Backup

```cangjie
Backup
```

**功能：** 数据备份扩展能力，提供应用数据的备份恢复能力。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### DataShare

```cangjie
DataShare
```

**功能：** 数据共享扩展能力，用于对外提供数据读写服务。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### Driver

```cangjie
Driver
```

**功能：** 提供外设驱动扩展能力。应用配置driver类型的ExtensionAbility后，被视为驱动应用，安装、卸载和恢复驱动应用时，不区分用户。创建新用户时，设备上已有的驱动应用也会安装。例如，创建子用户时，默认安装主用户已有的驱动应用。在子用户上卸载驱动应用时，主用户上对应的驱动应用也会被卸载。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### EmbeddedUI

```cangjie
EmbeddedUI
```

**功能：** 嵌入式UI扩展能力，提供跨进程界面嵌入的能力。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### EnterpriseAdmin

```cangjie
EnterpriseAdmin
```

**功能：** 企业设备管理扩展能力，提供企业管理时处理管理事件的能力，比如设备上应用安装事件、锁屏密码输入错误次数过多事件等。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### FileShare

```cangjie
FileShare
```

**功能：** 文件共享扩展能力，用于应用间的文件分享。预留能力，仅系统应用支持。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### InputMethod

```cangjie
InputMethod
```

**功能：** 输入法扩展能力，用于开发输入法应用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### InsightIntentUI

```cangjie
InsightIntentUI
```

**功能：** 为开发者提供能被小艺意图调用，以窗口形态呈现内容的扩展能力。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### Preview

```cangjie
Preview
```

**功能：** 文件预览扩展，支持系统应用直接嵌入显示。预留能力，仅系统应用支持。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### Print

```cangjie
Print
```

**功能：** 文件打印扩展，提供应用打印照片、文档等办公场景能力。仅系统应用支持。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### Push

```cangjie
Push
```

**功能：** 推送扩展能力，提供推送场景化消息能力。预留能力，仅系统应用支持。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22