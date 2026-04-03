### func onError(?VoidCallback)

```cangjie
public func onError(event: ?VoidCallback): This
```

**功能：** 播放失败时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|?[VoidCallback](./cj-common-types.md#type-voidcallback)|是|-|回调函数，播放失败时触发。<br>初始值：{ => }|

### func onFinish(?VoidCallback)

```cangjie
public func onFinish(event: ?VoidCallback): This
```

**功能：** 播放结束时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|?[VoidCallback](./cj-common-types.md#type-voidcallback)|是|-|回调函数，播放结束时触发。<br>初始值：{ => }|

### func onPause(?VoidCallback)

```cangjie
public func onPause(event: ?VoidCallback): This
```

**功能：** 暂停播放时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|?[VoidCallback](./cj-common-types.md#type-voidcallback)|是|-|回调函数，暂停播放时触发。<br>初始值：{ => }|

### func onPrepared(?Callback\<PreparedInfo, Unit>)

```cangjie
public func onPrepared(callback: ?Callback<PreparedInfo, Unit>): This
```

**功能：** 视频准备完成时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[Callback](./cj-common-types.md#type-callbackt-v)\<[PreparedInfo](#class-preparedinfo), Unit>|是|-|回调函数，视频准备完成时触发。<br>初始值：{ _ => }|

### func onSeeked(?Callback\<PlaybackInfo, Unit>)

```cangjie
public func onSeeked(callback: ?Callback<PlaybackInfo, Unit>): This
```

**功能：** 操作进度条完成后触发该事件，上报播放时间信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[Callback](./cj-common-types.md#type-callbackt-v)\<[PlaybackInfo](#class-playbackinfo), Unit>|是|-|回调函数，操作进度条完成后触发。<br>初始值：{ _ => }|

### func onSeeking(?Callback\<PlaybackInfo, Unit>)

```cangjie
public func onSeeking(callback: ?Callback<PlaybackInfo, Unit>): This
```

**功能：** 操作进度条过程时触发该事件，上报时间信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[Callback](./cj-common-types.md#type-callbackt-v)\<[PlaybackInfo](#class-playbackinfo), Unit>|是|-|回调函数，操作进度条过程时触发。<br>初始值：{ _ => }|

### func onStart(?VoidCallback)

```cangjie
public func onStart(event: ?VoidCallback): This
```

**功能：** 播放时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|?[VoidCallback](./cj-common-types.md#type-voidcallback)|是|-|回调函数，播放时触发。<br>初始值：{ => }|

### func onUpdate(?Callback\<PlaybackInfo, Unit>)

```cangjie
public func onUpdate(callback: ?Callback<PlaybackInfo, Unit>): This
```

**功能：** 说明播放进度变化时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[Callback](./cj-common-types.md#type-callbackt-v)\<[PlaybackInfo](#class-playbackinfo), Unit>|是|-|回调函数，说明播放进度变化时触发。<br>初始值：{ _ => }|