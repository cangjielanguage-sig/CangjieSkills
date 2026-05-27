### geometryTransition结合模态转场使用

更多的场景中，需要对一个页面的元素与另一个页面的元素添加一镜到底动效。可以通过geometryTransition搭配模态转场接口实现。以点击头像弹出个人信息页的demo为例：

<!--run-->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.resource_manager.AppResource
import ohos.resource_manager.__GenerateResource__
import std.collection.ArrayList
import ohos.hilog.Hilog

let storage: LocalStorage = LocalStorage()

class PostData {
    public var avatar: AppResource = @r(app.media.app_foreground)
    public var name: String = ""
    public var message: String = ""
    public var images: Array<AppResource> = []

    public init(avatar: AppResource, name: String, message: String, images: Array<AppResource>) {
        this.avatar = avatar
        this.name = name
        this.message = message
        this.images = images
    }
}

@Entry
@Component
class EntryView {
    @State
    var isPersonalPageShow: Bool = false;
    @State
    var selectedIndex: Int = 0
    @State
    var alphaValue: Int = 1

    private var allPostData: Array<PostData> = [
        PostData(@r(app.media.flower), "Alice", "天气晴朗", [@r(app.media.spring), @r(app.media.tree)]),
        PostData(@r(app.media.sky), "Bob", "你好世界", [@r(app.media.island)]),
        PostData(@r(app.media.tree), "Carl", "万物生长", [@r(app.media.flower), @r(app.media.sky), @r(app.media.spring)]
        )
    ]

    public func onAppear() {
        AppLog.info("BindContentCover onAppear.")
    }
    public func onDisappear() {
        AppLog.info("BindContentCover onDisappear.")
    }

    private func onAvatarClicked(index: Int): Unit {
        this.selectedIndex = index
        animateTo(
            AnimateParam(duration: 350, curve: Curve.Friction),
            {
                =>
                this.isPersonalPageShow = !this.isPersonalPageShow
                this.alphaValue = 0
            }
        )
    }

    private func onPersonalPageBack(index: Int): Unit {
        animateTo(
            AnimateParam(duration: 350, curve: Curve.Friction),
            {
                =>
                this.isPersonalPageShow = !this.isPersonalPageShow
                this.alphaValue = 1
            }
        )
    }

    @Builder
    public func PersonalPageBuilder() {
        Column() {
            Image(this.allPostData[this.selectedIndex].avatar).size(width: 200, height: 200).borderRadius(100)
                // 头像配置共享元素效果，与点击的头像的id匹配
                .
                geometryTransition(this.selectedIndex.toString()).clip(true).transition(TransitionEffect.opacity(0.99))

            Text(this.allPostData[this.selectedIndex].name).font(TextFont(size: 30, weight: FontWeight.W600))
                // 对文本添加出现转场效果
                .transition(
                TransitionEffect.asymmetric(
                    TransitionEffect.OPACITY.combine(TransitionEffect.translate(TranslateOptions(x: 100, y: 100, z: 100)
                    )),
                    TransitionEffect.OPACITY.animation(AnimateParam(duration: 0))
                )
            )

            Text("你好，我是${this.allPostData[this.selectedIndex].name}").transition(
                TransitionEffect.asymmetric(
                    TransitionEffect.OPACITY.combine(TransitionEffect.translate(TranslateOptions(x: 100, y: 100, z: 100)
                    )),
                    TransitionEffect.OPACITY.animation(AnimateParam(duration: 0))
                )
            )
        }.padding(20).size(width: 360, height: 780).backgroundColor(Color.WHITE).onClick {
            evt => this.onPersonalPageBack(this.selectedIndex)
        }.transition(TransitionEffect.asymmetric(TransitionEffect.opacity(0.99), TransitionEffect.OPACITY))
    }

    func build() {
        Column() {
            ForEach(
                this.allPostData,
                itemGeneratorFunc: {
                    postData: PostData, index: Int => Column() {
                        Post(data: postData, index: index, postOnAvatarClicked: this.onAvatarClicked)
                    }.width(100.percent)
                }
            )
        }.size(width: 100.percent, height: 100.percent).backgroundColor(Color.GREY).bindContentCover(
            this.isPersonalPageShow,
            this.PersonalPageBuilder,
            ContentCoverOptions(
                modalTransition: ModalTransition.NONE,
                onAppear: onAppear,
                onDisappear: onDisappear
            )
        ).opacity(this.alphaValue)
    }
}

@Component
class Post {
    @Prop
    var data: PostData
    @Prop
    var index: Int