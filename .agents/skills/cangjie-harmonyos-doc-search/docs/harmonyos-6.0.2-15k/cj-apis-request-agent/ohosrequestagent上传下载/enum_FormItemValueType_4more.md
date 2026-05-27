## enum FormItemValueType

```cangjie
public enum FormItemValueType {
    | STR(String)
    | FILE(FileSpec)
    | FILES(Array<FileSpec>)
    | ...
}
```

**功能：** 表单项的文件信息枚举类型。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

### FILE(FileSpec)

```cangjie
FILE(FileSpec)
```

**功能：** 表示文件信息。

**起始版本：** 12

### FILES(Array\<FileSpec>)

```cangjie
FILES(Array<FileSpec>)
```

**功能：** 表示多个文件信息。

**起始版本：** 12

### STR(String)

```cangjie
STR(String)
```

**功能：** 表示文件路径。

**起始版本：** 12

## enum Mode

```cangjie
public enum Mode <: ToString {
    | BACKGROUND
    | FOREGROUND
    | ...
}
```

**功能：** 定义模式选项。前端任务在应用切换到后台一段时间后失败/暂停；后台任务不受影响。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

**父类型：**

- ToString

### BACKGROUND

```cangjie
BACKGROUND
```

**功能：** 表示后台任务。

**起始版本：** 12

### FOREGROUND

```cangjie
FOREGROUND
```

**功能：** 表示前端任务。

**起始版本：** 12

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 15

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|

## enum Network

```cangjie
public enum Network <: ToString {
    | ANY
    | WIFI
    | CELLULAR
    | ...
}
```

**功能：** 定义网络选项。网络不满足设置条件时，未执行的任务等待执行，执行中的任务失败/暂停。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

**父类型：**

- ToString

### ANY

```cangjie
ANY
```

**功能：** 表示不限网络类型。

**起始版本：** 12

### CELLULAR

```cangjie
CELLULAR
```

**功能：** 表示蜂窝数据网络。

**起始版本：** 12

### WIFI

```cangjie
WIFI
```

**功能：** 表示无线网络。

**起始版本：** 12

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 15

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|

## enum State

```cangjie
public enum State <: ToString {
    | INITIALIZED
    | WAITING
    | RUNNING
    | RETRYING
    | PAUSED
    | STOPPED
    | COMPLETED
    | FAILED
    | REMOVED
    | ...
}
```

**功能：** 定义任务当前的状态。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

**父类型：**

- ToString

### COMPLETED

```cangjie
COMPLETED
```

**功能：** 表示任务完成。

**起始版本：** 12

### FAILED

```cangjie
FAILED
```

**功能：** 表示任务失败。

**起始版本：** 12

### INITIALIZED

```cangjie
INITIALIZED
```

**功能：** 通过配置信息（Config）创建初始化任务。

**起始版本：** 12

### PAUSED

```cangjie
PAUSED
```

**功能：** 表示任务暂停，通常后续会恢复任务。

**起始版本：** 12

### REMOVED

```cangjie
REMOVED
```

**功能：** 表示任务移除。

**起始版本：** 12

### RETRYING

```cangjie
RETRYING
```

**功能：** 表示任务至少失败一次，现在正在再次处理中。

**起始版本：** 12

### RUNNING

```cangjie
RUNNING
```

**功能：** 表示正在处理的任务。

**起始版本：** 12

### STOPPED

```cangjie
STOPPED
```

**功能：** 表示任务停止。

**起始版本：** 12

### WAITING

```cangjie
WAITING
```

**功能：** 表示任务缺少运行或重试的资源与网络状态不匹配。

**起始版本：** 12

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 15

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|