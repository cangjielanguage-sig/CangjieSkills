## enum FinishCallbackType

```cangjie
public enum FinishCallbackType <: Equatable<FinishCallbackType> {
    | Removed
    | Logically
    | ...
}
```

**功能：** 动画结束时的回调类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[FinishCallbackType](#enum-finishcallbacktype)>

### Removed

```cangjie
Removed
```

**功能：** 当整个动画结束并立即删除时，将触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Logically

```cangjie
Logically
```

**功能：** 当动画在逻辑上处于下降状态，但可能仍处于其长尾状态时，将触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(FinishCallbackType)

```cangjie
public operator func ==(other: FinishCallbackType): Bool
```

**功能：** 判断两个FinishCallbackType枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FinishCallbackType](#enum-finishcallbacktype)|是|-|要比较的另一个FinishCallbackType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(FinishCallbackType)

```cangjie
public operator func !=(other: FinishCallbackType): Bool
```

**功能：** 判断两个FinishCallbackType枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FinishCallbackType](#enum-finishcallbacktype)|是|-|要比较的另一个FinishCallbackType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|