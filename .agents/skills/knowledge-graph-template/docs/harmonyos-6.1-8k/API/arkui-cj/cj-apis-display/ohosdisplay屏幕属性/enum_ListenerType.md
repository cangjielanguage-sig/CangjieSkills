## enum ListenerType

```cangjie
public enum ListenerType <: Equatable<ListenerType> {
    | ListenerTypeAdd
    | ListenerTypeRemove
    | ListenerTypeChange
    | ListenerTypeFoldStatusChange
    | ListenerTypeFoldAngleChange
    | ListenerTypeCaptureStatusChange
    | ListenerTypeFoldDisplayModeChange
    | ListenerTypeAvailableAreaChange
    | ...
}
```

**功能：** 监听事件枚举。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**父类型：**

- Equatable\<[ListenerType](#enum-listenertype)>

### ListenerTypeAdd

```cangjie
ListenerTypeAdd
```

**功能：** 添加显示变化事件类型。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### ListenerTypeRemove

```cangjie
ListenerTypeRemove
```

**功能：** 移除显示变化事件类型。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### ListenerTypeChange

```cangjie
ListenerTypeChange
```

**功能：** 显示变化事件类型。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### ListenerTypeFoldStatusChange

```cangjie
ListenerTypeFoldStatusChange
```

**功能：** 折叠状态变化事件类型。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### ListenerTypeFoldAngleChange

```cangjie
ListenerTypeFoldAngleChange
```

**功能：** 折叠角度变化事件类型。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### ListenerTypeCaptureStatusChange

```cangjie
ListenerTypeCaptureStatusChange
```

**功能：** 捕获状态变化事件类型。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### ListenerTypeFoldDisplayModeChange

```cangjie
ListenerTypeFoldDisplayModeChange
```

**功能：** 折叠显示模式变化事件类型。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### ListenerTypeAvailableAreaChange

```cangjie
ListenerTypeAvailableAreaChange
```

**功能：** 可用区域变化事件类型。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### operator func !=(ListenerType)

```cangjie
public operator func !=(other: ListenerType): Bool
```

**功能：** 不等比较运算符。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ListenerType](#enum-listenertype)|是|-|要比较的另一个ListenerType实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，不相等时返回true。|

### operator func ==(ListenerType)

```cangjie
public operator func ==(other: ListenerType): Bool
```

**功能：** 相等比较运算符。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ListenerType](#enum-listenertype)|是|-|要比较的另一个ListenerType实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，相等时返回true。|