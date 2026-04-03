# Router切换Navigation

鉴于组件导航(Navigation)支持更丰富的动效、一次开发多端部署能力和更灵活的栈操作。本文主要从页面跳转、动效和生命周期等方面介绍如何从Router切换到Navigation。

## 页面结构

Router路由的页面是一个@Entry修饰的Component。

以下为Router页面的示例。

<!-- run -->

```cangjie
// index.cj
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var message: String = "Hello World";
    func build() {
        Row() {
            Column() {
                Text(this.message).fontSize(10).fontWeight(FontWeight.Bold)
                Button("router to pageOne").stateEffect(true).width(120).height(80).margin(40).onClick(
                    {
                    => Router.pushUrl(url: "pageOne", // 目标url
                    params: "pagesparams", mode: RouterMode.Standard,
                        callback: {code =>})
                })
            }.width(100)
        }.height(100)
    }
}
```

<!-- run -->

```cangjie
//pageOne.cj
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class pageOne {
    @State
    var message: String = "This is pageOne";
    func build() {
        Row() {
            Column() {
                Text(this.message).fontSize(10).fontWeight(FontWeight.Bold)
                Button("router back to Index").stateEffect(true).width(120).height(80).margin(40).onClick(
                    {
                    => Router.back();
                })
            }.width(100)
        }.height(100)
    }
}
```

而基于Navigation的路由页面分为导航页和子页，导航页又叫Navbar，是Navigation包含的子组件，子页是NavDestination包含的子组件。

以下为Navigation导航页以及子页的示例。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Builder
func pageMap(name: String) {
    if (name == "pageOne") {
        PageOne()
    }
}

@Entry
@Component
class EntryView {
    var pageInfos: NavPathStack = NavPathStack()
    public func build() {
        Navigation(pageInfos) {
            Button("Navigation page").onClick {
                pageInfos.pushPath(NavPathInfo("pageOne", "pageOne test"))
            }
        }.navDestination(bind<String>(pageMap, this))
    }
}

@Component
class PageOne {
    var pageInfos: NavPathStack = NavPathStack()

    public func build() {
        NavDestination() {
            Column() {
                Button("回到首页", ButtonOptions(shape: ButtonType.Capsule)).width(80.percent).height(40).onClick {
                    => this.pageInfos.pop()
                }
            }
        }.title("pageOne").onReady {
            context => this.pageInfos = context.pathStack
        }.onBackPressed {
            this.pageInfos.pop()
            true
        }
    }
}
```