### GEOLOCATION_ORIGINS_ALLOWED

```cangjie
GEOLOCATION_ORIGINS_ALLOWED
```

**功能：** 浏览器可以使用的默认地理位置。多个地理位置由空格分隔。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### HDC_STATUS

```cangjie
HDC_STATUS
```

**功能：** 是否启用USB设备上的硬盘控制器（HDC）。值为true，表示启用HDC；值为false，表示不启用HDC。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### SETUP_WIZARD_FINISHED

```cangjie
SETUP_WIZARD_FINISHED
```

**功能：** 是否已运行启动向导。值为0，表示启动向导尚未运行；值不是0，表示启动向导已运行。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### SKIP_USE_HINTS

```cangjie
SKIP_USE_HINTS
```

**功能：** 应用程序是否应在首次启动时尝试跳过所有介绍性提示。这适用于临时用户或熟悉环境的用户。值为1，表示应用程序将尝试在第一次启动时跳过所有介绍性提示；值为0，表示应用程序不会在首次启动时跳过介绍性提示。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### TOUCH_EXPLORATION_STATUS

```cangjie
TOUCH_EXPLORATION_STATUS
```

**功能：** 是否启用触摸浏览。值为1，表示启用触摸浏览；值为0，表示不启用触摸浏览。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### USB_STORAGE_STATUS

```cangjie
USB_STORAGE_STATUS
```

**功能：** 是否启用USB大容量存储。值为true，表示启用USB大容量存储；值为false，表示不启用USB大容量存储。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### func toString()

```cangjie
public override func toString(): String
```

**功能：** 返回设置设备常规信息的数据项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**返回值：**

| 类型  | 说明  |
| :------ | :------ |
| String | 设置设备常规信息的数据项。 |