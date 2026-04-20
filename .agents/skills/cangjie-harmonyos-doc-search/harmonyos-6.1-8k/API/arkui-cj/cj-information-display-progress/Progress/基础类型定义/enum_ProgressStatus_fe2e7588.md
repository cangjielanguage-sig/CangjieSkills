### enum ProgressStatus

```cangjie
public enum ProgressStatus <: Equatable<ProgressStatus> {
    | Loading
    | Progressing
    | ...
}
```

**功能：** 当前进度条的状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ProgressStatus](#enum-progressstatus)>

#### Loading

```cangjie
Loading
```

**功能：** 加载状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### Progressing

```cangjie
Progressing
```

**功能：** 处理中状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### operator func !=(ProgressStatus)

```cangjie
public operator func !=(other: ProgressStatus): Bool
```

**功能：** 比较两个枚举值是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ProgressStatus](#enum-progressstatus)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不相等则返回true，否则返回false。|

#### operator func ==(ProgressStatus)

```cangjie
public operator func ==(other: ProgressStatus): Bool
```

**功能：** 比较两个枚举值是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ProgressStatus](#enum-progressstatus)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等则返回true，否则返回false。|