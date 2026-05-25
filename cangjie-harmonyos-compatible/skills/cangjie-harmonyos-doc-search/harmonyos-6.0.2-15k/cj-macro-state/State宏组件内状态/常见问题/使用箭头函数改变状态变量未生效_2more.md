### 使用箭头函数改变状态变量未生效

箭头函数体内的this对象，就是定义该函数时所在的作用域指向的对象，而不是使用时所在的作用域指向的对象。所以要将当前this.vm传入，调用代理状态变量的属性赋值。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Observed
class PlayDetailViewModel {
    @Publish
    var coverUrl: UInt32
    var changeCoverUrl: (PlayDetailViewModel) -> Unit
}

@Entry
@Component
class EntryView {
    @State
    var vm: PlayDetailViewModel = PlayDetailViewModel(coverUrl: 0x00ff00,
        changeCoverUrl: {model: PlayDetailViewModel => model.coverUrl = 0x00F5FF})
    func build() {
        Column() {
            Text(this.vm.coverUrl.toString()).width(100).height(100).backgroundColor(this.vm.coverUrl)
            Button('点击改变颜色').onClick(
                {
                    evt =>
                    let self = this.vm
                    this.vm.changeCoverUrl(self)
                }
            )
        }
    }
}
```

![Video-state-PlayDetail](figures/Video-state-PlayDetail.gif)

### 状态变量只能影响其直接绑定的UI组件的刷新

【示例1】

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Observed
class Info {
    @Publish
    var address: String = '杭州'
}

@Entry
@Component
class EntryView {
    @State
    var message: String = '上海'
    @State
    var info: Info = Info()
    public func aboutToAppear() {
        this.info.address = this.message
    }
    func build() {
        Column() {
            Text(this.message)
            Text(this.info.address)
            Button('change').onClick({
                evt => this.info.address = '北京'
            })
        }
    }
}
```

![Video-State-Ui1](figures/Video-State-Ui1.gif)

以上示例点击Button('change')，只会触发第二个Text组件的刷新，因为message是简单类型string，简单类型是值拷贝，所以点击按钮改变的是info中的address值，不会影响this.message的值。

【示例2】

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Observed
class Info {
    @Publish
    var address: String = '杭州'
}

@Observed
class User {
    @Publish
    var infomation: Info
}

@Entry
@Component
class EntryView {
    @State
    var info: Info = Info(address: '上海')
    @State
    var user: User = User(infomation: Info(address: '天津'))
    public func aboutToAppear() {
        this.user.infomation = this.info
    }
    func build() {
        Column() {
            Text(this.info.address)
            Text(this.user.infomation.address)
            Button('change').onClick(
                {
                    evt =>
                    this.user.infomation = Info(address: '广州')
                    this.user.infomation.address = '北京'
                }
            )
        }
    }
}
```

![Video-state-Ui3](figures/Video-State-Ui3.gif)

上述示例中，点击Button('change')，只会触发第二个Text组件的刷新。这是因为点击按钮后，首先执行`this.user.infomation = Info(address: '广州')`，会创建一个新的Info对象。再执行`this.user.infomation.address = '北京'`，改变的是这个新创建的Info对象中的address值，而原始的Info对象中的address值不会受到影响。