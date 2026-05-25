## 事件调用

Video组件回调事件主要为播放开始、暂停结束、播放失败、播放停止、视频准备和操作进度条等事件，除此之外，Video组件也支持通用事件的调用，如点击、触摸等事件的调用。详情请参见[事件说明](../reference/arkui-cj/cj-image-video-video.md#组件事件)。

<!-- code_check_manual -->

```cangjie
@Component
class VideoPlayer {
    private var controller: VideoController = VideoController()
    private var previewUris: AppResource = @r(app.media.preview)
    private var innerResource: AppResource = @rawfile("videoTest.mp4")

    func build() {
        Column() {
            Video(src: this.innerResource, previewUri: this.previewUris, controller: this.controller)
                .onUpdate({ value => // 更新事件回调
                    Hilog.info(0, "cangjie", "video update.")
                })
                .onPrepared({ value => // 准备事件回调
                    Hilog.info(0, "cangjie", "video prepared.")
                })
                .onError({ => // 失败事件回调
                    Hilog.info(0, "cangjie", "video error.")
                })
        }
    }
}
```

## Video控制器使用

Video控制器主要用于控制视频的状态，包括播放、暂停、停止以及设置进度等，详情请参见[VideoController使用说明](../reference/arkui-cj/cj-image-video-video.md#class-videocontroller)。

- 默认控制器

  默认的控制器支持视频的开始、暂停、进度调整、全屏显示四项基本功能。

     <!-- run -->

  ```cangjie
  package ohos_app_cangjie_entry

  import kit.ArkUI.*
  import ohos.arkui.state_macro_manage.*
  import ohos.resource.*

  @Entry
  @Component
  class EntryView {
      @State var videoSrc: AppResource = @r(app.media.startIcon) // 需要传入正确的视频数据源
      @State var previewUri: AppResource = @r(app.media.startIcon)
      @State var curRate: PlaybackSpeed = PlaybackSpeed.SpeedForward100X

      func build() {
          Row() {
              Column() {
                  Video(src: this.videoSrc, previewUri: this.previewUri, currentProgressRate: this.curRate)
              }
              .width(100.percent)
          }
          .height(100.percent)
      }
  }
  ```

- 自定义控制器

  使用自定义的控制器，先将默认控制器关闭掉，之后可以使用[button](./cj-common-components-button.md)以及[slider](../reference/arkui-cj/cj-button-picker-slider.md)等组件进行自定义的控制与显示，适合在自定义较强的场景下使用。

     <!-- run -->

  ```cangjie
  package ohos_app_cangjie_entry

  import kit.ArkUI.*
  import ohos.arkui.state_macro_manage.*
  import ohos.resource.*

  @Entry
  @Component
  class EntryView {
      @State var videoSrc: AppResource = @r(app.media.startIcon) // 需要传入正确的视频数据源
      @State var previewUri: AppResource = @r(app.media.startIcon)
      @State var curRate: PlaybackSpeed = PlaybackSpeed.SpeedForward100X
      @State var isAutoPlay: Bool = false
      @State var showControls: Bool = true
      @State var sliderStartTime: String = ""
      @State var currentTime: Int32 = 0
      @State var durationTime: Int32 = 0
      var controller: VideoController = VideoController()
      func build() {
          Row() {
              Column() {
                  Video(src: this.videoSrc, previewUri: this.previewUri, currentProgressRate: this.curRate,
                      controller: this.controller)
                      .controls(false)
                      .autoPlay(true)
                      .onPrepared({
                              value => this.durationTime = value.duration.getOrThrow()
                          })
                      .onUpdate({
                              value => this.currentTime = value.time.getOrThrow()
                          })
                  Row() {
                      Text("${this.currentTime}s")
                      Slider(value: Float64(this.currentTime),  min: 0.0, max: Float64(this.durationTime))
                          .onChange({ value: Float64, mode: SliderChangeMode =>
                                  this.controller.setCurrentTime(Int32(value), SeekMode.Accurate)
                              })
                          .width(85.percent)
                      Text("${this.durationTime}s")
                  }
                  .opacity(0.8)
                  .width(100.percent)
              }.width(100.percent)
          }.height(100.percent)
      }
  }
  ```