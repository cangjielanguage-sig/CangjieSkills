### class PanGestureRecognizer

```cangjie
public class PanGestureRecognizer <: GestureRecognizer {}
```

**功能：** 拖动手势识别器对象。

**起始版本：** 20

**父类型：**

- [GestureRecognizer](#class-gesturerecognizer)

#### func getPanGestureOptions()

```cangjie
public func getPanGestureOptions(): PanGestureOptions
```

**功能：** 返回当前滑动手势识别器的属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|[PanGestureOptions](./cj-universal-gesture-pangesture.md#class-pangestureoptions)|当前拖动手势识别器的属性。|

### class ScrollableTargetInfo

```cangjie
public class ScrollableTargetInfo <: EventTargetInfo {}
```

**功能：** 手势识别器对应的滚动类容器组件的信息。

**起始版本：** 20

**父类型：**

- [EventTargetInfo](#class-eventtargetinfo)

#### func isBegin()

```cangjie
public func isBegin(): Bool
```

**功能：** 返回当前滚动类容器组件是否在顶部，如果为Swiper组件且在循环模式下返回false。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Bool|当前滚动类容器组件是否在顶部。true表示组件在顶部，false表示组件不在顶部。|

#### func isEnd()

```cangjie
public func isEnd(): Bool
```

**功能：** 返回当前滚动类容器组件是否在底部，如果为Swiper组件且在循环模式下返回false。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Bool|当前滚动类容器组件是否在底部。true表示组件在底部，false表示组件不在底部。|

### enum GestureRecognizerState

```cangjie
public enum GestureRecognizerState {
    | Ready
    | Detecting
    | Pending
    | Blocked
    | Successful
    | Failed
}
```

**功能：** 定义手势识别器状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### Blocked

```cangjie
Blocked
```

**功能：** 阻塞状态。

#### Detecting

```cangjie
Detecting
```

**功能：** 检测状态。

#### Failed

```cangjie
Failed
```

**功能：** 失败状态。

#### Pending

```cangjie
Pending
```

**功能：** 等待状态。

#### Ready

```cangjie
Ready
```

**功能：** 准备状态。

#### Successful

```cangjie
Successful
```

**功能：** 成功状态。