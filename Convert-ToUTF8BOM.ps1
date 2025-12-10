# Convert all Markdown files to UTF-8 with BOM
# This script processes all .md files in the project and ensures UTF-8 BOM encoding

$rootPath = "D:\OneDrive\OneDrive - Jakof\The-Resonant"

# Get all .md files recursively
$mdFiles = Get-ChildItem -Path $rootPath -Filter "*.md" -Recurse -File

$convertedCount = 0
$skippedCount = 0
$errorCount = 0

Write-Host "Starting UTF-8 BOM conversion..." -ForegroundColor Cyan
Write-Host "Found $($mdFiles.Count) markdown files" -ForegroundColor Yellow
Write-Host ""

foreach ($file in $mdFiles) {
    try {
        # Read file content
        $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
        
        # Check if file already has UTF-8 BOM
        $bytes = [System.IO.File]::ReadAllBytes($file.FullName)
        $hasBOM = ($bytes.Length -ge 3) -and ($bytes[0] -eq 0xEF) -and ($bytes[1] -eq 0xBB) -and ($bytes[2] -eq 0xBF)
        
        if (-not $hasBOM) {
            # Write with UTF-8 BOM
            $utf8BOM = New-Object System.Text.UTF8Encoding $true
            [System.IO.File]::WriteAllText($file.FullName, $content, $utf8BOM)
            
            Write-Host "? Converted: $($file.FullName.Replace($rootPath, ''))" -ForegroundColor Green
            $convertedCount++
        } else {
            Write-Host "? Already UTF-8 BOM: $($file.FullName.Replace($rootPath, ''))" -ForegroundColor Gray
            $skippedCount++
        }
    }
    catch {
        Write-Host "? ERROR: $($file.FullName.Replace($rootPath, ''))" -ForegroundColor Red
        Write-Host "  $($_.Exception.Message)" -ForegroundColor Red
        $errorCount++
    }
}

Write-Host ""
Write-Host "=== CONVERSION SUMMARY ===" -ForegroundColor Cyan
Write-Host "Converted:     $convertedCount files" -ForegroundColor Green
Write-Host "Already UTF-8: $skippedCount files" -ForegroundColor Gray
Write-Host "Errors:        $errorCount files" -ForegroundColor Red
Write-Host ""

if ($errorCount -eq 0) {
    Write-Host "? All files processed successfully!" -ForegroundColor Green
} else {
    Write-Host "? Some files had errors. Please review." -ForegroundColor Yellow
}

# List specific directories processed
Write-Host ""
Write-Host "Directories processed:" -ForegroundColor Cyan
$directories = $mdFiles | ForEach-Object { $_.DirectoryName } | Select-Object -Unique | Sort-Object
foreach ($dir in $directories) {
    $count = ($mdFiles | Where-Object { $_.DirectoryName -eq $dir }).Count
    Write-Host "  $($dir.Replace($rootPath, '').TrimStart('\')) ($count files)" -ForegroundColor White
}
