## 组件事件

### func onOffsetChange((Float64) -> Unit)

```cangjie
public func onOffsetChange(callback: (Float64) -> Unit): This
```

**功能：** 下拉距离发生变化时触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Float64)->Unit|是|-|下拉距离。 <br> 单位：vp。|

### func onRefreshing(() -> Unit)

```cangjie
public func onRefreshing(callback: ()-> Unit): This
```

**功能：** 进入刷新状态时触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|进入刷新状态时触发回调。|

### func onStateChange((RefreshStatus) -> Unit)

```cangjie
public func onStateChange(callback: (RefreshStatus)-> Unit): This
```

**功能：** 设置刷新状态变更时，触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([RefreshStatus](cj-common-types.md#enum-refreshstatus))->Unit|是|-|刷新状态。|

## 基础类型定义

### class RefreshParams

```cangjie
public class RefreshParams {
    public var refreshing: Bool
    public var changeEvent:(Bool) -> Unit
    public init(refreshing!: Bool)
    public init(refreshing!: (Bool, (Bool) -> Unit))
}
```

**功能：** 用于设置Refresh组件参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var changeEvent

```cangjie
public var changeEvent:(Bool) -> Unit
```

**功能：** 配合 @Binder 宏使用，用于refreshing属性的双向绑定。

**类型：** (Bool)->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var refreshing

```cangjie
public var refreshing: Bool
```

**功能：** 当前组件是否正在刷新。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(Bool)

```cangjie
public init(refreshing!: Bool)
```

**功能：** 创建一个 RefreshParams 对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|refreshing|Bool|是|-| **命名参数。** 标识刷新组件当前是否正在刷新。|

#### init((Bool,(Bool) -> Unit))

```cangjie
public init(refreshing!: (Bool, (Bool) -> Unit))
```

**功能：** 根据刷新状态创建一个 RefreshParams 对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|refreshing|(Bool,(Bool)->Unit)|是|-| **命名参数。** 标识刷新组件当前是否正在刷新。|