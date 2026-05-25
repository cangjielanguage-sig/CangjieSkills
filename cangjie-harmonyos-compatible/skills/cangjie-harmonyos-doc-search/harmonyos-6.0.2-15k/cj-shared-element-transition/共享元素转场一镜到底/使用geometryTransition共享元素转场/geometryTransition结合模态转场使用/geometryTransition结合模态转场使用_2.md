@State
    var expandImageSize: Int = 100
    @State
    var avatarSize: Int = 50

    let postOnAvatarClicked: (Int) -> Unit

    public func build() {
        Column() {
            Row() {
                Image(this.data.avatar).size(width: this.avatarSize, height: this.avatarSize).borderRadius(
                    this.avatarSize / 2).clip(true).onClick {
                    evt => this.postOnAvatarClicked(this.index)
                }
                    // 对头像绑定共享元素转场的id
                    .geometryTransition(this.index.toString(), followWithoutTransition: true).transition(
                    TransitionEffect.OPACITY.animation(AnimateParam(duration: 350, curve: Curve.Friction)))

                Text(this.data.name)
            }.justifyContent(FlexAlign.Center)

            Text(this.data.message)

            Row() {
                ForEach(
                    this.data.images,
                    {
                        imageResource: AppResource, index: Int => Image(imageResource).size(width: 100, height: 100)
                    }
                )
            }
        }.backgroundColor(Color.WHITE).size(width: 100.percent, height: 250).alignItems(HorizontalAlign.Start).padding(
            left: 10, top: 10)
    }
}
```

效果为点击主页的头像后，弹出模态页面显示个人信息，并且两个页面之间的头像做一镜到底动效：

![shared-element-transiton2](./figures/shared-element-transition2.gif)