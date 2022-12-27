
Set-ExecutionPolicy -Scope CurrentUser -Force Unrestricted


try { NonsenseString }
catch {
  Write-Host "An error occurred:"
  Write-Host $_
}


Set-ExecutionPolicy -Scope CurrentUser -Force Undefined