## enum ExtensionAbilityType

```cangjie
public enum ExtensionAbilityType {
    | FORM
    | WORK_SCHEDULER
    | INPUT_METHOD
    | SERVICE
    | ACCESSIBILITY
    | DATA_SHARE
    | FILE_SHARE
    | STATIC_SUBSCRIBER
    | WALLPAPER
    | BACKUP
    | WINDOW
    | ENTERPRISE_ADMIN
    | THUMBNAIL
    | PREVIEW
    | PRINT
    | SHARE
    | PUSH
    | DRIVER
    | ACTION
    | ADS_SERVICE
    | EMBEDDED_UI
    | INSIGHT_INTENT_UI
    | UNSPECIFIED
    | UNKNOWN
    | ...
}
```

**功能：** 指示扩展组件的类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### ACCESSIBILITY

```cangjie
ACCESSIBILITY
```

**功能：** 无障碍服务扩展能力，支持访问与操作前台界面。

**起始版本：** 12

### ACTION

```cangjie
ACTION
```

**功能：** 自定义服务扩展能力，为开发者提供基于UIExtension的自定义操作业务模板。

**起始版本：** 12

### ADS_SERVICE

```cangjie
ADS_SERVICE
```

**功能：** 广告服务扩展能力，对外提供后台自定义广告业务服务，当前暂未支持。

**起始版本：** 12

### BACKUP

```cangjie
BACKUP
```

**功能：** 数据备份扩展能力，提供应用数据的备份恢复能力。

**起始版本：** 12

### DATA_SHARE

```cangjie
DATA_SHARE
```

**功能：** 数据共享扩展能力，用于对外提供数据读写服务。

**起始版本：** 12

### DRIVER

```cangjie
DRIVER
```

**功能：** 驱动扩展能力，提供外设驱动扩展能力，当前暂未支持。

**起始版本：** 12

### EMBEDDED_UI

```cangjie
EMBEDDED_UI
```

**功能：** 嵌入式UI扩展能力，提供跨进程界面嵌入的能力。

**起始版本：** 19

### ENTERPRISE_ADMIN

```cangjie
ENTERPRISE_ADMIN
```

**功能：** 企业设备管理扩展能力，提供企业管理时处理管理事件的能力，比如设备上应用安装事件、锁屏密码输入错误次数过多事件等。

**起始版本：** 12

### FILE_SHARE

```cangjie
FILE_SHARE
```

**功能：** 文件共享扩展能力，用于应用间的文件分享。预留能力，当前暂未支持。

**起始版本：** 12

### FORM

```cangjie
FORM
```

**功能：** 卡片扩展能力，提供卡片开发能力。

**起始版本：** 12

### INPUT_METHOD

```cangjie
INPUT_METHOD
```

**功能：** 输入法扩展能力，用于开发输入法应用。

**起始版本：** 12

### INSIGHT_INTENT_UI

```cangjie
INSIGHT_INTENT_UI
```

**功能：** 为开发者提供能被小艺意图调用，以窗口形态呈现内容的扩展能力。

**起始版本：** 19

### PREVIEW

```cangjie
PREVIEW
```

**功能：** 文件预览扩展能力，提供文件预览的能力，其他应用可以直接在应用中嵌入显示。预留能力，当前暂未支持。

**起始版本：** 12

### PRINT

```cangjie
PRINT
```

**功能：** 文件打印扩展能力，提供应用打印照片、文档等办公场景。当前支持图片打印，文档类型暂未支持。

**起始版本：** 12

### PUSH

```cangjie
PUSH
```

**功能：** 推送扩展能力，提供推送场景化消息能力。预留能力，当前暂未支持。

**起始版本：** 12

### SERVICE

```cangjie
SERVICE
```

**功能：** 后台服务扩展能力，提供后台运行并对外提供相应能力。

**起始版本：** 12

### SHARE

```cangjie
SHARE
```

**功能：** 提供分享业务能力，为开发者提供基于UIExtension的分享业务模板。

**起始版本：** 12

### STATIC_SUBSCRIBER

```cangjie
STATIC_SUBSCRIBER
```

**功能：** 静态广播扩展能力，用于处理静态事件，比如开机事件。

**起始版本：** 12

### THUMBNAIL

```cangjie
THUMBNAIL
```

**功能：** 文件缩略图扩展能力，用于为文件提供图标缩略图的能力。预留能力，当前暂未支持。

**起始版本：** 12

### UNKNOWN

```cangjie
UNKNOWN
```

**功能：** 未知类型的ExtensionAbility。

**起始版本：** 19

### UNSPECIFIED

```cangjie
UNSPECIFIED
```

**功能：** 不指定类型，配合queryExtensionAbilityInfo接口可以查询所有类型的ExtensionAbility。

**起始版本：** 12

### WALLPAPER

```cangjie
WALLPAPER
```

**功能：** 壁纸扩展能力，用于实现桌面壁纸。预留能力，当前暂未支持。

**起始版本：** 12

### WINDOW

```cangjie
WINDOW
```

**功能：** 界面组合扩展能力，允许系统应用进行跨应用的界面拉起和嵌入。

**起始版本：** 12