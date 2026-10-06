<#
.SYNOPSIS
    为 Shimamura-Skill 生成一个可直接上传分享的发布包。

.DESCRIPTION
    默认**排除 references/source/**（15 册原著中文译本全文，约 3.25 MB，受版权保护）。
    Skill 去掉语料后仍可正常工作：研究结论都写在 references/research/ 里，
    每条都带 `文件名:行号`，使用者自备合法来源的文本即可复现。

    加 -IncludeSource 才会把语料一起打包（请自行确认发布地区的合规性）。

.EXAMPLE
    pwsh scripts/make-release.ps1
    pwsh scripts/make-release.ps1 -IncludeSource
#>
[CmdletBinding()]
param(
    [string]$OutDir,
    [switch]$IncludeSource
)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot

# 默认输出到 <工作区>\dist\Shimamura-Skill（技能目录 = <工作区>\.dsh\skills\Shimamura-Skill）
if (-not $OutDir) {
    $ws = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $root))
    $OutDir = Join-Path $ws 'dist\Shimamura-Skill'
}

$dstFull = [System.IO.Path]::GetFullPath($OutDir)

# 安全阀：绝不能把发布包放进 DSH 的技能根，否则会被当成第二个同名 Skill
foreach ($skillsRoot in (Join-Path (Split-Path -Parent (Split-Path -Parent $root)) 'skills'), (Join-Path $env:USERPROFILE '.dsh\skills')) {
    if ($dstFull.StartsWith([System.IO.Path]::GetFullPath($skillsRoot), [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "拒绝执行：输出目录落在 DSH 技能根内（$skillsRoot）。这会产生第二个名为 shimamura 的 Skill。请改用其它路径。"
    }
}
if ($dstFull -eq [System.IO.Path]::GetFullPath($root) -or $dstFull.StartsWith([System.IO.Path]::GetFullPath($root) + '\')) {
    throw "拒绝执行：输出目录不能位于技能目录内部。"
}

$dst = $dstFull
if (Test-Path $dst) { Remove-Item $dst -Recurse -Force }
New-Item -ItemType Directory -Force $dst | Out-Null

# 顶层文件
Copy-Item (Join-Path $root 'SKILL.md') $dst
Copy-Item (Join-Path $root 'README.md') $dst

# 子目录（references 单独处理，以便排除 source）
foreach ($d in 'agents', 'scripts') {
    $src = Join-Path $root $d
    if (Test-Path $src) { Copy-Item $src (Join-Path $dst $d) -Recurse }
}

$refDst = Join-Path $dst 'references'
New-Item -ItemType Directory -Force $refDst | Out-Null
Get-ChildItem (Join-Path $root 'references') -Force | ForEach-Object {
    $exclude = ($_.Name -eq 'source' -and -not $IncludeSource)
    if (-not $exclude) { Copy-Item $_.FullName (Join-Path $refDst $_.Name) -Recurse -Force }
}

# 校验：发布包里的相对链接不应指向被排除的目录
$skill = Get-Content (Join-Path $dst 'SKILL.md') -Raw -Encoding UTF8
if (-not $IncludeSource -and $skill -match 'references/source') {
    Write-Warning 'SKILL.md 仍提到 references/source —— 这在发布包里是预期的（作为可选路径说明），但请确认语气不像是"已包含"。'
}

$mb = [math]::Round((Get-ChildItem $dst -Recurse -File | Measure-Object Length -Sum).Sum / 1MB, 2)
$n  = (Get-ChildItem $dst -Recurse -File).Count
Write-Host "发布包：$dst"
Write-Host "  文件数：$n    大小：$mb MB    含语料：$([bool]$IncludeSource)"
Write-Host "  下一步：确认 references/citation-report.md 里 ERROR = 0，然后打包上传。"
