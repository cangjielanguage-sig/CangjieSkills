## 编辑列表

列表的编辑模式用途十分广泛，常见于待办事项管理、文件管理、备忘录的记录管理等应用场景。在列表的编辑模式下，新增和删除列表项是最基础的功能，其核心是对列表项对应的数据集合进行数据添加和删除。

## 长列表的处理

[循环渲染](./rendering_control/cj-rendering-control-foreach.md)适用于短列表，当构建具有大量列表项的长列表时，如果直接采用循环渲染方式，会一次性加载所有的列表元素，会导致页面启动时间过长，影响用户体验。因此，推荐使用[数据懒加载](./rendering_control/cj-rendering-control-lazyforeach.md)（LazyForEach）方式实现按需迭代加载数据，从而提升列表性能。

关于长列表按需加载优化的具体实现可参考[数据懒加载](./rendering_control/cj-rendering-control-lazyforeach.md)章节中的示例。

当使用懒加载方式渲染列表时，为了更好的列表滚动体验，减少列表滑动时出现白块，List组件提供了cachedCount参数用于设置列表项缓存数，只在懒加载LazyForEach中生效。

```cangjie
List() {
  // ...
}.cachedCount(3)
```

以垂直列表为例：

- 若懒加载是用于ListItem，当列表为单列模式时，会在List显示的ListItem前后各缓存cachedCount个ListItem；若是多列模式下，会在List显示的ListItem前后各缓存cachedCount \* 列数个ListItem。

- 若懒加载是用于ListItemGroup，无论单列模式还是多列模式，都是在List显示的ListItem前后各缓存cachedCount个ListItemGroup。

> **说明：**
>
> cachedCount的增加会增大UI的CPU、内存开销。使用时需要根据实际情况，综合性能和用户体验进行调整。
>
> 列表使用数据懒加载时，除了显示区域的列表项和前后缓存的列表项，其他列表项会被销毁。