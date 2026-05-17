#!/usr/bin/env pwsh
# Build EPUB from Chapters/
# Usage: ./build_epub.ps1 [-Lang en|de] [-Out path\output.epub]

param(
    [string]$Lang = "en",
    [string]$Out  = ""
)

$Root     = Split-Path $PSScriptRoot -Parent
$ChapDir  = Join-Path $Root "Chapters"
$Cover    = Join-Path $Root "CoverArt.jpg"
$MetaFile = Join-Path $Root "Scripts\_epub_meta.yaml"

if ($Out -eq "") {
    $Out = Join-Path $Root "The_Resonant_EN.epub"
    if ($Lang -eq "de") {
        $ChapDir = Join-Path $Root "Deutsch"
        $Out     = Join-Path $Root "The_Resonant_DE.epub"
    }
}

# ── Chapter order ────────────────────────────────────────────────────────────
# Preface first, then ordered by filename prefix, then back-matter
$allFiles = Get-ChildItem -Path $ChapDir -Filter "*.md" | Sort-Object Name

$preface   = $allFiles | Where-Object { $_.Name -like "__-*" }
$mainChaps = $allFiles | Where-Object { $_.Name -notlike "__-*" }
$ordered   = @($preface) + @($mainChaps)

$fileList  = $ordered | ForEach-Object { "`"$($_.FullName)`"" }

# ── Metadata ─────────────────────────────────────────────────────────────────
@"
---
title: 'The Resonant'
author: 'J. He'
lang: en
rights: 'All rights reserved'
...
"@ | Set-Content -Path $MetaFile -Encoding UTF8

# ── Build ─────────────────────────────────────────────────────────────────────
$pandocArgs = @(
    "--from=markdown+smart"
    "--to=epub3"
    "--split-level=1"
    "--toc"
    "--toc-depth=1"
    "--metadata-file=`"$MetaFile`""
    "--output=`"$Out`""
)

if (Test-Path $Cover) {
    $pandocArgs += "--epub-cover-image=`"$Cover`""
}

$pandocArgs += $fileList

$cmd = "pandoc " + ($pandocArgs -join " ")
Write-Host "Building: $Out"
Invoke-Expression $cmd

if ($LASTEXITCODE -eq 0) {
    $size = [math]::Round((Get-Item $Out).Length / 1KB, 1)
    Write-Host "Done: $Out ($size KB)"
} else {
    Write-Error "pandoc exited with code $LASTEXITCODE"
}

# cleanup temp meta
Remove-Item $MetaFile -ErrorAction SilentlyContinue
