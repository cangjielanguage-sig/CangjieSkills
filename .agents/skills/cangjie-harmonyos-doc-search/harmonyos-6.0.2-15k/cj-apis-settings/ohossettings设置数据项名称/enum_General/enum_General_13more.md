## enum General

```cangjie
public enum General <: ToString {
    | SETUP_WIZARD_FINISHED
    | END_BUTTON_ACTION
    | AIRPLANE_MODE_STATUS
    | ACCELEROMETER_ROTATION_STATUS
    | DEVICE_PROVISION_STATUS
    | HDC_STATUS
    | BOOT_COUNTING
    | CONTACT_METADATA_SYNC_STATUS
    | DEVELOPMENT_SETTINGS_STATUS
    | DEVICE_NAME
    | USB_STORAGE_STATUS
    | DEBUGGER_WAITING
    | DEBUG_APP_PACKAGE
    | ACCESSIBILITY_STATUS
    | ACTIVATED_ACCESSIBILITY_SERVICES
    | GEOLOCATION_ORIGINS_ALLOWED
    | SKIP_USE_HINTS
    | TOUCH_EXPLORATION_STATUS
    | ...
}
```

**功能：** 提供设置设备常规信息的数据项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**父类型：**

- ToString

### ACCELEROMETER_ROTATION_STATUS

```cangjie
ACCELEROMETER_ROTATION_STATUS
```

**功能：** 是否使用加速计更改屏幕方向，即是否启用自动旋转。值为1，表示启用加速度计；  值为0，表示不启用加速计。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### ACCESSIBILITY_STATUS

```cangjie
ACCESSIBILITY_STATUS
```

**功能：** 是否启用辅助功能。值为1，表示启用辅助功能；值为0，表示不启用辅助功能。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### ACTIVATED_ACCESSIBILITY_SERVICES

```cangjie
ACTIVATED_ACCESSIBILITY_SERVICES
```

**功能：** 已激活的辅助功能的列表。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### AIRPLANE_MODE_STATUS

```cangjie
AIRPLANE_MODE_STATUS
```

**功能：** 是否启用飞行模式。值为1，表示启用飞行模式；值为0，表示不启用飞行模式。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### BOOT_COUNTING

```cangjie
BOOT_COUNTING
```

**功能：** 设备开机后的启动操作数。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### CONTACT_METADATA_SYNC_STATUS

```cangjie
CONTACT_METADATA_SYNC_STATUS
```

**功能：** 是否启用联系人元数据同步。值为true，表示启用同步；值为false，表示不启用同步。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### DEBUGGER_WAITING

```cangjie
DEBUGGER_WAITING
```

**功能：** 设备在启动应用程序进行调试时是否等待调试器进行调试。值为1，表示设备等待调试器；值为0，表示系统不会等待调试器，因此应用程序会正常运行。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### DEBUG_APP_PACKAGE

```cangjie
DEBUG_APP_PACKAGE
```

**功能：** 要调试的应用程序的bundle name。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### DEVELOPMENT_SETTINGS_STATUS

```cangjie
DEVELOPMENT_SETTINGS_STATUS
```

**功能：** 是否启用开发人员选项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### DEVICE_NAME

```cangjie
DEVICE_NAME
```

**功能：** 设备名称。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### DEVICE_PROVISION_STATUS

```cangjie
DEVICE_PROVISION_STATUS
```

**功能：** 是否预配设备。在具有单个系统用户的多用户设备上，当值为true时，屏幕可能会被锁定。此外，其他功能无法在系统用户上启动，除非它们被标记为在屏幕锁定上显示。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### END_BUTTON_ACTION

```cangjie
END_BUTTON_ACTION
```

**功能：** 在用户不在呼叫中时，用户按下呼叫结束按钮会发生的情况。值为0，表示没有任何反应；值为1，表示显示主屏幕；值为2，表示设备进入睡眠状态，屏幕锁定值为3，表示显示主屏幕。如果用户已在主屏幕上，设备将进入睡眠状态。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19