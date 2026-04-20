## enum SystemBarType

```cangjie
public enum SystemBarType <: Equatable<SystemBarType> {
    | Status
    | Navigation
    | ...
}
```

**功能：** 系统栏类型枚举。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**父类型：**

- Equatable\<[SystemBarType](#enum-systembartype)>

### Status

```cangjie
Status
```

**功能：** 状态栏。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### Navigation

```cangjie
Navigation
```

**功能：** 导航栏。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### operator func !=(SystemBarType)

```cangjie
public operator func !=(other: SystemBarType): Bool
```

**功能：** 不等比较运算符。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SystemBarType](#enum-systembartype)|是|-|要比较的另一个SystemBarType实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，不相等时返回true。|

### operator func ==(SystemBarType)

```cangjie
public operator func ==(other: SystemBarType): Bool
```

**功能：** 相等比较运算符。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SystemBarType](#enum-systembartype)|是|-|要比较的另一个SystemBarType实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，相等时返回true。|