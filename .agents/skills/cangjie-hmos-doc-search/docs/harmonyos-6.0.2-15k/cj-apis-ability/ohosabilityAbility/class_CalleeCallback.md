## class CalleeCallback

```cangjie
public class CalleeCallback <: Callback1ArgumentWithReturn<MessageSequence, Parcelable> {
    public CalleeCallback(let callback: (MessageSequence) -> Parcelable)
}
```

**功能：** 通用组件服务端注册消息通知的回调函数类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**父类型：**

- [Callback1ArgumentWithReturn](../../cj-apis-base/.overview.md)\<[MessageSequence](../../cj-apis-rpc/.overview.md), [Parcelable](../../cj-apis-rpc/.overview.md)>

### CalleeCallback((MessageSequence) -> Parcelable)

```cangjie
public CalleeCallback(let callback: (MessageSequence) -> Parcelable)
```

**功能：** CalleeCallback的主构造器。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([MessageSequence](../../cj-apis-rpc/.overview.md))->[Parcelable](../../cj-apis-rpc/.overview.md)|是|-|发送需传递的数据的回调函数。|

### func invoke(MessageSequence)

```cangjie
public func invoke(arg1: MessageSequence): Parcelable
```

**功能：** 触发回调函数。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arg1|[MessageSequence](../../cj-apis-rpc/.overview.md)|是|-|发送需传递的数据。|

**返回值：**

|类型|说明|
|:----|:----|
|[Parcelable](../../cj-apis-rpc/.overview.md)|返回的数据对象。|