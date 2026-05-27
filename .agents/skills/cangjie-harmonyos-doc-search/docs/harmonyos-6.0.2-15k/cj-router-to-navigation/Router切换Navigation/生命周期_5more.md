## 生命周期

Router页面生命周期为@Entry页面中的通用方法，主要有如下四个生命周期：

```cangjie

// 在执行其build()函数之前执行的回调
public func aboutToAppear(){
}

// 在自定义组件析构销毁之前执行的回调
public func aboutToDisappear(){
}

// 页面显示时的回调
public func onPageShow(){
}

// 页面隐藏时的回调
public func onPageHide(){
}

// 页面隐藏时的回调
public fun onPageHide(){
}
```

其生命周期时序如下图所示：

![zhouqi](figures/zhouqi.jpg)

Navigation作为路由容器，其生命周期承载在NavDestination组件上，以组件事件的形式开放。

```cangjie
@Component
class EntryView {
    protected func aboutToDisappear() {
    }

    protected func aboutToAppear() {
    }

    func build() {
        NavDestination() {
            // ...
        }
        .onWillAppear({=>
        })
        .onAppear({=>
        })
        .onWillShow({=>
        })
        .onShown({=>
        })
        .onWillHide({=>
        })
        .onHide({=>
        })
        .onWillDisappear({=>
        })
        .onDisAppear({=>
        })
        .
    }
}
```

## 转场动画

Router和Navigation都提供了系统的转场动画也提供了自定义转场的能力。

其中Router自定义页面转场通过通用方法pageTransition()实现，具体请参见Router[页面转场动画](./cj-page-transition-animation.md)。

Navigation作为路由容器组件，其内部的页面切换动画本质上属于组件跟组件之间的属性动画。

## 共享元素转场

页面和页面之间跳转的时候需要进行共享元素过渡动画，Router可以通过通用属性sharedTransition来实现共享元素转场，具体请参见如下链接：

[Router共享元素转场动画](../../API_Reference/source_zh_cn/arkui-cj/cj-animation-sharedtransition.md#共享元素转场-sharedtransition)

Navigation也提供了共享元素一镜到底的转场能力，需要配合geometryTransition属性，在子页面（NavDestination）之间切换时，可以实现共享元素转场，具体请参见[Navigation共享元素转场动画](cj-navigation-navigation.md#共享元素转场)。

## 跨包路由

Navigation作为路由组件，默认支持跨包跳转。

1. 在mainPage中导入自定义组件，并添加到pageMap中，即可正常调用。

    <!-- run -->

    ```cangjie
    package ohos_app_cangjie_entry

    import kit.UIKit.*
    import ohos.state_macro_manage.*

    @Builder
    func pageMap(name: String) {
        // 1.定义路由映射表
        if (name == "PageInHSP") {
            PageInHSP()
        }
    }

    @Entry
    @Component
    class EntryView {
        var pageInfos: NavPathStack = NavPathStack()
        public func build() {
            Navigation(pageInfos) {
                Button("Navigation page").onClick {
                    // 1.定义路由映射表
                    pageInfos.pushPath(NavPathInfo("PageInHSP", "pageOne test"))
                }
            }.navDestination(bind<String>(pageMap, this))
        }
    }

    @Component
    class PageInHSP {
        var pageInfos: NavPathStack = NavPathStack()
        public func build() {
            NavDestination() {
                Text("Page One").onClick {
                    evt => pageInfos.pop()
                }
            }.onReady {
                context => pageInfos = context.pathStack
            }.onBackPressed {
                pageInfos.pop()
                true
            }
        }
    }
    ```

以上是通过**静态依赖**的形式完成了跨包的路由。

## 路由拦截

Router原生没有提供路由拦截的能力，开发者需要自行封装路由跳转接口，并在自己封装的接口中做路由拦截的判断并重定向路由。