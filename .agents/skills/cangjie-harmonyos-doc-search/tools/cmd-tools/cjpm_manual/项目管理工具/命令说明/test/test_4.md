`cjpm test` 参数选项使用示例:

```text
输入：
cjpm test src --coverage
cjcov --root=./ --html-details -o html_output
输出：cjpm test success
覆盖率生成：在 html_output 目录下会生成 html 文件，总的覆盖率报告文件名固定为 index.html
```

```text
输入: cjpm test --filter=*
输出: cjpm test success
```

```text
输入: cjpm test src --report-path=reports --report-format=xml
输出: cjpm test success
```

> **注意：**
>
> `cjpm test` 会自动构建所有带有 `mock` 支持的包，因此在测试中，开发者可以对自定义的类或依赖源模块的类进行 `mock` 测试。为了能够从一些二进制依赖中 `mock` 类，应该通过 `cjpm build --mock` 来构建带有 `mock` 支持的类。