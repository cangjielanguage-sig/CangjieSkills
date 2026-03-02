# 超简化版 - 读取 .env 文件并设置环境变量
$ScriptDir = $PSScriptRoot
if (-not $ScriptDir) { 
    $ScriptDir = (Get-Location).Path 
}
$envFile = Join-Path $ScriptDir ".claude\skills\cangjie-dev-harmonyos\scripts\.env"
if (-not (Test-Path $envFile)) {
    $envFile = Join-Path $ScriptDir ".env"
}

if (Test-Path $envFile) {
    Get-Content $envFile | ForEach-Object {
        if ($_.Contains('=') -and -not $_.StartsWith('#')) {
            $parts = $_.Split('=', 2)
            $key = $parts[0].Trim()
            $value = $parts[1].Trim()
            [System.Environment]::SetEnvironmentVariable($key, $value, "Process")
        }
    }
}

# 检查必要的环境变量
if (-not $env:DEVECO_HOME) {
    Write-Error "DEVECO_HOME Not Set Yet"
    exit 1
}

ohpm.bat install --all --registry https://ohpm.openharmony.cn/ohpm/ --strict_ssl true

& "$env:DEVECO_HOME\tools\node\node.exe" "$env:DEVECO_HOME\tools\hvigor\bin\hvigorw.js" --mode module -p module=entry@default SyncCangjieResource --analyze=normal --parallel --incremental --daemon

& "$env:DEVECO_HOME\tools\node\node.exe" "$env:DEVECO_HOME\tools\hvigor\bin\hvigorw.js" --mode module -p product=default assembleHap --analyze=normal --parallel --incremental --daemon

