### geometryTransition结合模态转场使用

更多的场景中，需要对一个页面的元素与另一个页面的元素添加一镜到底动效。可以通过geometryTransition搭配模态转场接口实现。以点击头像弹出个人信息页的demo为例：

 <!--run-->

```cangjie
package ohos_app_cangjie_entry

import kit.ArkUI.*
import ohos.arkui.ui_context.*
import ohos.arkui.state_macro_manage.*
import ohos.resource_manager.AppResource
import ohos.resource.__GenerateResource__
import kit.PerformanceAnalysisKit.Hilog

let storage: LocalStorage = LocalStorage()

class PostData{
    public var avatar: AppResource = @r(app.media.foreground)
    public var name: String = ""
    public var message: String = ""
    public var images: Array<AppResource> = []

    public init(avatar: AppResource,name:String,message: String,images: Array<AppResource>) {
        this.avatar = avatar
        this.name = name
        this.message = message
        this.images = images
    }
}

@Entry
@Component
class EntryView {
    @State var isPersonalPageShow: Bool = false;
    @State var selectedIndex: Int = 0
    @State var alphaValue: Float64 = 1.0

    private var allPostData: Array<PostData> = [
        PostData(@r(app.media.startIcon),"Alice","天气晴朗",[@r(app.media.startIcon), @r(app.media.startIcon)] ),
        PostData(@r(app.media.startIcon),"Bob","你好世界",[@r(app.media.startIcon)]),
        PostData(@r(app.media.startIcon),"Carl","万物生长",[@r(app.media.startIcon),@r(app.media.startIcon),@r(app.media.startIcon)])
        ]

    public func onAppear() {
        Hilog.info(0, "cangjie", "BindContentCover onAppear.")
    }
    public func onDisappear() {
        Hilog.info(0, "cangjie", "BindContentCover onDisappear.")
    }

    private func onAvatarClicked(index: Int):Unit {
        this.selectedIndex = index
        getUIContext().animateTo(
            AnimateParam(duration: 350,curve: Curve.Friction),
            {
                =>
                this.isPersonalPageShow = !this.isPersonalPageShow
                this.alphaValue = 0.0
            }
        )
    }

    private func onPersonalPageBack(index: Int):Unit{
        getUIContext().animateTo(AnimateParam(duration: 350,curve: Curve.Friction),{
            =>
            this.isPersonalPageShow = !this.isPersonalPageShow;
            this.alphaValue = 1.0;
        })
    }

    @Builder
    public func PersonalPageBuilder(){
        Column(){
            Image(this.allPostData[this.selectedIndex].avatar)
            .size(width:200,height:200)
            .borderRadius(100)
            // 头像配置共享元素效果，与点击的头像的id匹配
            .geometryTransition(this.selectedIndex.toString())
            .clip(true)
            .transition(TransitionEffect.opacity(0.99))

            Text(this.allPostData[this.selectedIndex].name)
            // 对文本添加出现转场效果
            .transition(TransitionEffect.asymmetric(
                TransitionEffect.OPACITY.combine(TransitionEffect.translate(TranslateOptions(x:100,y:100,z:100))),
                TransitionEffect.OPACITY.animation(AnimateParam(duration: 0))))

            Text("你好，我是${this.allPostData[this.selectedIndex].name}")
            .transition(TransitionEffect.asymmetric(
                TransitionEffect.OPACITY.combine(TransitionEffect.translate(TranslateOptions(x:100,y:100,z:100))),
                TransitionEffect.OPACITY.animation(AnimateParam(duration: 0))))
        }
        .padding(20)
        .size(width:360,height:780)
        .backgroundColor(Color.White)
        .onClick({
            evt =>
            this.onPersonalPageBack(this.selectedIndex)
        })
        .transition(TransitionEffect.asymmetric(
            TransitionEffect.opacity(0.99),TransitionEffect.OPACITY
        ))
    }