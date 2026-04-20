### static func mix(LazySeq\<T>,LazySeq\<T>,LazySeq\<T>,LazySeq\<T>,LazySeq\<T>)

```cangjie
public static func mix(l1: LazySeq<T>, l2: LazySeq<T>, l3: LazySeq<T>, l4: LazySeq<T>, l5: LazySeq<T>): LazySeq<T> 
```

功能：五个序列穿插混合成一个。

参数：

- l1: [LazySeq](#class-lazyseqt)\<T> - 待穿插的序列。
- l2: [LazySeq](#class-lazyseqt)\<T> - 待穿插的序列。
- l3: [LazySeq](#class-lazyseqt)\<T> - 待穿插的序列。
- l4: [LazySeq](#class-lazyseqt)\<T> - 待穿插的序列。
- l5: [LazySeq](#class-lazyseqt)\<T> - 待穿插的序列。

返回值：

- [LazySeq](#class-lazyseqt)\<T> - 处理后的序列。

### static func of(Iterable\<T>)

```cangjie
public static func of(iterable: Iterable<T>): LazySeq<T>
```

功能：从迭代器构造一个序列。

参数：

- iterable: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 待处理的迭代器。

返回值：

- [LazySeq](#class-lazyseqt)\<T> - 处理后的序列。

### static func of(Array\<T>)

```cangjie
public static func of(array: Array<T>): LazySeq<T>
```

功能：从数组构造一个序列。

参数：

- array: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> - 待处理的数组。

返回值：

- [LazySeq](#class-lazyseqt)\<T> - 处理后的序列。