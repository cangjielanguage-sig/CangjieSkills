# ohos.multimedia_avsession（媒体会话管理）

媒体会话管理模块提供媒体播控相关功能的接口，目的是让应用接入播控中心。

## 导入模块

```cangjie
import kit.AVSessionKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func createAVSession(CPointer\<Unit>, String, AVSessionType)

```cangjie
public func createAVSession(context: CPointer<Unit>, tag: String, `type`: AVSessionType): AVSession
```

**功能：** 创建会话对象，一个Ability只能存在一个会话，重复创建会失败。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|CPointer\<Unit>|是|-|需要使用[UIAbilityContext](../AbilityKit/cj-apis-ability.md#class-uiabilitycontext)，用于系统获取应用组件的相关信息。|
|tag|String|是|-|会话的自定义名称。|
|\`type\`|[AVSessionType](#enum-avsessiontype)|是|-|会话的自定义名称。|

**返回值：**

|类型|说明|
|:----|:----|
|[AVSession](#class-avsession)|回调返回会话实例对象，可用于获取会话ID，以及设置元数据、播放状态，发送按键事件等操作。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|

## class AVCallState

```cangjie
public class AVCallState {
    public AVCallState (
        public var state: CallState,
        public var muted: Bool
    )
}
```

**功能：** 通话状态相关属性。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

### var muted

```cangjie
public var muted: Bool
```

**功能：** 通话mic是否静音。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var state

```cangjie
public var state: CallState
```

**功能：** 当前通话状态。

**类型：** [CallState](#enum-callstate)

**读写能力：** 可读写

**起始版本：** 19

### AVCallState(CallState, Bool)

```cangjie
public AVCallState (
    public var state: CallState,
    public var muted: Bool
)
```

**功能：** AVCallState构造函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|state|[CallState](#enum-callstate)|是|-|当前通话状态。|
|muted|Bool|是|-|通话mic是否静音。|