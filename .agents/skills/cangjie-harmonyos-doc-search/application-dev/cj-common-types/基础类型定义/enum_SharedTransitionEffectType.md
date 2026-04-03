## enum SharedTransitionEffectType

```cangjie
public enum SharedTransitionEffectType <: Equatable<SharedTransitionEffectType> {
    | Static
    | Exchange
    | ...
}
```

**功能：** 共享元素转场动效类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[SharedTransitionEffectType](#enum-sharedtransitioneffecttype)>

### Static

```cangjie
Static
```

**功能：** 目标页面元素的位置保持不变，可以配置透明度动画。目前，只有为重定向到目标页面而配置的静态效果才会生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Exchange

```cangjie
Exchange
```

**功能：** 将源页面元素移动到目标页面元素位置并适当缩放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(SharedTransitionEffectType)

```cangjie
public operator func ==(other: SharedTransitionEffectType): Bool
```

**功能：** 判断两个SharedTransitionEffectType枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SharedTransitionEffectType](#enum-sharedtransitioneffecttype)|是|-|要比较的另一个SharedTransitionEffectType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(SharedTransitionEffectType)

```cangjie
public operator func !=(other: SharedTransitionEffectType): Bool
```

**功能：** 判断两个SharedTransitionEffectType枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SharedTransitionEffectType](#enum-sharedtransitioneffecttype)|是|-|要比较的另一个SharedTransitionEffectType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|