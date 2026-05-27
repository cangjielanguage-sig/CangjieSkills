# 选项卡（Tabs）

当页面信息较多时，为了让用户能够聚焦于当前显示的内容，需要对页面内容进行分类，提高页面空间利用率。[Tabs](../../API_Reference/source_zh_cn/arkui-cj/cj-navigation-switching-tabs.md)组件可以在一个页面内快速实现视图内容的切换，一方面提升查找信息的效率，另一方面精简用户单次获取到的信息量。

## 基本布局

Tabs组件的页面组成包含两个部分，分别是TabContent和TabBar。TabContent是内容页，TabBar是导航页签栏，页面结构如下图所示，根据不同的导航类型，布局会有区别，可以分为底部导航、顶部导航、侧边导航，其导航栏分别位于底部、顶部和侧边。

**图1** Tabs组件布局示意图

![tab-1](figures/tab-1.png)

> **说明：**
>
> - TabContent组件不支持设置通用宽度属性，其宽度默认撑满Tabs父组件。
> - TabContent组件不支持设置通用高度属性，其高度由Tabs父组件高度与TabBar组件高度决定。

Tabs使用花括号包裹TabContent，如图2，其中TabContent显示相应的内容页。

![tab-2](figures/tab-2.png)

每一个TabContent对应的内容需要有一个页签，可以通过TabContent的tabBar属性进行配置。在如下TabContent组件上设置tabBar属性，可以设置其对应页签中的内容，tabBar作为内容的页签。

```cangjie
  TabContent() {
    Text('首页的内容').fontSize(30)
  }
 .tabBar('首页')
 ```

设置多个内容时，需在Tabs内按照顺序放置。

```cangjie
Tabs() {
  TabContent() {
    Text('首页的内容').fontSize(30)
  }
  .tabBar('首页')

  TabContent() {
    Text('推荐的内容').fontSize(30)
  }
  .tabBar('推荐')

  TabContent() {
    Text('发现的内容').fontSize(30)
  }
  .tabBar('发现')

  TabContent() {
    Text('我的内容').fontSize(30)
  }
  .tabBar("我的")
}
```

## 底部导航

底部导航是应用中最常见的一种导航方式。底部导航位于应用一级页面的底部，用户打开应用，能够分清整个应用的功能分类，以及页签对应的内容，并且其位于底部更加方便用户单手操作。底部导航一般作为应用的主导航形式存在，其作用是将用户关心的内容按照功能进行分类，迎合用户使用习惯，方便在不同模块间的内容切换。

**图3** 底部导航栏

![tab-3](figures/tab-3.gif)

导航栏位置使用Tabs的barPosition参数进行设置。默认情况下，导航栏位于顶部，此时，barPosition为BarPosition.Start。设置为底部导航时，需要将barPosition设置为BarPosition.End。

```cangjie
Tabs(BarPosition.End) {
    // TabContent的内容，例如：首页、发现、推荐、我的
    // ...
}
```

## 顶部导航

当内容分类较多，用户对不同内容的浏览概率相差不大，需要经常快速切换时，一般采用顶部导航模式进行设计，作为对底部导航内容的进一步划分，常见一些资讯类应用对内容的分类为关注、视频、数码，或者主题应用中对主题进行进一步划分为图片、视频、字体等。

**图4** 顶部导航栏

![tab-4](figures/tab-4.gif)

```cangjie
Tabs(BarPosition.Start) {
    // TabContent的内容，例如:关注、视频、游戏、数码、科技、体育、影视
    // ...
}
```

## 侧边导航

侧边导航是应用较为少见的一种导航模式，更多适用于横屏界面，用于对应用进行导航操作，由于用户的视觉习惯是从左到右，侧边导航栏默认为左侧侧边栏。

**图5** 侧边导航栏

![tab-5](figures/tab-5.png)

实现侧边导航栏需要将Tabs的vertical属性设置为true，vertical默认值为false，表明内容页和导航栏垂直方向排列。

```cangjie
Tabs(BarPosition.Start) {
    // TabContent的内容，例如：首页、发现、推荐、我的
    // ...
}
.vertical(true)
```

> **说明：**
>
> - vertical为false时，tabbar的宽度默认为撑满屏幕的宽度，需要设置barWidth为合适值。
> - vertical为true时，tabbar的高度默认为实际内容的高度，需要设置barHeight为合适值。