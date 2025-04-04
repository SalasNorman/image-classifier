$Env:CONDA_EXE = "/workspaces/image-classifier/venv/bin/conda"
$Env:_CE_M = $null
$Env:_CE_CONDA = $null
$Env:_CONDA_ROOT = "/workspaces/image-classifier/venv"
$Env:_CONDA_EXE = "/workspaces/image-classifier/venv/bin/conda"
$CondaModuleArgs = @{ChangePs1 = $True}
Import-Module "$Env:_CONDA_ROOT\shell\condabin\Conda.psm1" -ArgumentList $CondaModuleArgs

Remove-Variable CondaModuleArgs