### func onFullscreenChange(?Callback\<FullscreenInfo, Unit>)

```cangjie
public func onFullscreenChange(callback: ?Callback<FullscreenInfo, Unit>): This
```

**功能：** 视频进入和退出全屏时触发该回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[Callback](./cj-common-types.md#type-callbackt-v)\<[FullscreenInfo](#class-fullscreeninfo), Unit>|是|-|视频进入和退出全屏时的回调函数。<br>初始值：{ _ => }|