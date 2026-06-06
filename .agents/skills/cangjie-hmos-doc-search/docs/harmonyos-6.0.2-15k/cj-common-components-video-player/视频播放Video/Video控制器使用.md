## Video控制器使用

Video控制器主要用于控制视频的状态，包括播放、暂停、停止以及设置进度等，详情请参见[VideoController使用说明](../../API_Reference/source_zh_cn/arkui-cj/cj-image-video-video.md#class-videocontroller)。

- 默认控制器

  默认的控制器支持视频的开始、暂停、进度调整、全屏显示四项基本功能。

  <!-- run -->

  ```cangjie
  package ohos_app_cangjie_entry

  import kit.UIKit.*
  import ohos.state_macro_manage.*
  import ohos.resource_manager.*

  @Entry
  @Component
  class EntryView {
      @State
      var videoSrc: AppResource = @rawfile("video.mp4")
      @State
      var previewUri: AppResource = @r(app.media.preview)
      @State
      var curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X

      func build() {
          Row() {
              Column() {
                  Video(src: this.videoSrc, previewUri: this.previewUri, currentProgressRate: this.curRate)
              }.width(100.percent)
          }.height(100.percent)
      }
  }
  ```

- 自定义控制器

  使用自定义的控制器，先将默认控制器关闭掉，之后可以使用button以及slider等组件进行自定义的控制与显示，适合在自定义较强的场景下使用。

  <!-- run -->

  ```cangjie
  package ohos_app_cangjie_entry

  import kit.UIKit.*
  import ohos.state_macro_manage.*
  import ohos.resource_manager.*

  @Entry
  @Component
  class EntryView {
      @State
      var videoSrc: AppResource = @rawfile("video.mp4")
      @State
      var previewUri: AppResource = @r(app.media.preview)
      @State
      var curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X
      @State
      var isAutoPlay: Bool = false
      @State
      var showControls: Bool = true
      @State
      var sliderStartTime: String = ""
      @State
      var currentTime: Int32 = 0
      @State
      var durationTime: Int32 = 0
      var controller: VideoController = VideoController()
      func build() {
          Row() {
              Column() {
                  Video(src: this.videoSrc, previewUri: this.previewUri, currentProgressRate: this.curRate,
                      controller: this.controller).controls(false).autoPlay(true).onPrepared(
                      {
                      value => this.durationTime = value
                  }).onUpdate({
                      value => this.currentTime = value
                  })
                  Row() {
                      Text("${this.currentTime}s")
                      Slider(value: Float64(this.currentTime), min: 0.0, max: Float64(this.durationTime)).onChange(
                          {
                          value: Float64, mode: SliderChangeMode => this.controller.setCurrentTime(Int32(value),
                              SeekMode.Accurate)
                      }).width(85.percent)
                      Text("${this.durationTime}s")
                  }.opacity(0.8).width(100.percent)
              }.width(100.percent)
          }.height(100.percent)
      }
  }
  ```