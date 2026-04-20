### hitTestBehavior对手势和事件的控制

hitTestBehavior属性可以实现在复杂的多层级场景下，一些组件能够响应手势和事件，而一些组件不能响应手势和事件。

```cangjie
ComponentA() {
    ComponentB()
    .onTouch({ => })
    .gesture(TapGesture(count: 1))

    ComponentC() {
        ComponentD()
        .onTouch({ => })
        .gesture(TapGesture(count: 1))
    }
    .onTouch({ => })
    .gesture(TapGesture(count: 1))
    .hitTestBehavior(HitTestMode.Block)
}
.onTouch({ => })
.gesture(TapGesture(count: 1))
```

HitTestMode.Block自身会响应触摸测试，阻塞子节点和兄弟节点的触摸测试，从而导致子节点和兄弟节点的onTouch事件和手势均无法触发。

当组件C未设置hitTestBehavior时，点击组件D区域，组件A、组件C和组件D的onTouch事件会触发，组件D的点击手势会触发。

当组件C设置了hitTestBehavior为HitTestMode.Block时，点击组件D区域，组件A和组件C的onTouch事件会触发，组件D的onTouch事件未触发。同时，由于组件D的点击手势因为被阻塞而无法触发，组件C的点击手势会触发。

```cangjie
Stack A() {
    ComponentB()
    .onTouch({ => })
    .gesture(TapGesture(count: 1))

    ComponentC()
    .onTouch({ => })
    .gesture(TapGesture(count: 1))
    .hitTestBehavior(HitTestMode.Transparent)
}
.onTouch({ => })
.gesture(TapGesture(count: 1))
```

HitTestMode.Transparent自身响应触摸测试，不会阻塞兄弟节点的触摸测试。

当组件C未设置hitTestBehavior时，点击组件B和组件C的重叠区域时，Stack A和组件C的onTouch事件会触发，组件C的点击事件会触发，组件B的onTouch事件和点击手势均不触发。

而当组件C设置hitTestBehavior为HitTestMode.Transparent时，点击组件B和组件C的重叠区域，组件A和组件C不受到影响与之前一致，组件A和组件C的onTouch事件会触发，组件C的点击手势会触发。而组件B因为组件C设置了HitTestMode.Transparent，组件B也收到了Touch事件，从而组件B的onTouch事件和点击手势触发。

```cangjie
ComponentA() {
    ComponentB()
    .onTouch({ => })
    .gesture(TapGesture(count: 1))
}
.onTouch({ => })
.gesture(TapGesture(count: 1))
.hitTestBehavior(HitTestMode.None)
```

HitTestMode.None自身不响应触摸测试，不会阻塞子节点和兄弟节点的触摸控制。

当组件A未设置hitTestBehavior时，点击组件B区域时，组件A和组件B的onTouch事件均会触发，组件B的点击手势会触发。

当组件A设置hitTestBehavior为HitTestMode.None时，点击组件B区域时，组件B的onTouch事件触发，而组件A的onTouch事件无法触发，组件B的点击手势触发。

针对简单的场景，建议在单个组件上绑定hitTestBehavior。

针对复杂场景，建议在多个组件上绑定不同的hitTestBehavior来控制Touch事件的分发。