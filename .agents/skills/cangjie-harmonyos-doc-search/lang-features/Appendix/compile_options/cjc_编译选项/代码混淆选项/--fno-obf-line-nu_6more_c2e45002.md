### `--fno-obf-line-number`

禁止外形混淆功能混淆堆栈信息中的行号信息。

### `--fobf-cf-flatten`

开启控制流平坦化混淆。

混淆代码中既存的控制流，使其转移逻辑变得复杂。

### `--fno-obf-cf-flatten`

关闭控制流平坦化混淆。

### `--fobf-cf-bogus`

开启虚假控制流混淆。

在代码中插入虚假的控制流，使代码逻辑变得复杂。

### `--fno-obf-cf-bogus`

关闭虚假控制流混淆。

### `--fobf-all`

开启所有混淆功能。

指定该选项等同于同时指定以下选项：

- `--fobf-string`
- `--fobf-const`
- `--fobf-layout`
- `--fobf-cf-flatten`
- `--fobf-cf-bogus`